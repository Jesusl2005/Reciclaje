import PySimpleGUI as sg
# Funcion ingreso de botellas que ejecuta los valores de las botellas y las guarda para calcular el valor de la comsision
def ingreso_botellas():
    Layout3 = [
        [sg.Text('Ingrese la cantidad de botellas a cotizar')],
        [sg.Input(key='botellas')],
        [sg.Button('Cotizar')]
    ]
    Layout4 = [
        [sg.Text(f'Ingrese el peso de la botella'), sg.Text('1', key='cont')],
        [sg.Input(key='peso')],
        [sg.Button('Agregar')]
    ]

    window3 = sg.Window('Ingreso botellas', Layout3)
    while True:
        evento, valores = window3.read()
        if evento == 'Cotizar':
            botellas = valores['botellas']
            botellas = int(botellas)
            window4 = sg.Window('Ingreso botella', Layout4)
            saldobotellas = 0
            cont = 1
            for i in range(botellas):
                evento2, valores2 = window4.read()
                pesobotella = valores2['peso']
                pesobotella = int(pesobotella)
                window4['peso'].update('')
                if pesobotella <= 500:
                    saldobotellas = saldobotellas + 50
                elif pesobotella > 1500:
                    saldobotellas = saldobotellas + 200
                else:
                    saldobotellas = saldobotellas + 125
                cont += 1
                window4['cont'].update(cont)
            Layout5 = [
                [sg.Text(f'El saldo total es de ${saldobotellas:,.0f}')],
                [sg.Text('Desea acreditar el saldo?')],
                [sg.Button('Si'), sg.Button('No')]
            ]

            window5 = sg.Window('Ingreso Botellas', Layout5)
            evento3, valores3 = window5.read()
            if evento3 == 'Si':
                sg.popup('Saldo acreditado exitosamente')
                window3.close()
                window4.close()
                window5.close()
                return saldobotellas
            else:
                sg.popup('Devolucion de las botellas procesada exitosamente')
                window3.close()
                window4.close()
                window5.close()
                saldobotellas = 0
                return saldobotellas
    
# Funcion de consulta de saldo, que muestra todos las comisiones de las botellas acreditadas            
def consultar_saldo(saldototal):
    sg.popup(f'El saldo total acreditado a la cuenta es: ${saldototal:,.0f}')