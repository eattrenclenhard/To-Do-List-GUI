FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """read a text file and return a list of
    to-do items.
    """
    with open(filepath) as f:
        todos_local = f.readlines()
    return todos_local


def write_todos(todos_param, filepath=FILEPATH):
    with open(filepath, 'w') as f:
        f.writelines(todos_param)


if __name__ == "modules.functions":
    print('get todos imported')
    print('write todos imported')

if __name__ == '__main__':
    print(__name__)

# think of modules as a collection of functions
