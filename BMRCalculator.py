'''
!!BMR FORMULAS!!
Male: 4.38 x weight in pounds + 14.55 x height in inches - 5.08 x age in years + 260
Female: 3.35 x weight in pounds + 15.42 x height in inches - 2.31 x age in years + 43

'''

def kg_to_pounds_conversion(kg):
    return kg * 2.20462

def cm_to_inches_conversion(cm):
    return cm * 0.39

def bmr_calculator(weight_lbs, height_inch, age, gender):
    gender = gender.lower()
    if gender == "male":
        return (4.38 * weight_lbs) + (14.55 * height_inch) - (5.08 * age) + 260
    elif gender == "female":
        return (3.35 * weight_lbs) + (15.42 * height_inch) - (2.31 * age) + 43
    else:
        raise ValueError("Gender is invalid! Please use either 'male' or 'female'.")
