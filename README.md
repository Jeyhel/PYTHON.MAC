nombre = input("Ingrese su nombre: ")
print(f"HOLA {nombre}")

radio = float(input("Ingrese el radio del circulo: "))
perimetro = float(3.1416)*2
radioDos = radio*2
area = float(3.1416*radioDos)
print ("El perimetro es: " , perimetro)
print ("El area es: " , area)

suma1 = input("Ingrese la primera nota")
suma2= input("Ingrese la segunda nota")
suma3 = input("Ingrese la tercera nota")
suma4 = input("Ingrese la cuarta nota")
sumas = int(suma1)+ int(suma2) + int(suma3) + int(suma4)
promedio = sumas / 4
print(promedio)

centimetros = float(input("Ingrese la cantidad de centimetro a convertir"))
pulgadas=(centimetros/2.54)
print(f"la cantidad es igual a" , {pulgadas})

numero = int(input(f"Ingrese un entero de tres digitos: "))
invert =int(str(numero)[::-1])
print (f"el numero invertido queda asi:{invert}")
