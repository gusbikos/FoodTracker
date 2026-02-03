import type { FoodItem, FoodNutrient, RawFoodItem, RawFoodNutrient } from "../types/food";

export async function searchFoods(query: string): Promise<FoodItem[]> {
    const res = await fetch(`http://localhost:8000/foods/search?query=${query}`);
    if (!res.ok) throw new Error("Failed to fetch foods");

    const data: RawFoodItem[] = await res.json();

  // Map raw API response to app's FoodItem type
    return data.map((food: RawFoodItem): FoodItem => ({
        fdcId: food.fdcId,
        description: food.description,
        foodNutrients: (food.foodNutrients || []).map(
            (nutrient: RawFoodNutrient): FoodNutrient => ({
                name: nutrient.nutrientName,
                value: nutrient.value ?? 0,
            })
        ),
    }));
}

