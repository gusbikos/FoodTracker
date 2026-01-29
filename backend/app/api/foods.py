# Search foods data via API
# The controller layer — receives requests and sends responses.
from app.config import FOOD_FACTS_API_KEY
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "https://world.openfoodfacts.net/api/v2"
username = "off"
password = "off"
basic_auth = HTTPBasicAuth(username, password)

def get_food_product_barcode(code):
    endpoint = f"/product/{code}"
    response = requests.get(
        f"{BASE_URL}{endpoint}",
        auth=basic_auth
    )
    
    if response.status_code != 200:
        return {
            "error": f"Request failed with status {response.status_code}"
        }
    data = response.json()

    if "product" not in data:
        return {
            "error: Product not found"
        }
    product = data["product"]
    
    images = product.get("images", {})
    full_images = []
    for image_id, image_data in images.items():
        full = image_data.get("sizes", {}).get("full")

        if full:
            full_images.append({
                "id": image_id,
                "height": full.get("h"),
                "width": full.get("w")
            })
    
    result = {
        "keywords": product.get("_keywords", []),
        "product_name": product.get("product_name_en"),
        "serving_size": product.get("serving_size"),
        "nutriments": product.get("nutriments", {}),
        "images": full_images
    }
    return result




# def get_food_product_barcode(code):
#     endpoint = f"/product/{code}"
    
#     response = requests.get(
#         f"{BASE_URL}{endpoint}",
#         auth=basic_auth
#     )


#     data = response.json()

#     return data

