# diccionario
los diccionariosson la forma mas comun para alamacenar datos estruccturados de ubjetos que nos rodean en el mundo , al igual que las las listas que guardan en 'elementos', de igual manera alos diccionarios alamacena sus datos en 'elementos' separados por comas la diferencia es que las listas alamacenan los elementos por indice y valor :
y los diccionarios los alamacenan los elementos por 'clave y valor'. 
** ejemplo **
```python
vocales:list[str]=['a','e','i','o','u'] # valores
# indice            0   1   2   3   4 
# un elemento en una lista esta comformado por dos cositas indice y su valor 
# para acceder a un valor a la lista 
vocales[2]#1
alumno:dict={'nombre':'eduardo','edad':40}
# un elemento esta conformando por clave - valor
# para un diccionario
alumno["nombre"]#eduardo 
```
## acceder a elemento
- **por clave(dorma directa)** 
```python
persona:dict{
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celiemail.com"
}
print(persona["edad"])#16
print(persona["email"])#"celiemail.com"
```
- **por su metodo (forma mas segura)**
```python
persona:dict{
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celiemail.com"
}
print(persona.get("nombre"))#celia
# la diferencia de este metodo esq permite manejar errores
print(persona.get("telefono"))#none

print(persona.get("telefono","no disponible"))#si la clave telefono no existe no muestra none sino el segundo parametro del metodo get.             
```
## modifircar elementos 
** cambiar un valor existente ** 
```python
persona:dict{
    "nombre":"celia",
    "edad":16
}
persona["edad"]=19
#agrwgar una nueva clave-valor
persona["carrera"]="agro"
#la clave si no existe se crea automanticamente -- si existe solo se actualiza 
```
## agregar/actualizar multiples elementos 
para este tenemos tenemos que aser uso del metodo .'update'se puede agregar si lo0s pares de 'clave-valor'no existe y actualizar si el 'clave--valor'existe
```python
tienda:[str:str|int]={
    "razon social":"bigote",
    "ruc":123234243
}
#actuaqlizar usando el metodo update tengo dos maneras de usar el metodo
# 1 _ diccionario
tienda.update({"ruc":12334434454,"telefono"987654321})
#2 _ pares clave =valor    
tienda.update(h_atencion="9-12",gerente="kevin")
```
## eliminar elementos
```python
tienda:[str:str|int]={
    "razon social":"bigote",
    "ruc":123234243
}
el_elemento=tienda.pop("ruc")
tienda.popitem()#eliminar el ultimo elemento
#para limpiar todo el diccionario
tienda.clear()
```