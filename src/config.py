from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = ROOT / "data" / "raw" / "retail_sales.csv"
PROCESSED_DATA = ROOT / "data" / "processed" / "retail_sales_enriched.csv"
OUTPUT_TABLES = ROOT / "outputs" / "tables"
OUTPUT_CHARTS = ROOT / "outputs" / "charts"

OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
OUTPUT_CHARTS.mkdir(parents=True, exist_ok=True)
