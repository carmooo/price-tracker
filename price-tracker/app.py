from fastapi import FastAPI, HTTPException
from .scraper import scrape_product_price

app = FastAPI()


@app.get("/products/{product_id}/price")
def get_product_price(product_id: str):
    price = scrape_product_price(product_id)
    if price is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"price": price}
