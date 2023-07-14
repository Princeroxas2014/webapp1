FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
     """
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(todos_arc, filepath=FILEPATH):
    """ Write a to-do item list in the text file """
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arc)


if __name__ == "__main __":
    print("hello from functions")
    print(get_todos())


def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    else:
        return "Gas"
