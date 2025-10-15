from models.basemodel import BaseModel, Base
from sqlalchemy import ForeignKey
from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped, relationship

class Admin(BaseModel, Base):
    __tablename__ = "admin"

    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    admin_name: Mapped[str] = mapped_column()

    user = relationship("User", back_populates="admin")

