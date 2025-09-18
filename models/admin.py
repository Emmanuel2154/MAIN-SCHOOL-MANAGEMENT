from models.basemodel import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import mapped_column, Mapped
class Admin(Base, BaseModel):
    __tablename__ = "admin"
    admin_name: Mapped[str] = mapped_column()
    admin_email: Mapped[str] = mapped_column()
