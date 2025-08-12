
# Contributing Guide

Terima kasih sudah tertarik berkontribusi! Tujuan repo ini adalah contoh portofolio AI Engineer yang rapi dan mudah direproduksi.

## Cara Mulai
1. Fork repo → buat branch fitur: `feat/nama-fitur`.
2. Setup dev:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   pre-commit install  # optional
   ```
3. Jalankan test lokal: `pytest -q`.
4. Buka PR ke `main` dengan deskripsi yang jelas dan screenshot bila relevan.

## Gaya Commit
Gunakan **Conventional Commits**:
- `feat: ...`, `fix: ...`, `docs: ...`, `test: ...`, `refactor: ...`

## Standar Kode
- PEP8/Black, lint dengan Ruff, dan unit test untuk modul baru.
- Tambahkan docstring singkat pada fungsi publik.

## Isu & Diskusi
Gunakan template **Bug report** atau **Feature request** (lihat `.github/ISSUE_TEMPLATE`). Sertakan langkah reproduksi dan contoh data jika perlu.

## Lisensi
Dengan berkontribusi, Anda setuju bahwa kontribusi dirilis di bawah lisensi MIT repo ini.
