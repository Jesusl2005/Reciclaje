# MAQUINA DE RECICLAJE DE BOTELLAS
Necesitamos crear un sistema para una máquina de reciclaje de botellas automática. Dicha
máquina nos pagará dinero por la cantidad de plástico reciclado. Tenemos que ingresar
nuestro usuario y contraseña para que se nos cargue el saldo por sistema a nuestra
cuenta.

• Validaremos que el usuario sea “Albus_D”, luego si esto es
verdadero, validaremos si la contraseña es “caramelosDeLimon”. Si la contraseña es
correcta haremos que una variable llamada Login sea verdadera.

• El usuario sólo tendra 3 intentos para poner la contraseña.

• Una vez que el login sea verdadero, accederemos al
menú de opciones:

o Ingresar botellas
o Consultar saldo
o Salir

• Ingresar Botellas: Primero preguntaremos cuántas botellas se va a ingresar al sistema.
Una vez que tenemos el número vamos a usar un bucle para, a fin de ir ingresando
cada botella. En cada ciclo del bucle se debe generar un número aleatorio entre 100 y
3000 gr, que va a ser el peso de las botellas a reciclar (simulando que el usuario está
ingresando botellas en la máquina). Una vez generado, según el peso del material,
usaremos un condicional múltiple para asignarle un valor monetario:

o Si es menos de 500 gr, corresponden $50
o Si es entre 501 gr y 1500 gr, corresponden $125
o Si es más de 1501 gr, corresponden $200

Hecho esto, el programa debe informar al usuario por pantalla el valor que se le
ofrece. Si el usuario acepta, lo acreditamos a su saldo, sino se debe devolver el
material (sólo mostrar en pantalla “Devolviendo material”). Para esto usaremos un
condicional doble.

• Consultar saldo: revisaremos el valor monetario que tiene asignada la variable “saldo”.

• Tanto al terminar “Ingresar Botellas” como “Consultar Saldo” debe volver al menú
principal.