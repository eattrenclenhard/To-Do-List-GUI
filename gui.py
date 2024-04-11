import modules.functions as ft
import PySimpleGUI as sg

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter todo', key='todo_input')  # no argument required
add_button = sg.Button("Add")
list_box = sg.Listbox(values=ft.get_todos(), key='todo_item',
                      enable_events=True, size=(45, 10))  # notice the logging of event at each item click
edit_button = sg.Button('Edit')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   # python recommends 79 char max per line
                   font=('Helvetica', 20)
                   )  # title of the window
# window = sg.Window('My To-Do App', layout=[[label], [input_box]])  # title of the window
# each nested list in the layout argument represents a row

while True:
    event, values = window.read()  # will stay at this line so long as the window stays open
    print('event:', event)
    print('values:', values)
    print("values['todo_item']:", values['todo_item'])
    match event:
        case 'Add':
            todos = ft.get_todos()
            todos.append(values['todo_input'] + '\n')
            # the backslash n is necessary to ensure new item starts on a new line
            ft.write_todos(todos)
            window['todo_item'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todo_item'][0]
            new_todo = values['todo_input']
            todos = ft.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            ft.write_todos(todos_param=todos)
            # refreshes the list in-place
            window['todo_item'].update(values=todos)
        case sg.WIN_CLOSED:
            print('Tq for choosing us! Shutting down...')
            break  # alternatively, exit() would stop the program completely
        case 'todo_item':
            # capture the event, then reflects clicked item in list box
            # onto input box in real time
            # each click of to-do item is considered one todo_item event
            # this is implemented so that input box becomes dynamic in nature. It would now display whichever todo item the user selects
            window['todo_input'].update(value=values['todo_item'][0])

window.close()
