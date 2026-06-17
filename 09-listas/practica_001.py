"""
1:lista de productos de limpieza(10 productos)
2:lista de materiales de constuccion 
el dueño desea realizar la siguiente  acciones 
1 en su lista de productos  de limpieza  exiiste un material de construccion.
 deves eliminarlos y pasar el producto al lista que corresponde 
2:indicar  si la lista M.c  existe cemento 
3; el la lista de p.l  buscar el producto legia sapolio 
4: nostrar unmensaje  donde se detalle cual  cual es la lista  de m.c y la lista de p.l formateo
"""
productos_limpieza:list[str]=['detergente','legia','jabon','desinfectante','escoba','trapeador','trapo','jabon liquido','cemento','limpia vidrios ']

print(f"productos de limpieza es: {productos_limpieza}")

materiales_construccion:list[str]= ["Ladrillos","Arena","Cal", "Yeso", "Varillas de acero","clavo","martillo","espatula","regla","plancha"]
print(f"mi malteriales de construccion es: {materiales_construccion}")

elemento_retirado=productos_limpieza.pop(productos_limpieza.index('cemento'))
materiales_construccion.append(elemento_retirado)
print(elemento_retirado)


existe:bool='cemento' in materiales_construccion
print(f"valor de cemento es : {existe}")


buscar=productos_limpieza.index("legia")
productos_limpieza[buscar]="legia sapolio"
print (productos_limpieza)

print("\n" + "=" * 50)
print("RESULTADOS DE LAS ACCIONES")
print("=" * 50)
print(f"¿Existe 'Cemento' en materiales de construccion? {'Sí' if 'existe cemento' else 'No'}")
print(f"¿Existe 'Legía Sapolio' en Productos de limpieza? {'Sí' if 'existe_legia_sapolio' else 'No'}")

mensaje:str=f'''
mi lista de productos de limpiesa modificada queda la siguiente manera
{productos_limpieza}
----------------------------------------------------------
mi lista de materiales  de costruccion  despues de las modifaciones queda de la siguiente 
manera
{materiales_construccion}
'''
print(mensaje)


