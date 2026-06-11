lista_vacia:list=[]
print(len(lista_vacia))
# por regla el nombre de una variable no deve teneral dato que se va almacenar 
amores:list[str]=["wicho","pocohuanca","cesar","guido","percy"] 
print(f"cantidad de elementos que tiene la variable amores es:{len(amores)}")
frutas:list[str]=["🍎","🍍","🍐","🍒"] 
#posision indice 
# acceder al tercer elemento
print(frutas[2])
#acceser al segundo elemento 
print(frutas[3])
#modificar el ultimo elemento con una naranja 
frutas[-1]="🍎"
print(frutas)
#REMPLASO DE ELEMENTOS POR SLAICING
num_pares:list[int]=[1,3,6,8,10]
print(num_pares)
num_pares[0:3]=[2,4]
print(f"mi lista modificada es: {num_pares}")
