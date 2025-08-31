from typing import List, Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    title: str
    category: Optional[str] = None
    width_cm: Optional[float] = None
    depth_cm: Optional[float] = None
    height_cm: Optional[float] = None
    price_gbp: Optional[float] = None
    currency: Optional[str] = "GBP"
    store_name: Optional[str] = None
    source_url: Optional[str] = None


class ProductList(BaseModel):
    items: List[Product]
    count: int
