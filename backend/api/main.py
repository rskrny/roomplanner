from fastapi import FastAPI
import pandas as pd
from pathlib import Path

from .schemas import Product, ProductList

app = FastAPI(title="RoomPlanner API")

# Path to the sample catalog CSV (../data/catalog_sample.csv)
DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "catalog_sample.csv"

# Load the catalog once at startup if the file exists
if DATA_PATH.exists():
    catalog_df = pd.read_csv(DATA_PATH)
else:
    catalog_df = pd.DataFrame()


def get_catalog() -> pd.DataFrame:
    """Return a copy of the catalog DataFrame."""
    return catalog_df.copy()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/products", response_model=ProductList)
def list_products(limit: int = 50, offset: int = 0):
    """Return a paginated list of products from the catalog."""
    df = get_catalog()
    items = df.iloc[offset:offset + limit].to_dict(orient="records")
    return {"items": items, "count": len(df)}


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    """Return a single product by its ID."""
    df = get_catalog()
    match = df[df["id"] == product_id]
    if not match.empty:
        return match.to_dict(orient="records")[0]
    return {"error": "Product not found"}
