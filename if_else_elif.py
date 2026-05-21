## uso de if
### 1. hacer uso del keyword if
### 2. la condicion
### 3. inicio del bloque de codigo 
### 4. codigo identado a ejecutar si la condocion es cierta 
 
## observacion el bloque de codigo de if solo se ejecuta si la condicion es "true"

# caso real: deseamos dividir dos numeros, pero si el denominador es cero que no realise la operacion
numerador=20
denominador=4

if denominador > 0 :
    print(numerador/denominador)

## uso de else 
### else esta directamente relacionadacon if ya que es la manera de manejar si una condicion nose llega a cumplir 
### el bloque de if se ejecuta siempre la condicion es verdad mientras que rl bloque de else se ejecutara si esa condicion es falso
mi_numero=5
if mi_numero== 5:
    print("el numero es cinco")
else:
    print("el numero no es cinco")

## del elif
### este keyword se una cuando tenemos distintas bloques de codigo que deseamos ejecutar segun se cumplan distintas condiciones
## caso practico - deseo crear un pregrama que diga si una letra es una vocal o no 
vocal="b"
if vocal == "a":
    print("es la vocal a")
if vocal == "e": 
    print("es la vocal e")
if vocal == "i": 
    print("es la vocal i")
if vocal == "o":
    print("es la vocal o")
if vocal == "u":
    print("es la vocal u")
else:
    print(f"la letra {vocal} no es una vocal")

#f-string