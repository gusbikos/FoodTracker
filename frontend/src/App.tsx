import { Routes, Route } from 'react-router-dom'
import FoodSearch from './pages/FoodSearch'
import FoodLog from './pages/FoodLog'

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<FoodSearch />} />
      <Route path="/food-log" element={<FoodLog />} />
    </Routes>
  )
}

export default App
