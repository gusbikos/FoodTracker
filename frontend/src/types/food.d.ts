// Internal app types
export interface FoodNutrient {
    name: string;
    value: number;
}

export interface FoodItem {
    fdcId: number;
    description: string;
    foodNutrients: FoodNutrient[];
}

// Raw API response types
export interface RawFoodNutrient {
    nutrientName: string;
    value: number | null;
}

export interface RawFoodItem {
    fdcId: number;
    description: string;
    foodNutrients: RawFoodNutrient[];
}
