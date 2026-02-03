import { useNavigate } from "react-router-dom"
import type { FoodItem } from "../types/food"
import { useFoodLog } from "../hooks/useFoodLog"

interface FoodCardProps {
    food: FoodItem
}

const FoodCard = ({ food }: FoodCardProps) => {
    const navigate = useNavigate()
    const { addFood } = useFoodLog()

    const handleClick = () => {
        addFood(food)
        navigate("/food-log", { state: food })
    }

    return (
        <div className="food-card" onClick={handleClick} style={{ cursor: "pointer" }}>
            <h3>{food.description}</h3>
            <ul>
                {food.foodNutrients.map((nutrient) => (
                    <li key={nutrient.name}>
                        {nutrient.name}: {nutrient.value}
                    </li>
                ))}
            </ul>
        </div>
    )
};

export default FoodCard