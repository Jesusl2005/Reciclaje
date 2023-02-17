from os import system
def ingresar():
    intentos = 0
    for i in range(3):
        print('--- INGRESE EL USUARIO ---')
        user = input('> ')
        if user == 'Albus_D':
            print('--- INGRESE LA CONTRASEÑA ---')
            key = input('> ')
            if key == 'caramelosDeLimon':
                break
            else:
                print('Contraseña incorrecta, intentelo nuevamente')
                print(f'Te quedan {2-i} intentos')
                print('')
                system('cls')
                intentos += 1
        else:
            print('Usuario incorrecto, intentelo nuevamente')
            print(f'Te quedan {2-i} intentos')
            print('')
            intentos += 1
    if intentos == 3:
        print('Usuario bloqueado')
        print('Sesion cerrada')