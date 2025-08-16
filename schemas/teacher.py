from pydantic import BaseModel, model_validator
from typing import Literal
class CreateTeacherSchema(BaseModel):
    """Teacher's pydantic attributes"""
    teacher_name: str
    teacher_gender: Literal['male', 'female']
    teacher_contact_information: str
    teacher_address: str | int
    teacher_role: Literal['form teacher', 'subject teacher']
    subject_teacher: Literal['mathematics', 'english', 'basic science', 'hysical health education', 'literature']

    """ To change the values to lower case before validation"""
    @model_validator(mode='before')
    def normalize_case(cls, dict_value):
        for field in ['teacher_gender', 'teacher_role', 'subject_teacher']:
            if field in dict_value and isinstance(dict_value[field], str):
                dict_value[field] = dict_value[field].lower()
        return dict_value        
