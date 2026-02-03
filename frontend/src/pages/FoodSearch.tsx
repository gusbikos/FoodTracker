import { useState } from "react"
import { searchFoods } from "../api/foodApi"
import FoodCard from "../components/Foodcard"
import type { FoodItem } from "../types/food"

const FoodSearch = () => {
    const [query, setQuery] = useState("")
    const [foods, setFoods] = useState<FoodItem[]>([])
    const [loading, setLoading] = useState(false)

    const handleSearch = async () => {
        setLoading(true)
        try {
            const data = await searchFoods(query)
            setFoods(data)
        } catch (err) {
            console.error(err)
            setFoods([])
        } finally {
            setLoading(false)
        }
    }

    return (
        <div>
            <h1>Food Search</h1>
            <input 
                type="text"
                value={query}
                placeholder="Enter a food name"
                onChange={(e) => setQuery(e.target.value)}
            />
            <button onClick={handleSearch}>Search</button>

            {loading && <p>Loading...</p>}

            <div>
                {foods.map((food) => (
                    <FoodCard key={food.fdcId} food={food} />
                ))}
            </div>
        </div>
    )
}

export default FoodSearch