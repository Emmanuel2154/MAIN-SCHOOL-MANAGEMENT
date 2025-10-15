import random
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
import json
from sqlalchemy.inspection import inspect
from datetime import datetime
from uuid import uuid4
from utils.fiile_handler import read_file, write_to_file, append_file

class Base(AsyncAttrs, DeclarativeBase):
    pass
class BaseModel:
    __abstract__ = True
    id: Mapped[str] = mapped_column(default=lambda: str(uuid4()), nullable=False, primary_key=True)
    created_at: Mapped[str] = mapped_column(nullable=True, default=datetime.now())
    updated_at: Mapped[str] = mapped_column(nullable=True, default=datetime.now())
    # # def __init__(self, *args, **kwargs) -> None:
    #     self.id = f"{self.__class__.__name__[0]}: {uuid4()}"
    #     self.created_at = datetime.now()
    #     self.updated_at = datetime.now()
    #     # print(self)
    #     for key, value in kwargs.items():
    #         setattr(self, key, value)

    def to_dict(self):
        data = dict(self.__dict__)
        data.pop("_sa_instance_state", None)
        return data
    
    def save_to_json(self, filename="database.json"):
        """Read existing data"""
        data = read_file(filename)
        object_type = self.__class__.__name__.lower()
        data = append_file(data, object_type, self.to_dict())
        write_to_file(filename, data)


    @classmethod
    def fetch_data(cls, object_type= None, key= None, value= None, object_id=None, filename="database.json"):
        """function to search the database"""
        data = read_file()
        """Searching the database"""
        if not object_type:
            return data
        
        objects = data.get(object_type, [])

        if key is None and value is None:
            return objects
        if key and not value:
            results = []
            for items in objects:
                if key in items:
                    results.append(items.get(key))
            return results
        if key and value:
            for items in objects:
                if items.get(key) == value:
                    return items
                    
    def update_obj(self, filename="database.json"):
        data = read_file(filename)
        
        object_types = self.__class__.__name__.lower()
        objects = data.get(object_types, [])

        for object_type in objects:
            if object_type["id"] == "s430":
                object_type["student_name"] = "Emmanuel"
        write_to_file(filename, data)
            
