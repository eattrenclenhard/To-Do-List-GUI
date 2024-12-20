import time
import modules.functions as ft
import PySimpleGUI as sg
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as f:
        pass

sg.theme("LightGreen5")

clock = sg.Text('', key='clock')
label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter todo', key='todo_input')  # no argument required
# add_button = sg.Button(size=2, image_source='images/add.png', mouseover_colors='Green', tooltip='Add Todo',
#                        key='Add')
add_button = sg.Button('Add', tooltip='Add a new task')  # event takes either button_text label as value
list_box = sg.Listbox(values=ft.get_todos(), key='todo_item',
                      enable_events=True, size=(45, 10))  # notice the logging of event at each item click
edit_button = sg.Button('Edit', tooltip='Select a task and then press to edit')
complete_button = sg.Button('Complete',tooltip='Select a completed task and then press to remove')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[
                       [clock],
                       [label], [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]
                   ],
                   # python recommends 79 char max per line
                   font=('Helvetica', 20)
                   )  # title of the window
# window = sg.Window('My To-Do App', layout=[[label], [input_box]])  # title of the window
# each nested list in the layout argument represents a row

while True:
    event, values = window.read(timeout=200)  # will stay at this line so long the window stays open
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = ft.get_todos()
            todos.append(values['todo_input'] + '\n')
            # the backslash n is necessary to ensure new item starts on a new line
            ft.write_todos(todos)
            window['todo_item'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todo_item'][0]
                new_todo = values['todo_input']
                todos = ft.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                ft.write_todos(todos_param=todos)
                # refreshes the list in-place
                window['todo_item'].update(values=todos)
            except IndexError as e:
                sg.popup('Please select an item first.', font=('Helvetica', 20))
        case 'Complete':
            try:
                todos = ft.get_todos()
                todos.remove(values['todo_item'][0])
                ft.write_todos(todos_param=todos)
                window['todo_item'].update(values=todos)
                window['todo_input'].update(value='')
            except IndexError as e:
                sg.popup('Please select an item first.', font=('Helvetica', 20))
        case 'Exit':
            print('Tq for choosing us! Shutting down...')
            break
        case sg.WIN_CLOSED:
            print('Tq for choosing us! Shutting down...')
            break  # break would only exit while loop, exit() would stop the program completely
        case 'todo_item':
            # capture the event, then reflects clicked item in list box
            # onto input box in real time
            # each click of to-do item is considered one todo_item event
            # this is implemented so that input box becomes dynamic in nature. It would now display whichever todo item the user selects
            try:
                window['todo_input'].update(value=values['todo_item'][0])
            except IndexError as e:
                sg.popup("There's nothing in the task list yet, please add at least one.")

window.close()
