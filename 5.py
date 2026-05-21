temperatura = float(input("ingrese la temperatura:"))
unidad = input("ingrese la unidad de origen (C/F):").upper()
if unidad == "C":
    fahrenheit = (temperatura * 9/5) + 32
    print(f"{temperatura:.2f}°c = {fahrenheit:.2f}°F")
elif unidad == "F":
    celcius = (temperatura - 32) * 5/9
    print(f"{temperatura:.2f}°F = {celcius:.2f}°C")
else:
    print("unidad no valida. use C para celsius o F para fahrenheit.")
