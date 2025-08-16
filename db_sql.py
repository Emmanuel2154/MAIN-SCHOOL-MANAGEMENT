import sqlite3
from data import student, employee

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student(
    id TEXT PRIMARY KEY,
    student_name TEXT,
    student_gender TEXT,
    student_address TEXT,
    student_role TEXT
)'''
)
cursor.execute('''
CREATE TABLE IF NOT EXISTS teacher(
    id TEXT PRIMARY KEY,
    teacher_name TEXT,
    teacher_gender TEXT,
    teacher_contact_information TEXT,
    teacher_role TEXT,
    subject_teacher TEXT
)
'''
)
def student_to_db(student_dict):
    cursor.execute('''
        INSERT INTO student (id, student_name, student_gender, student_address, student_role)
        VALUES (:id, :student_name, :student_gender, :student_address, :student_role)
    ''', student_dict
    )
    connection.commit()

def teacher_to_db(teacher_dict):
    cursor.execute('''
        INSERT INTO employee (id, t_name, teacher_gender, teacher_contact_information, teacher_role, subject_teacher)
        VALUES (:id, :teacher_name, :teacher_gender, :teacher_contact_information, :teacher_role, :subject_teacher)
    ''', teacher_dict
    )
    connection.commit()
# def create_table_from_dict(table_name, data: dict, db_name="database.db"):
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
    
#     columns = [f"{key} TEXT" for key in data]
#     columns_str = ", ".join(columns)

#     sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()
# connection.commit()
# print("Saved!!")

