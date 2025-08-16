from models.employee import Employee
from schemas.employee_schema import CreateEmployeeSchema
# from db_sql import teacher_to_db
from sql_alchemy import add_empployee_to_database

def create_new_employee(employee_dict: dict) -> Employee:
    """Create Student"""
    data = CreateEmployeeSchema(**employee_dict)
    data_dict = data.model_dump()
 
    employee = Employee(**data_dict)
    # call the method that saves it to the file
    # print(employee)
    employee.save_to_json()
    return employee

def add_employee_to_db(employee_dict: dict) -> Employee:
    """Create Employee"""
    data = CreateEmployeeSchema(**employee_dict)
    data_dict = data.model_dump()
    employee = Employee(**data_dict)
    add_empployee_to_database(employee.to_dict())
    return employee