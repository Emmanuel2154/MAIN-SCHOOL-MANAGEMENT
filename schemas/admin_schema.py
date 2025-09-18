from pydantic import BaseModel, EmailStr, model_validator


class CreateAdminSchema(BaseModel):
    admin_name : str
    admin_email : str
    admin_username: str
    

    # @model_validator(mode="before")
    # def check_email(cls, admin_email):
    #     if not isinstance(admin_email, EmailStr):
    #         raise ValueError ("Kindly follow the email format 'email@gmail.com'")