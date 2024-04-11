import modules.functions as ft
import PySimpleGUI as sg

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter todo')  # no argument required
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   # python recommends 79 char max per line
                   font=('Helvetica', 20)
                   )  # title of the window
# window = sg.Window('My To-Do App', layout=[[label, input_box]])  # title of the window
# each nested list in the layout argument represents a row

while True:
    event, values = window.read()  # will stay at this line so long as the window stays open
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = ft.get_todos()
            todos.append(values['add_todo'] + '\n')
            # the backslash n is necessary to ensure new item starts on a new line
            ft.write_todos(todos)
        case sg.WIN_CLOSED:
            print('Tq for choosing us! Shutting down...')
            break

window.close()
