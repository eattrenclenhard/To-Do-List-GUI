import modules.functions
from modules.functions import get_todos, write_todos
import time

manual_file = None

now = time.strftime('%d %b,%Y(%a) %H:%M:%S')
print('It is currently', now)

while True:
    user_prompt = 'Type add, show, edit, complete, or exit: '
    user_action = input(user_prompt).strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todo = todo.lstrip()

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif 'show' in user_action or 'display' in user_action:
        try:
            todos = get_todos()
        except FileNotFoundError as e:
            print(e)
            manual_file = (input('Would you like to create a new todos.txt file'
                                 ' under the same directory? (press y to create)')
                           .strip().lower())
            if manual_file == 'y':
                with open('todos.txt', 'w') as f:
                    pass
            continue

        if todos:
            for index, item in enumerate(todos):
                item = item.strip().title()
                print(f"{index + 1}-{item}")
        else:
            print('Todo list is currently empty.')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[
                         5:])
            todos = get_todos()
            print(f'Replacing {number}-{todos[number]}...')
            number -= 1
            todos[number] = input('Enter a new todo to replace with: ').strip() + '\n'
        except ValueError as e:
            print(e)
            print('Gimme a number and nothing else! Fool!')
            continue
        except IndexError:
            print("OUT OF RANGE! FOOL!")
            continue

        write_todos(todos)

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            with open('todos.txt', 'r') as f:
                todos = f.readlines()
            number -= 1
            removed_todo = todos.pop(number).strip()
            print(f'"{removed_todo}" has been successfully removed from the list.')
        except ValueError as e:
            print(e)
            print('Gimme a number and nothing else! Fool!')
            continue
        except IndexError as e:
            print("OUT OF RANGE YOU FOOL!")
            continue

        write_todos(todos)

    elif user_action.startswith('exit'):
        break
    else:
        print('Command invalid! Don\'t mess with me, you fool!')

print('Thank you for choosing us, have a nice day!')
