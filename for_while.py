## ejemplos con for 
#for numero in range(5):
    #print ("hola")

# fores la sentencia de python esas preferida recorer una lista
#amigos=["eduardo","jymy","pepe"] 
#for amigo in amigos:
   # print(amigo)
    #if amigo=="jymi":
     #   print(f"aya tu eres el famoso {amigo}")

## recorrer una lista de numeros aletorios y mostrar solo los numeros pares que tenga una lista 

#numeros=(1,2,3,4,5,6,7,8,9)
#for n in numeros:
   # if n % 2 == 0:
     #   print(n)

## de una lista de letras solo encuentra que sean vocales 

letras=["a","b","e","d"]
for n in letras:
    if n in      "aeiou":
        print(f"{n}es una vocal")
##    
respuesta="s"
while respuesta=="s": 
    respuesta=input("escrive S/N:")



while True:
    print("bienvenido a mi programa de vocales")
    pedir_vocal=input("ingrese uma vocal; ")
    if pedir_vocal in "aeiou":
        print("continuamos con el programa")
    else:
        break 