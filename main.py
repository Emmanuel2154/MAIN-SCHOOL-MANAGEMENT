from services.studentservices import create_new_student, add_student_to_db
from models.base_model import BaseModel
from data import student as student_obj
from services.teacherservices import create_new_teacher
from data import teacher as teacher_obj
from pprint import pprint
from db_sql import create_table_from_dict
def main():
    # student = create_new_student(student_obj)
    # print(student)
   
    base = BaseModel()
    
    try:
        # retrived_data = base.fetch_data(object_type="student", key="id", value="123" )            
        # x = base.access_single_obj(object_id="S: 4993", array=retrived_data)
        # pprint(retrived_data)
        student = add_student_to_db(student_obj)
        print(student)
    except ValueError as e:
        print(e)
    
    

    
    # teacher = create_new_teacher(teacher_obj)
    #teacher.save_to_json()

main()