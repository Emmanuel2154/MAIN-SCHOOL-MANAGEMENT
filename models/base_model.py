import json
class BaseModel:            
    def __init__(self, *args, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return self.__dict__

        
    def save_to_json(self, filename='database.json'):
        data = []
    # Reading existing data
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f'Error reading file: {e}')

        # Append current object
        data.append(self.to_dict())

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
