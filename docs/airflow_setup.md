
# Airflow Setup (Local)

1. Install Airflow sesuai OS Anda, atau gunakan docker-compose sendiri.
2. Pastikan Python env memiliki dependensi project.
3. Salin DAG di `airflow/dags/` ke folder DAG Airflow Anda.
4. Jalankan `airflow webserver` dan `airflow scheduler`.
5. Aktifkan DAG `smart_retail_monitoring_and_retrain`.

DAG akan:
- generate data → monitoring drift → train xgb & uplift.
