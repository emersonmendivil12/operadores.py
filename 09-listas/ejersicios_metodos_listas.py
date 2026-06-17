#deseamos agg en una lista basia los nombres de los paises que participaran en el mundial ,desarrollar el programa que aga posible esta tarea 
paises:list[str]=[]
paises.append("peru")
paises.append("bolivia")
paises.append("chile")
#segunda forma
paises:str=input("ingresa el nombre de los paises: ")
paises.append(paises)
#tercera forma
rango:int=int(input("ingrese la cantidad de paises que deseas agregar: "))

for i in range(5):
    nuevos_paises:str=input("ingrese un pais: ")
    paises.append(nuevos_paises)
print (paises)


