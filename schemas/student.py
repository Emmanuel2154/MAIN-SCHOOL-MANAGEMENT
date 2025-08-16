from pydantic import BaseModel, model_validator
from typing import Literal
class CreateStudentSchema(BaseModel):
    """Student's pydantic attributes"""
    student_name: str
    student_gender: Literal['male', 'female']
    student_address: str
    student_role: Literal['headboy', 'headgirl', 'assistant headboy', 'assitant headboy']

    """ To change the values to lower case before validation"""
    @model_validator(mode='before')
    def normalize_case(cls, dict_value):
        for field in ['student_gender', 'student_role']:
            if field in dict_value and isinstance(dict_value[field], str):
                dict_value[field] = dict_value[field].lower()
        return dict_value        
