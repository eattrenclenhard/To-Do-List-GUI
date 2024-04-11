import modules.functions as ft
import PySimpleGUI as sg

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter todo')  # no argument required
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]]
                   )  # title of the window
# window = sg.Window('My To-Do App', layout=[[label], [input_box]])  # title of the window
# each nested list in the layout argument represents a row

window.read()  # will stay at this line so long as the window stays open
print('hello')
window.close()
