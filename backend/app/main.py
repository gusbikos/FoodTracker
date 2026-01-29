"""_summary_
- FastAPI entry point
- The entry point of your backend application.

Responsibilities:
- Create the FastAPI app
- Register all API routes
- Configure middleware (CORS, logging, etc.)
- Start the backend server
"""

from typing import Union

from fastapi import FastAPI, HTTPException
from app.api.foods import get_food_product_barcode, search_foods

app = FastAPI()

@app.get("/product/{code}")
def get_products_barcode(code):
    data = get_food_product_barcode(code)
    if not data:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return data

@app.get("/foods/search")
def get_food_item(query):
    foods_list = search_foods(query)
    if not foods_list:
        raise HTTPException(
            status_code=404,
            detail="Foods not found"
        )
    return foods_list

