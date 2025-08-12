
# Monitoring Guide (Evidently)

Jalankan:
```bash
python -m src.monitoring.data_drift
```

Output:
- `reports/evidently_data_drift.html` — laporan visual
- `reports/drift_summary.json` — ringkasan metrik (+flag alert)

Konfigurasi:
- `DRIFT_ALERT_THRESHOLD` (default 0.2)
- `ALERT_SLACK_WEBHOOK` untuk notifikasi Slack

Tips:
- Sesuaikan jendela reference/current sesuai bisnis.
- Jadwalkan via Airflow (`smart_retail_monitoring_and_retrain`).
