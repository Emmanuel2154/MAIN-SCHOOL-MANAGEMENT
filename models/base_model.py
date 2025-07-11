import json
class BaseModel:            
    def __init__(self, *args, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return self.__dict__

        
    def save_to_json(self, filename='database.json'):
        data = {"students": [], "teachers": []}
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






    
    # @classmethod
    # def from_json(cls, filename= 'database.json'):
    #     try:
    #         with open(filename, 'r') as json_file:
    #             data = json.load(json_file)
    #         return cls(**data)
    #     except Exception as e:
    #         print(f"Error reading file: {e}")
