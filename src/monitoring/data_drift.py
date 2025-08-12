
import os, json
from pathlib import Path
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import requests

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "raw" / "sales.csv"
REPORTS = BASE / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

THRESHOLD_ALERT = float(os.getenv("DRIFT_ALERT_THRESHOLD", "0.2"))
SLACK_WEBHOOK = os.getenv("ALERT_SLACK_WEBHOOK", "")

def send_slack(text: str):
    if not SLACK_WEBHOOK:
        return False
    try:
        requests.post(SLACK_WEBHOOK, json={"text": text}, timeout=10)
        return True
    except Exception:
        return False

def main():
    if not DATA.exists():
        raise SystemExit("No data found. Run: python -m src.data.make_mock_data")

    df = pd.read_csv(DATA, parse_dates=["date"]).sort_values("date")
    if len(df) < 60:
        raise SystemExit("Not enough rows for drift check")

    ref = df[df["date"] <= (df["date"].min() + pd.Timedelta(days=90))]
    cur = df[df["date"] >= (df["date"].max() - pd.Timedelta(days=30))]

    cols = [c for c in ["qty","price","revenue"] if c in df.columns]
    ref = ref[cols + ["store_id","product_id","date"]]
    cur = cur[cols + ["store_id","product_id","date"]]

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=cur)
    html_path = REPORTS / "evidently_data_drift.html"
    json_path = REPORTS / "evidently_data_drift.json"
    report.save_html(html_path)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report.as_dict(), f)

    # compute drift ratio
    d = report.as_dict()
    drift_ratio = 0.0
    for m in d.get("metrics", []):
        if m.get("metric") == "DataDriftTable":
            num = m.get("result", {}).get("number_of_drifted_columns", 0)
            total = m.get("result", {}).get("number_of_columns", 1)
            drift_ratio = num / max(total, 1)
            break

    summary = {"drift_ratio": drift_ratio, "threshold": THRESHOLD_ALERT, "alert": drift_ratio >= THRESHOLD_ALERT, "html_report": str(html_path)}
    with open(REPORTS / "drift_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    if summary["alert"]:
        send_slack(f":rotating_light: Data drift alert ({drift_ratio:.0%}) — see {html_path}")

    print(json.dumps(summary))

if __name__ == "__main__":
    main()
