# algoritmos y estructura de datos con phyton
## comentarios
los comentarios no solo en phyton si no en cualquier lenguaje de programacion son utiles a nivel educativo y para la explicacion de cada linia y para la explicacion de cada linea de codigo que se escrive .
los comentarios no se ejecutan por el interprete de phyton , eso quiere decir que no son visto como codigo en si solo como anotaciones .
existen dos maneras de escrivir de comentario 
1. de una sola linia 
2. multilinea "docstring"
```python
#aqui van comentarios de una linia 
#otro comentario de una linia 
```
comentario
de multi
linea

```

## tipos de datos 
los tipos de datos son informacion absoluta y atomica que nos permite procesarlos para obtener como resultado otro dato 

> [!tip] El dato es absoluto cuando un dato se puede medir o realizar operacion ellas y decimos que es atomico por que esa nformacion ya no se puede dividir en mas datos 
>
> en caso de "phyton" tenemos hasta 5 tipos de datos , al decir tipos nos referimos que vamos a clasificar o agrupar los datos segun su semejanza 

1. **Numericos** dentro de los datos de tipo numerico tenemos una sub clasificacion:
   - enteros **integer (int)** positivo y negativos 
        ```python
        23
        -12
        ```
   - decimales **flotante (float)** positivo y negativos 
        ```python
        2.4
        -3.4
        ```
2.  **texto string(str)**
este tipo de dato me oermite capturar informacion de tipo texto ocadena ,cosiderando todo el que este entre comillas ``` como un caracter .
se puede usar comillas dobles o comillas sinples la informacion de tipo de cadena deve estar entre las comillas
     ```python
     "emerson"
     `2025`
      ```
3. **boleanos (bol)**

este es un tipo de dato que tiene dos estados
- true-verdad
- false-falso
```python
true 
false
```
4. **listas (list)** **tarea**
- una lista es un tipo de dato estruccturado- puedes almacenar una varierdad  de tipos datos 
```python
# para crear una lista de un corchetes(scuard brakets)[]
[] #lista vacia
## una lista puede tener elementos cada elementos puede ser del mismo tipo de dato o distintos, cada elemento dentro de una lista devera estar separados por comas (,)
[1,2,3,4,5] # una lista de datos numericos
["a","e","i","o","u"] # lista de datos estring 
[True,False,False] # una lista de datos booleanos 
["emerson" , 17,True] # una lista de datos mixtos
# Una lista ordenadas de datos
[3,2,6,7,8] 
# se dice que esta ordenado por que python lo asigna un indice acendiendo  a cada elemento comenzando por el numero 0 
# 0,1,2,3,4
# indice es el identificador que python le asigna a cada elemento tenemos dos tipos de indice
# indices positivos que son los indices que comienzan en 0 y se  van aumentando en uno de izquierda a derecha 
# indices negativos que son indices que comienzan de -1 y van decreciendo en uno desde la derecha hacia la izquierda 
["🍎","🍍","🍐","🍒"]
# 0 ,   1  , 2   ,  3 indice positivo 
# -4 ,  -3 , -2 , -1  i      ndice negativo  
 ``` 
5. **diccionarios(dict)** **tarea**
al igual que las listas es una coleccion oedenada de datos la diferencia es lasiguiente :
- una lista ordenada sus elementos en indice y valor 

- en vambio un diccionaria sus elementos con clave :valor 
```python
{} #diccionario vacio 
# al igual que las listas tenemos elementos y cada elementos se separa por comas (,)
{nombre:"",edad:50,sexo"no especifica" }
```
- ejemplos
## tipos de errrores en python ("tarea")
El error NameError en Python ocurre cuando intentas usar una variable, función o biblioteca que no ha sido definida o está fuera de su alcance. Este error es común y puede solucionarse fácilmente al identificar la causa.
En Python, los errores se dividen principalmente en errores de sintaxis y excepciones. A continuación, se explican los tipos más comunes con ejemplos:

## 1. Error de Sintaxis (SyntaxError)
### print
es cuando escreibes mal las palabras reservadas de python y las built>it.
print()
input()
int()

 
####  2.exepcion o en ejecucuion 
estos errores se muestran cuando ejecutan el codigo.
#### 1. syntaxErrors
este error se muestra cuando el codigo violas las reglas de lenguaje de programacion 
## 2.  IdentationError
python utiliza sangrias (identacion) para definir la jerarquia del codigo
## 3.TypeError
este error surge cuando ententamos para definir la jerarquia del codigo
## 4.ValueError
este error se produce cuando una funcion de python un dato correcto pero su valor es inapropiado 

### 3. errrores logicos 
error humano, cuando retornau obtienes una respuesta distinta a la que esperabas   
## 5.NameError 
es un error que se muestra cuando intentamos usar una variable funcion o modulo que no existe o no esta definido,

## variables y constantes (investigacion examen la siguiente clase)pag. 50-58
### reglas para nombrar variables 
en python existen 4 reglas principales para el nombre de los variables .
- letras minusculas
- letras mayusculas
- digitos
- guiones bajos (_)
### comvenciones para nombrar variable y constante 
en el caso phyton la comvencion que suele usar al nombrar una variable en "snake_case" .
 ```python
primer_numero=23
segundo_numero=34
 ```
la convencion para nombrar unaconsonante es haciendo el uso de mayuscula "SNAKE_CASE"
 ```phyton
 NUMERO_DNI=71644254
 VALOR_PI=3.141516
  ```
### QUE ES LA MUTABILIDAD
consiste en en que cada variable apesar de tener el mismo nombre , cada vez que se crea apunta a un espacio distinto de memoria. 
## operadores (investigacion examen la siguente clase)pag.63/73
- (+)operador de suma
- (-)operador de resta
- (*)operador de multiplicacion 
- (/)operador de division 
- (//)operador de division exacta
- (**)operador de potencia 
- (=)operador de asignacion 
### operacion de comparacion 
-( >)mayor que 
- (<)menor que 
- (==) igual a
- (>)mayor igual
- (<)menor igual 
### operadores logicos
este es un operardor vinario que recibe dos valores y nos da como resultado un valor que puede ser "True" o "False"
- and (True and False)
- or (4>5 or 8<2)
operador logico pero unario eso quiere decir que solo evakue un dato y como resultado un valor que puede ser "True" o "False" 
- not (not True)
## structura de decision if else 
esta estructura nos permite cambiar ewl flujo de un programa en algunos lenguajes de programacion selo conoce como controles de flujo :
grasias a esta estructura de control podemos lograr sietos bloques se ejecuten y solo si se dan unas condiciones particulares 
### Uso del if 
"if" nos permite ejecutar un bloque de codigo  si una condicion es cierta 

> [!NOTE]
> **Que es bloque de codigo** - es un codigo que se ejecuta despues de cumplir ciertas condiciones , los bloques codigo comienza siempre con ":".,los bloquesde codigo sienpre estan identados e indican que codigo se deve ejecutar  apartir de la instruccion que se lo de 
> **Que es un identado** - es el espacio que se le da a una linia de codigo, el tamaño o espacio que se lo da es en cuatro espacios o un tab. 
> **Keywords en los que se ejecutan bloques de codigo**
"if" , "else" , "elif" , "for" , "while" , "def" , "class"
## estructura de repeticion for y while(ciclos o bucles)
este mecanismo que usa python para repetir instruciones 

mientras que una condcion sea verdad el bloke de codigo se ejecuta asta asta la condicion sea falsa 

> [!TIP]
> tanto "for" como "while" tienen el mismo comportamiento, la diferencia usamos "for" cuando sabemos las veses que vamos a repetir un codigo. usamos while cuando la repeticion  del codigo esta condicionado por un acto externo 
## ciclos de blucles con for  
Un bucle for se usa cuando queremos repetir una acción un número determinado de veces.
Por ejemplo, si quieres imprimir los números del 1 al 5, puedes hacerlo con un for en lugar de escribir cinco veces la misma instrucción.
>