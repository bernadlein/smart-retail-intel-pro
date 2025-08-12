
# Data Card — Synthetic Retail

**Sumber**: Generator internal (`src/data/make_mock_data.py`).  
**Lisensi**: Bebas digunakan untuk demo & edukasi.

## Skema
- `sales(date, store_id, product_id, qty, revenue, promo_flag, price)`
- rentang tanggal ~180 hari, 5 store × 10 produk.

## Kualitas & Batasan
- Musiman & promo disimulasikan; tidak ada anomali ekstrem dunia nyata.
- Jangan gunakan untuk estimasi bisnis nyata tanpa validasi lebih lanjut.
