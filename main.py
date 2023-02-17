# Se importan los otros modulos del programa
import ingreso, menu
from os import system

# Se inicializa el programa principal
def run():
    system('cls')
    print("*"*35)
    print("BIENVENIDO A RECICLEMOS BOTELLAS")
    print("*"*35)
    print("")
    # Inicia el modulo de ingreso del usuario
    ingreso.ingresar()
    system("cls")
    print('')
    print('*'*25)
    print('INGRESO EXITOSO')
    print('*'*25)
    print('')
    # Inicia el modulo de opciones de menu principal
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
    # Finaliza el programa
    print('*'*25)
    print('Sesion finalizada')
    print('*'*25)
           
if __name__ == '__main__':
    run()
    