import ingreso, menu
import PySimpleGUI as sg
from os import system

def run():
    Layout1 = [
        [sg.Text('BIENVENIDO A RECICLEMOS BOTELLAS')],
        [sg.Button('INGRESAR'), sg.Button('CERRAR')]
    ]

    window1 = sg.Window('Maquina de reciclaje', Layout1)
    while True:
        evento, valores = window1.read()
        if evento == "INGRESAR":
            break
        elif evento == "CERRAR" or evento == sg.WIN_CLOSED:
            window1.Close()
            exit()
    
    ingreso.ingresar()
    Layout6 = [
        [sg.Button('INGRESAR BOTELLAS')],
        [sg.Button('CONSULTAR SALDO')],
        [sg.Button('CERRAR SESION')]
    ]
    saldototal = 0
    window6 = sg.Window('MENU PRINCIPAL', Layout6)
    while True:
        evento4,valores4 = window6.read()
        if evento4 == 'INGRESAR BOTELLAS':
           saldo = menu.ingreso_botellas()
           saldototal = saldototal + saldo
        elif evento4 == 'CONSULTAR SALDO':
            menu.consultar_saldo(saldototal)
        elif evento4 == 'CERRAR SESION':
            sg.popup('SESION FINALIZADA')
            exit()
if __name__ == '__main__':
    run()
    