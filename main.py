from fastapi import FastAPI
from models import TdeeInputRequest, TdeeResponse
from BMRCalculator import bmr_calculator, kg_to_pounds_conversion, cm_to_inches_conversion
from TDEECalculator import tdeeCalculation
from models import Food, Meal
from mealPlannerFunctions import addFoodToMeal, addNewMeal, getMealSum


app = FastAPI()

@app.post("/tdeeCalculation", response_model=TdeeResponse)
def getUserTdee(data: TdeeInputRequest):
    # Convert units if needed
    if data.units.lower() == "metric":
        weightLbs = kg_to_pounds_conversion(data.weight)
        heightInch = cm_to_inches_conversion(data.height)
    else:
        weightLbs = data.weight
        heightInch = data.height

    # Calculate BMR & TDEE
    try:
        bmr = bmr_calculator(weightLbs, heightInch, data.age, data.gender)
        tdee = tdeeCalculation(bmr, data.activityLevel)
    except ValueError as e:
        return {"error": str(e)}

    return TdeeResponse(
        bmr=round(bmr, 2),
        tdee=round(tdee, 2),
        units="calories/day"
    )


#Meal Planing
@app.post("/meals/{meal_name}/add")
def add_food(meal_name, food: Food):
    return {"message": addFoodToMeal(meal_name, food)}

@app.post("/meals/add")
def add_meal(meal: Meal):
    return {"message": addNewMeal(meal.name)}

@app.get("/meals/summary")
def meal_summary():
    return getMealSum()




