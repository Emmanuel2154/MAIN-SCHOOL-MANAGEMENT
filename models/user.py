from models.basemodel import BaseModel, Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from typing import List, Optional
from random import randint


class User(BaseModel, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column()
    is_email_verfied: Mapped[bool] = mapped_column(default=False)
    reset_token: Mapped[str] = mapped_column(default=False, nullable=True)
    role: Mapped[str] = mapped_column()


    student: Mapped[Optional["Student"]] = relationship(back_populates="user", uselist=False)
    employee: Mapped[Optional["Employee"]] = relationship(back_populates="user", uselist=False)
    admin: Mapped[Optional["Admin"]] = relationship(back_populates="user", uselist=False)
    