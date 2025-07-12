import json
import random
class BaseModel:            
    def __init__(self, *args, **kwargs) -> None:
        self.id = kwargs.get("id", f"{self.__class__.__name__[0].lower()}{random.randint(100, 900)}")
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
