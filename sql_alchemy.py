# from myalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base, sessionmaker
# from models.student import Student as Student


# Base = declarative_base()
# engine = create_engine("sqlite:///mysqlalchemy.db", echo=True)

# # with engine.connect() as conn:
# #     print("Connected to database!")

# class Student(Base):
#     __tablename__ = "students"
#     id = Column(String, primary_key=True)
#     student_name = Column(String)
#     student_gender = Column(String)
#     student_address = Column(String)
#     student_role = Column(String)
#     student_age = Column(Integer, nullable=True)

# class Employee(Base):
#     __tablename__ = "employees"
#     id = Column(String, primary_key=True)
#     employee_name = Column(String)
#     employee_gender = Column(String)
#     employee_contact_information = Column(Integer)
#     employee_address = Column(String)
#     employee_role = Column(String)
    

# Base.metadata.create_all(engine)
    
# def add_student_to_database(student_dict):
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     student_obj = Student(**student_dict)
#     session.add(student_obj)
#     session.commit()
#     print("Student has been saved to database!!")

# def add_empployee_to_database(employee_dict):
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     employee_obj = Employee(**employee_dict)
#     session.add(employee_obj)
#     session.commit()
#     print("Employee has been saved to database!!")
