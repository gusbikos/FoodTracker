# Search foods data via API
# The controller layer — receives requests and sends responses.
from app.config import FOOD_DATA_CENTRAL_API_KEY
import requests
from requests.auth import HTTPBasicAuth

# Variables for Open food facts API usage
OPEN_FOOD_FACTS_BASE_URL = "https://world.openfoodfacts.net/api/v2"
open_food_facts_username = "off"
open_food_facts_password = "off"
open_food_facts_basic_auth = HTTPBasicAuth(open_food_facts_username, open_food_facts_password)

# Variables for Food data central API usage
FOOD_DATA_CENTRAL_BASE_URL = "https://api.nal.usda.gov/fdc/v1/"
food_data_central_username = f"{FOOD_DATA_CENTRAL_API_KEY}"
food_data_central_password = ""
food_data_central_basic_auth = HTTPBasicAuth(food_data_central_username, food_data_central_password)


# This function is used with Open food facts to retrieve foods by barcode.
def get_food_product_barcode(code):
    endpoint = f"/product/{code}"
    response = requests.get(
        f"{OPEN_FOOD_FACTS_BASE_URL}{endpoint}",
        auth=open_food_facts_basic_auth
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

# This function is used with Food data central API to search a list of foods based of query parameter.
def search_foods(query):
    endpoint = "/foods/search"
    params = {
        "query": query,
        "pageSize": 10,
        "dataType": ["Foundation"],
        "sortBy": "dataType.keyword",
    }
    response = requests.get(
        f"{FOOD_DATA_CENTRAL_BASE_URL}{endpoint}",
        params=params,
        auth=food_data_central_basic_auth
    )
    
    if response.status_code != 200:
        return {
            "error": f"Request failed with status {response.status_code}"
        }
        
    data = response.json()
    foods = data.get("foods", [])
    
    # Process each food to extract only fdcId, description, and nutrients
    result = []
    for food in foods:
        simplified_nutrients = []
        for nutrient in food.get("foodNutrients", []):
            simplified_nutrients.append({
            "name": nutrient.get("nutrientName"),
            "value": nutrient.get("value")
        })
        
        food_data = {
            "fdcId": food.get("fdcId"),
            "description": food.get("description"),
            "foodNutrients": simplified_nutrients
        }
        result.append(food_data)
    return result

