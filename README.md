# Smart Retail Intelligence — by **Bernadus Boli**

Forecasting • Promo/Price Uplift • FastAPI • Streamlit • MLOps (CI/Monitoring)



&#x20;&#x20;

> **Ringkas** — Proyek portofolio end‑to‑end untuk menonjolkan peran **AI Engineer & Data Analyst**: data pipeline → model peramalan **XGBoost** → estimator **uplift** (promo/harga) → **API FastAPI** → **Dashboard Streamlit** (*what‑if*) + **CI GitHub Actions** + **Monitoring (Evidently)**.

---

## 🔗 Demo

- **Hugging Face Space**: → `(https://huggingface.co/spaces/bernadlein/bernadusboli-smart-retail-intel)`
- **Repo GitHub**: [https://github.com/bernadlein/smart-retail-intel](https://github.com/bernadlein/smart-retail-intel)

> Jika butuh live URL, saya juga menyiapkan bundle untuk HF Spaces (lihat folder `smart-retail-intel-hf-space`).

---

## ✨ Fitur Utama

- **Demand Forecasting (XGBoost)**: model global dengan encoding store/product, fitur lag & kalender, *recursive horizon* (7–60 hari).
- **Baseline Forecast**: MA7 sederhana sebagai pembanding cepat.
- **Promo/Price Uplift**: pendekatan *two‑model* (treated vs control) untuk mengukur dampak skenario promosi/penyesuaian harga.
- **API FastAPI**: endpoint `/forecast`, `/forecast/xgb`, dan `/uplift` dengan dokumentasi OpenAPI.
- **Dashboard Streamlit**: histori penjualan, pemilihan model, *what‑if* (Δ harga/promo), grafik uplift & metrik ringkas.
- **MLOps**: workflow **CI** (GitHub Actions), **Evidently** untuk data drift + opsi **Slack alert**, **Airflow DAG** untuk retrain/monitoring mingguan.

---

## 🧭 Arsitektur

```
[Data (Synthetic CSV)] → [Feature Build] → [Model Training (XGB)]
                                         ↘
                                    [FastAPI Inference] → [Streamlit Dashboard]
```

---

## 🗂️ Struktur Proyek

```
smart-retail-intel/
├─ app/                 # Streamlit dashboard
├─ api/                 # FastAPI service
├─ src/
│  ├─ data/             # data generation
│  ├─ features/         # feature utils
│  ├─ models/           # training: baseline & XGB
│  ├─ uplift/           # two-model uplift trainer
│  └─ utils/
├─ sql/                 # skema & seed (opsional, Postgres)
├─ infra/               # docker-compose (opsional)
├─ airflow/             # DAG skeleton + monitoring/retrain
├─ docs/images/         # cover & screenshots
├─ reports/             # evidently outputs
├─ content/             # linkedin post, demo script, resume bullets
├─ tests/               # pytest examples
├─ .github/workflows/   # CI pipeline
├─ requirements.txt
└─ README.md
```

---

## 🚀 Quickstart (Local Dev)

**Prasyarat**: Python 3.10/3.11, `pip`

```bash
# 1) Virtual env & install
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2) Generate data sintetis
python -m src.data.make_mock_data

# 3) Latih model (opsional baseline)
python -m src.models.train_baseline

# 4) Latih model XGBoost & Uplift (advanced)
python -m src.models.train_xgb
python -m src.uplift.train_uplift

# 5) Jalankan API & UI
uvicorn api.main:app --reload          # Swagger di http://localhost:8000/docs
streamlit run app/app.py               # App di http://localhost:8501
```

> **MLflow (opsional)**: set `MLFLOW_TRACKING_URI="file:./mlruns"` untuk melacak eksperimen.

---

## 🧪 API Endpoints

- `POST /forecast` — baseline MA7 dengan knob *what‑if* (price, promo)
- `POST /forecast/xgb` — peramalan XGBoost (recursive)
- `POST /uplift` — estimasi uplift skenario vs kontrol

**Contoh Request** `POST /forecast/xgb`

```json
{
  "store_id": "S01",
  "product_id": "P001",
  "horizon": 14,
  "price_delta_pct": 5.0,
  "promo_flag": true
}
```

**Contoh Response (ringkas)**

```json
{
  "model": "xgb",
  "forecast": [
    {"date": "2025-08-13", "qty_forecast": 87.2},
    {"date": "2025-08-14", "qty_forecast": 88.0}
  ]
}
```

---

## 🛰️ Monitoring (Evidently) & Alerts

Generate drift report (reference: 90 hari awal, current: 30 hari terakhir). **Optional Slack alert** via env `ALERT_SLACK_WEBHOOK`.

```bash
python -m src.monitoring.data_drift
# output: reports/evidently_data_drift.html, reports/drift_summary.json
```

Konfigurasi:

- `DRIFT_ALERT_THRESHOLD` (default `0.2` → alert jika ≥20% fitur terdampak)
- `ALERT_SLACK_WEBHOOK` untuk notifikasi Slack

---

## 🧰 Makefile Shortcuts

```bash
make data         # generate synthetic data
make xgb          # train XGBoost
make uplift       # train uplift two-model
make monitor      # run Evidently drift report
make api          # run FastAPI
make app          # run Streamlit
```

---

## 🏗️ CI (GitHub Actions)

Workflow minimal untuk test otomatis berada di `.github/workflows/ci.yml`.

---

---

## 📚 Dokumentasi Tambahan

- **Model Card**: docs/MODEL\_CARD.md
- **Data Card**: docs/DATA\_CARD.md
- **Monitoring Guide**: docs/monitoring\_guide.md
- **Airflow Setup**: docs/airflow\_setup.md
- **Contributing**: CONTRIBUTING.md • **Code of Conduct**: CODE\_OF\_CONDUCT.md • **Security**: SECURITY.md

---

## 📌 Roadmap Singkat

- v0: baseline + XGB + uplift + API + dashboard
- v1: monitoring data drift (Evidently) & scheduling Airflow
- v1.1: recommender sederhana + AB testing simulator
- v1.2: Power BI executive view

---

## 📝 Lisensi

Kode dirilis di bawah **MIT License** (lihat file `LICENSE`). Data yang digunakan bersifat **sintetis**.

---

## 👤 Author

**Bernadus Boli**\
AI Engineer / Data Analyst\
GitHub: [https://github.com/bernadlein](https://github.com/bernadlein)\
LinkedIn:(https://www.linkedin.com/in/bernadus-boli-657a17197/)

---

## 🙌 Ucapan Terima Kasih

Komunitas open‑source: FastAPI, Streamlit, XGBoost, scikit‑learn, MLflow, Evidently, Airflow, dan lainnya.

