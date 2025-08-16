import random
import json
from utils.fiile_handler import read_file, write_to_file, append_file
class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        self.id = f"{self.__class__.__name__[0]}:{random.randint(1,3000)}"
        print(kwargs)
        for key, value in kwargs.items():
            
            print(key, value)
            setattr(self, key, value)

    def to_dict(self):
        print(self.__dict__)
        return self.__dict__
    
    def save_to_json(self, filename="database.json"):
        """Read existing data"""
        data = read_file(filename)
        # """Accessing the class and storing in a variable"""
        object_type = self.__class__.__name__.lower()
        # print(object_type)
        data = append_file(data, object_type, self.to_dict())
        
        # print(data)
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
            
