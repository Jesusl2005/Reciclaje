from os import system
import PySimpleGUI as sg
def ingresar():
    Layout2 = [
    [sg.Text('INGRESE EL USUARIO')],
    [sg.Input(key='user')],
    [sg.Text('INGRESE LA CONTRASEÑA')],
    [sg.Input(key='key', password_char='*')],
    [sg.Button('Log in'), sg.Button('Exit')]
    ]

    window2 = sg.Window('Entrada', Layout2, element_justification='center')
    intentos = 3
    salir = 1
    while intentos != 0 and salir != 0:
        evento, valores = window2.read()
        if evento == 'Exit' or evento == sg.WIN_CLOSED:
            salir = 0
        elif evento == 'Log in' and valores['user'] == 'Albus_D' and valores['key'] == 'caramelosDeLimon':
            sg.popup('INGRESO EXITOSO')
            break
        elif (valores['user'] != 'Albus_D' or valores['key'] != 'carmelosDeLimon'):
            intentos = intentos-1
            if intentos != 0:
                sg.popup(f'Ingreso incorrecto, te quedan {intentos} intentos')
            else:
                sg.popup('Sesion bloqueada')
                salir = 0
    window2.close()
    return salir
            