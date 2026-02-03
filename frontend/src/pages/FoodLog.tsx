// import { useLocation } from "react-router-dom"
// import type { FoodItem } from "../types/food"
import { useFoodLog } from "../hooks/useFoodLog"

const FoodLog = () => {
    const { log, removeFood } = useFoodLog()

    if (log.length == 0) return <p>No foods added yet.</p>
    
    return (
        <div>
            <h1>Food Log</h1>
            {log.map((food) => (
                <div key={food.fdcId} className="food-card">
                    <h3>{food.description}</h3>
                    <ul>
                        {food.foodNutrients.map((nutrient) => (
                            <li key={nutrient.name}>
                                {nutrient.name}: {nutrient.value}
                            </li>
                        ))}
                    </ul>
                    <button onClick={() => removeFood(food.fdcId)}>Remove</button>
                </div>
            ))}
        </div>
    )

}

export default FoodLog