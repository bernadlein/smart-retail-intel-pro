
# Model Card — XGBoost Global Forecasting

**Tujuan**: Prediksi kuantitas harian per SKU–store (horizon 7–60 hari).  
**Pemilik**: Bernadus Boli

## Data Pelatihan
- Synthetic retail: transaksi 180 hari, fitur `qty`, `price`, `promo_flag` + kalender.
- Pra‑proses: lag(1,7,28), MA7, dow/week/month/year, encoding store/product.

## Evaluasi
- TimeSeriesSplit (5 fold). Metrik utama: MAE/SMAPE.
- Baseline pembanding: lag‑7 & MA7.

## Keterbatasan
- Data sintetis → tidak mencerminkan noise dunia nyata sepenuhnya.
- Tidak memodelkan efek stok/inventory & cuaca.

## Etika & Bias
- Tidak menggunakan data personal; privasi aman.
- Pastikan transparansi saat mengomunikasikan hasil berbasis data sintetis.

## Versi & Artifak
- Model: `models/xgb/model.json|joblib`
- Meta: `models/xgb/meta.json` (fitur, mapping, val_mae)
