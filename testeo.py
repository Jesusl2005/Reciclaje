import PySimpleGUI as sg

layout = [
    [sg.Text("Etiqueta 1"), sg.Input()],
    [sg.Text("Etiqueta 2"), sg.Input()],
    [sg.Button("Boton 1", key='boton'), sg.Button("Boton 2")]
]

window = sg.Window("Centrar botones en PySimpleGUI", layout)
event, values = window.read()
window.close()


