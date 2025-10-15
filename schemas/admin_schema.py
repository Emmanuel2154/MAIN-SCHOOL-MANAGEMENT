from pydantic import BaseModel, EmailStr, model_validator


class CreateAdminSchema(BaseModel):
    admin_name : str