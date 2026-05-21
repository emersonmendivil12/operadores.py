peso= float(input("ingrese su peso en kg:"))
altura = float(input("ingrese su altura en metros:"))
if peso <= 0 or altura <= 0:
  print("el peso y la altura deben ser mayores que 0")
else:                                                                                                                                                                                                                                                                                                                                                                                                                             
  imc= peso / (altura ** 2)
print(f"su IMC es: {imc:.2f}")                                                             
if imc < 18.5:
 print("categoria: bajo peso")
elif imc < 25:
 print("categoria: normal")
elif imc < 30:
 print("categoria: sobrepeso")
else:                                                                               
 print("gategoria: obesidad")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     