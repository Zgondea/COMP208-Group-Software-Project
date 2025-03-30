
def tdeeCalculation(bmr, activityLevel):
    
    activity_level = activity_level.strip().lower().replace(" ", "_")

    activityMultipliers ={
        "sedentary": 1.2,
        "light":1.37,
        "moderate": 1.55,
        "active": 1.72,
        "very active": 1.9
    }

    multiplier = activityMultipliers.get(activityMultipliers.lower())
    if not multiplier:
        raise ValueError("Invalid activity level selected. Choose from: sedentary, light, moderate, active, very active ")
    
    return round(bmr, multiplier, 2)

