from pydantic import BaseModel, model_validator
from typing import Literal

class CreateEmployeeSchema(BaseModel):
    """Teacher's pydantic attributes"""
    employee_name: str
    employee_gender: Literal['male', 'female']
    employee_contact_information: str
    employee_address: str | int
    employee_role: Literal['principal', 'form teacher', 'subject teacher']
    # subject_teacher: Literal['mathematics', 'english', 'basic science', 'hysical health education', 'literature']

   
    @model_validator(mode='before')
    def normalize_case(cls, dict_value):
        """ To change the values to lower case before validation"""
        for field in ['employee_gender', 'employee_role']:
            if field in dict_value and isinstance(dict_value[field], str):
                dict_value[field] = dict_value[field].lower()
        return dict_value