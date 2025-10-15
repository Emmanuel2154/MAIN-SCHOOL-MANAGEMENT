from pydantic import BaseModel

class CreateCourseSchema(BaseModel):
    course_name: str
    course_code: str
    course_description: str
