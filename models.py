from pydantic import BaseModel

#Model use to get input data
class TdeeInputRequest(BaseModel):
    weight: float
    height: float
    age: int
    gender: str
    units:str
    activityLevel: str

#gender can be either male or female
#units can be either metric or imperial
#activity level can sedentary, light, moderate, active or very active

#Model use to get response data

class TdeeResponseRequest(BaseModel):
    bmr: float
    tdee: float
    units: str
    message: str = "Your TDEE has been calculated"