edad = int(input("ingrese su edad:"))
if edad < 0:
    print("la edad no puede ser nevativa.")
elif edad <= 12:
    print("categoria: niño")
elif edad <= 17:
    print("categori: adolecente")
elif edad <= 64:
    print("categoria: adulto")
else:
    print("categoria: adulto mayor")