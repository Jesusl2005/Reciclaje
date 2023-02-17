import random
# Funcion ingreso de botellas que ejecuta los valores de las botellas y las guarda para calcular el valor de la comsision
def ingreso_botellas():
    print('Cuantas botellas va a ingresar?')
    botellas = input('> ')
    botellas = int(botellas)
    saldo = 0
    for i in range(botellas):
        peso = random.randrange(100,3000)
        print(f'El peso de la botella es de {peso} gr')
        if peso <= 500:
            saldo = saldo + 50
        else:
            if peso > 1500:
                saldo = saldo + 200
            else:
                saldo = saldo + 125
    print(f'El saldo total es de ${saldo:,.0f}, desea acreditarlo?')
    print('si/no')
    acreditar = input('> ')
    if acreditar.lower() == 'si':
        print('Su saldo ha sido acreditado exitosamente')
        return saldo
    else:
        print('Devolviendo el material ingresado')
        return saldo == 0
    
# Funcion de consulta de saldo, que muestra todos las comisiones de las botellas acreditadas            
def consultar_saldo(saldototal):
    print(f'Su saldo actual en la cuenta es de ${saldototal:,.0f}')
    
# Funcion menu, que muestra las opciones que tiene el usuario dentro del programa
def menu():
    print('--- MENU PRINCIPAL ---')
    print('')
    print('1- Ingresar botellas')
    print('2- Consultar saldo')
    print('3- Cerrar sesion')
    eleccion = input('> ')
    return eleccion