alumnos:list[str]=['deduarso','noemi','victor','emerson','yo']
print(alumnos)
#eliminar por valor
alumnos.remove('yo')
print(alumnos)
# el ultimo valor por defecto
alumnos.pop()
# el metodo pop tieme la caracteristica de recuperar el elemento eliminado eso quiere dexcir que podemos almacenar en una bariable
## print(f"elimine:{a}")
# pop tambien elimina elementos por indice
alumnos.pop(1)
print(f"mi lista de desaprobados sera: {alumnos}")


#tengo una lista de marcas de veiculos (toyota,nissan,datsun,deawod,simo mark,mazda,honda)crea un programa que realize la sigueinte 
#1. eliminar el 5 elementio.
#2.en su lugar agregar la marca mitsubishi
#3. buscar nissan y mostrar  su valor terminal 
#4. mostrar si existe honda em mi listade veiculos
marcas_veiculos:list[str]=["toyota","nissan","datsun","deawod","simo mark","mazda","honda"]
marcas_veiculos.pop(4)
print(marcas_veiculos)
marcas_veiculos.insert(4,"mitsubishi")
print(marcas_veiculos)



buscar:int=marcas_veiculos.index("nissan") 
marcas_veiculos[buscar]
print(f"valor nissan es:{buscar}")



existe:bool="honda" in marcas_veiculos
print(f"valor de honda: {existe}")

