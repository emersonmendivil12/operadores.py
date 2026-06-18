#modulo y libreria estandar 
#libreria estandar typing datos list y diccionarios para ser mas optimo codigo 
#un modulo es una porcion de codigo utilisable para poder utilizarlo nesecitamos inportar la parte del codigo que deseamos utilizarlo
#en este codigo estoy ipoirtando desde la libreria typing de la funcion union:
#tipos si no sabes los tipos de datos con union lo podemos pasar una lista de los posibles datos que puede tener mi valor  
from typing import Union
#sin libreria
#alumno:dict[str:str|int]
alumno:dict[str:Union [str,int,float,bool]]={
    "id_alumno":1,
    "dni":7865432,
    "nombre":"mio",
    "edad":20,
    "matricula":True,
}
# acceder
##clasica
print (alumno["dni"])
##METODO
print(alumno.get("edad"))
#crear/modificar
print(alumno)
alumno["nombre"]="otro" #si existe la clabe e actializa
alumno["ruc"]=87678575655#sino existe la clave se crea
#crea
print(alumno)
#crear/modificar varios
alumno.update({"nombre":"celia","edad":15})
alumno.update({"carrera":"agro","semestre":"III"})
print(alumno)
#eliminar
eliminado=alumno.pop("carrera")
print(f"el elemento elimindo es:{eliminado}")
print(f"mi nuevo diccionario{alumno}")