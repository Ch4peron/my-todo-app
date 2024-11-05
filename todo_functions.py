FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        to_dos_local = file_local.readlines()  # .readlines() creates a list -> no to_dos = [] necessary
    return to_dos_local


def write_todos(to_dos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(to_dos_arg)


if __name__ == "__main__":  # wird ausgeführt, wenn todo_functions direkt ausgeführt wird und nicht über das main file
    print("Hello")
    print(get_todos())