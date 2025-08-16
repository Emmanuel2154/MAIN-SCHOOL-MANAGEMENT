import json
import random
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        self.id = f"{self.__class__.__name__[0]}: {random.randint(1,6000)}"
        # self.created_at = datetime.now()
        # self.updated_at = datetime.now()
        for key, value in kwargs.items():
            setattr(self, key, value)


    def to_dict(self):
         return self.__dict__


    def save_to_json(self, filename='database.json'):
        data = {"student": [], "teacher": []}
    # Reading existing data
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f'Error reading file: {e}')

        # Accessing the class, storing in a variable and checking if the stored class is in data before appending
        object_type = self.__class__.__name__.lower()

        if object_type in data:
            data[object_type].append(self.to_dict())
        # Save updated list back to file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Saved to {filename}")
  
    @classmethod
    def fetch_data(cls ,object_type= None, key= None, value= None, object_id=None, filename= 'database.json'):
        """function to search the database"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
        except Exception as e:
            print(f'Error loading file: {e}')

        """Getting the whole database"""
        if not object_type:
            return data
        
        objects = data.get(object_type, [])

        if object_id:
            return cls.access_single_obj(array=objects, object_id=object_id)

        if key is None and value is None:
            return objects

        """Getting data from just keys"""
        if key and not value:
            results = []
            for items in objects:
                if key in items:
                    results.append(items.get(key))
            return results
        
        if key and value:
            """Getting data by keys and values"""
            for items in objects:
                if items.get(key) == value:
                    return items
        

    # function to update an object
    def update_obj(self, filename='database.json'):
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"Error reading file: {e}")
        object_types = self.__class__.__name__.lower()
        
        objects = data.get(object_types, [])

        for object_type in objects:
            if object_type["id"] == 's430':
                object_type['student_name'] = "Emeka"

        with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        print(f"Saved to {filename}")
    
    def delete_item(self, object_type, key, value, filename='database.json'):
        try:
             with open(filename, 'r') as f:
                data = json.load(f)
        except Exception as e:
                print(f'Error reading file{e}')
        if object_type not in data:
            raise ValueError(f'{object_type} not found in data.')
        new_data = []
        for item in data[object_type]:
            if item.get(key) != value:
                new_data.append(item)
        data[object_type] = new_data

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f'Error writing file{e}')

                
    
    @classmethod
    def access_single_obj(cls, array: list = [], object_id: str=""):
        if not array or not isinstance(array, list):
            raise ValueError('Kindly pass an array')
        
        if not isinstance(object_id, str):
            raise ValueError('Kindly pass a string')

        for item in array:
            # if item.get("id") == object_id:
            if item['id'] == object_id:
                return item
            
        return f"[id: {object_id}] not found in the list"
    





