import ingreso, menu
from os import system
def run():
    system('cls')
    print("*"*35)
    print("BIENVENIDO A RECICLEMOS BOTELLAS")
    print("*"*35)
    print("")
    
    ingreso.ingresar()
    system("cls")
    print('')
    print('*'*25)
    print('INGRESO EXITOSO')
    print('*'*25)
    print('')
    eleccion = menu.menu()
    eleccion = int(eleccion)
    saldototal = 0
    while eleccion !=3:
        if eleccion == 1:
            system('cls')
            saldo = menu.ingreso_botellas()
            saldototal = saldototal + saldo
        else: 
            if eleccion == 2:
                system('cls')
                menu.consultar_saldo(saldototal)
        eleccion = menu.menu()
        eleccion = int(eleccion)

    print('*'*25)
    print('Sesion finalizada')
    print('*'*25)
           
if __name__ == '__main__':
    run()
    