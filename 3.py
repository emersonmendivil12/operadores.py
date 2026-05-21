precio_original = float(input("ingrese el precio del producto:"))
if precio_original <= 0:
    print("el precio deve ser mayor que 0.")
else:
    if precio_original > 1000:
        descuento = 0.20
    elif precio_original >= 500:
        descuento = 0.15
    else:
        descuento = 0.10
    monto_descuento = precio_original * descuento
    precio_final = precio_original - monto_descuento
    print(f"descuento aplicado: {descuento*100}%")
    print(f"monto de descuento: S/{monto_descuento:.2f}")
    print(f"precio final: S/{precio_final:.2f}")