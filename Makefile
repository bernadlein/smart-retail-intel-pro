
.PHONY: setup data train baseline xgb uplift api app monitor lint test

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

data:
	python -m src.data.make_mock_data

baseline:
	python -m src.models.train_baseline

xgb:
	python -m src.models.train_xgb

uplift:
	python -m src.uplift.train_uplift

monitor:
	python -m src.monitoring.data_drift

api:
	uvicorn api.main:app --reload

app:
	streamlit run app/app.py

lint:
	python -m pip install ruff black
	ruff check .
	black --check . || true

test:
	pytest -q
