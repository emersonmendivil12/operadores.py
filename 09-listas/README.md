# DATOS ESTRUCTURADOS
- TENEMOS TRES TIPOS DE DATOS PRIMARIOS (string,numerico,boleanos)
- TENEMOS DOS TIPOS DE DATOS ESTRUCTURADOS (listas,diccionarios)
## LISTAS 
som la manera como python puede organizar multipes tipos de datos en una sola variable
- listas de tipo numerico
- listas de tipo texto
- listas de tipo mixto
python nos permite acceder a lista atravez de indice, los indices son asendentes enpesando deñ numero 0. 
### creacion de listas 
para crear listas solo basta encerrrar los elementos que deseamos almacenar con corchetes '[]'inmediantemente despues del operador de asignacion `=`
```python
# creando una lista vacia
lista:list=[]#lista vacia ""list ANOTACION , QUE TIPO DE DATO ALMACENA LA BARIABLE 
#lista numerica
##OJON:Los elementos de una lista se separan por comas 
lista_numerica:list[int]=[1,2,3,4] lista numeros enteros 
lista_num_mixta:list[int|float]=[3.8,3,9.4] lista numeros mixtos
# lista de texto
amigos:list[str]=[`eduardo´,`kevin`]
#lista mixta👌👍
lista_mixta=list["pedro",20,false,1.67]
```
### acceder y modificar alementos de una lista 
para poder acceder a a un elemento de la lista trabajamos con los indices que python lo asignan a cada elemento tenemos:
-- los indicies positivos {comiensan de 0 y van de la izquierda ala derercha} 
-- los indicies negativos {comiensan de -1 y van de la derecha ala izquierda}
son los indices podemos acceder al valor del elemento y tambien podemos modificarlos:
tenemos dos formas de acceder  alo0s elementos 
- por indice (posicion)
- por rango (slicing)
```python
frutas:list[str]=["🍎","🍍","🍐","🍒"] 
#posision indice 
# acceder al tercer elemento
print(frutas[2])
#acceser al segundo elemento 
print(frutas[3])
#modificar el ultimo elemento con una naranja 
frutas[-1]="🍎"
print(frutas)

# como acceder por rango
```python
# ACEDER Y MODIFICAR POR RANGO
- ACCEDER Y MODIFICAR POR RANGO (STR)
```
```python
vocales:str=['a','e','i','o','u']
vocales[0:3]
#   REMPLASAMOS LOS ELEMENTOS POR SLACING
    vocales[0:3]=['A','E','I']
    
```
 el rango (o slice) te permite obtener una subsección de una lista, string, tupla, etc., usando la sintaxis:
 objeto[inicio:fin:paso]
 numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 print(numeros[2:5])
## metodods para listas 
un metodo es unaaccionque puedo realizar en una lista los metodos x lo general se utilixa despues de una variable se accede a traves de un punto .
los metodos mas comunes son aquellos que nos permiten .agregar .modificar y eliminar 
```python
append
animales:list[str]=[]
animales.append("leon")
animales.append("gato")
el metdo append agrega los elementos en la ultima posicion de nuestra lista
numeros_pares:list[int]=[4,6,10]
numeros_pares:insert(0,2)
numeros_pares:insert(0,3)

amigos.insert("juan","jose")
amigos.insert("")
## eliminar por indice
vocales:list[str]=("a","e","i","o","u")
elimina al ultimo elemnto
vocales.pop("u")

vocales.pop(3)

## BUSCAR
# Este metodo permite ubicar atraves del valorel primer elemntodentro de un lista  y devolvera el indice de ese valor este metodo es index  
amantes:list[str]=['chapo','cristian','emerson','victor']
# quiero ubicar si en mi lista amantes existe victor

buscar:int=amantes.index("victor") 

amantes[buscar]
### busqueda por pertenencia
existe:bool="chapo" in amantes
```
## DICCIONAROS👌
