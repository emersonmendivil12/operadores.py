 # HACER UNA LISTA DE 5 AMIGOS  Y REMPLAZAR  SUS NOBRES POR NOMBRES DE FRUTAS 
amigos:list[str]=['lucas','mateo','luis','alex','julian']
print(amigos)
amigos[0]="manzana"
amigos[1]="naranja"
amigos[2]="platano"
amigos[3]="uva"
amigos[4]="pera"
print(f"mi lista modificada es: {amigos}")
### slicing
ciudades:list[str]=['lima','ica','chincha','pauza','urcos']
#si deseamos que los datos sean persistentes o se mantengan almacenados durante mi programa lo alamceno en una varialble  
datos_extraidos:list[str]=ciudades[-2:]
#si   solo deseo mostrar y no alamcenar el slincing la realizo en un print  
ciudades[0:3]
print(ciudades)
print(datos_extraidos)


















