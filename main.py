from services.studentservices import create_new_student
from data import student as student_obj
from services.teacherservices import create_new_teacher
from data import teacher as teacher_obj
def main():
    student = create_new_student(student_obj)
    student.save_to_json()

    student.update_obj()


    teacher = create_new_teacher(teacher_obj)
    teacher.save_to_json()

main()