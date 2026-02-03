import { useContext } from "react"
import { FoodLogContext } from "../context/FoodLogContext"

export function useFoodLog() {
    const context = useContext(FoodLogContext)
    if (!context) {
        throw new Error("useFoodLog must be used within a FoodLogProvider")
    }
    return context
}