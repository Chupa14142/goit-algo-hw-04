"""Methods for files(read and write)"""


def read_file(file_path):
    """Open file and read"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError as e:
        return f"Couldn't find file {e}"
    

def write_file(file_path, args: list):
    """Open file and write"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for value in args:
                f.write(value)
    except FileNotFoundError as e:
        return f"File not found exception {e}"


def read_and_write(input, output):
    data_from_file = read_file(input)


    write_file(output, data_from_file)

