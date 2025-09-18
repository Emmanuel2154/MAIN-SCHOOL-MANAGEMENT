from fastapi import FastAPI
from api.v1.student_routes import student_router
from api.v1.admin_routes import admin_router
from api.v1.employee_routes import employee_router

app = FastAPI()

app.include_router(student_router, prefix="/api/v1/students", tags=["Students"])

app.include_router(employee_router, prefix="/api/v1/employees", tags=["Employees"])

app.include_router(admin_router, prefix="/api/v1/admins", tags=["Admins"])