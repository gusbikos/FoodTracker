import { createContext } from "react"
import type { FoodItem } from "../types/food"

interface FoodLogContextType {
    log: FoodItem[]
    addFood: (food: FoodItem) => void
    removeFood: (fdcId: number) => void
}

export const FoodLogContext = createContext<FoodLogContextType | undefined>(undefined)



