from services.student_services import add_student_to_db
from services.employee_services import add_employee_to_db, create_new_employee
from models.student import Student
from utils.fiile_handler import append_file
from data import student as student_obj
from data import employee as employee_obj
from pprint import pprint
def main():    
    try:
        # student = add_student_to_db(student_obj)
        student = Student(**student_obj)
        # print(student)
        student.to_dict()
        student.save_to_json()



        # employee = add_employee_to_db(employee_obj)
    except ValueError as e:
        print(e)

main()