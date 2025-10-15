from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes.student_routes import student_router
from api.v1.routes.admin_routes  import admin_router
from api.v1.routes.employee_routes import employee_router
from api.v1.routes.user_routes import user_router
from api.v1.routes.course_routes import course_router
from api.v1.routes.auth_routes import auth_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods=['*'],
    allow_headers=["*"]
)

app.get("/hello")
def status():
    return {"status": "We are good to go..."}

app.include_router(user_router)
app.include_router(student_router)
app.include_router(employee_router)
app.include_router(admin_router, prefix="/api/v1/admins", tags=["Admins"])
app.include_router(course_router)
app.include_router(auth_router)










