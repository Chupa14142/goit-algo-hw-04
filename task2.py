"""Module 4/Task 2"""

from file_helper import read_file

def get_cats_info(path):
    """Parse file and return cat info in a format [{}]"""
    data_from_file = read_file(path)
    cats_info = []
   
    for cat in data_from_file:
        id, name, age = cat.split(",")

        # Create dict with cat info and get rid off \n in age
        cat_info = {
            "id": id,
            "name": name,
            "age": age.replace('\n', '')
        }
        # Add dict=cat_info in list=cats_info
        cats_info.append(cat_info)
    
    return cats_info


if __name__ == "__main__":
    FILE_PATH = "data_for_dz/task2.txt"

    cats_info = get_cats_info(FILE_PATH)
    print(cats_info)

