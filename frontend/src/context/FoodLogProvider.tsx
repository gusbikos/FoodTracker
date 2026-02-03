import { useState, type ReactNode } from "react"
import type { FoodItem } from "../types/food"
import { FoodLogContext } from "./FoodLogContext"

export const FoodLogProvider = ({ children }: {children: ReactNode }) => {
    const [log, setLog] = useState<FoodItem[]>([])

    const addFood = (food: FoodItem) => setLog(prev => [...prev, food]);

    const removeFood = (fdcId: number) => setLog(prev => prev.filter(f => f.fdcId !== fdcId));

    return (
    <FoodLogContext.Provider value={{ log, addFood, removeFood }}>
        {children}
    </FoodLogContext.Provider>
    )
}