import json
def read_file(filename):
    """Function to read a file"""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        write_to_file(filename, {"student": [], "teacher": []})


def write_to_file(filename, data):
    """Function to write to a file"""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent = 4)
            print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error writing file: {e}")


def append_file(data, object_type, new_item):
    """Function to append to a file"""
    if object_type in data:
        data[object_type].append(new_item)
        # print(new_item)
    return data


