# operadores arimenticos
from ast import Div, Expression, Module
from decimal import DivisionByZero
from itertools import product
from pdb import Restart


primer_numero=24
segundo_numero=30
suma=primer_numero+segundo_numero
print("suma",suma)
primer_numero-segundo_numero
print("resta",Restart)
print("Multiplicacion:",product)

print("divicion con decimales",Div)
print("Modulo",Module)

## ejemplos de operadores comparacion y logicos 
#Operadores lógicos:
and :evalúa_si_dos_condiciones _son _verdaderas _al _mismo_tiempo_Ejemplo: 
1
or(): Evalúa si al menos una de las condiciones es verdadera. Ejemplo: 
1
not (!): Negra el valor de su entrada. Ejemplo: !
1
Operadores de comparación:
==: Compara si dos valores son iguales. Ejemplo: a == b. 
1
<: Compara si el valor de la izquierda es menor que el de la derecha. Ejemplo: a < b. 
1
>: Compara si el valor de la izquierda es mayor que el de la derecha. Ejemplo: a > b. 
1
<=: Compara si el valor de la izquierda es menor o igual que el de la derecha. Ejemplo: a <= b. 
1
>=: Compara si el valor de la izquierda es mayor o igual que el de la derecha. Ejemplo: a >= b. 

#operadores logicos    
##and
###esta expesion sera verdadera siempre que ambos datos sean verdaderos caso contrario sera falso 

usuario=input("ingesa tu usuario:")
password=input("ingresa tu contraseña:")

user_bd="administrador"
pass_bd="admin1234"

mensaje=usuario==user_bd and password==pass_bd
if mensaje:
 print(" Bienvenido al sistema")
else:
 print("usuario o contraseña incorrecta")

## or
### toda una exprecion sera verdadera si almenos unode sus datos es verdadero caso contrario sera falso 
logico_False or True
print("expresion con or:",logico_or)

##not
### wate operador unario niega aldato que esta asu derecha

negando_valor=not True
print(negando_valor)
