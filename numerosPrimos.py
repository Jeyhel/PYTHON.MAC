numero = int(input("Ingrese algun numero: "))
k = 1
m = 0

while k <= numero:
    if numero % k == 0: 
        m = m + 1 
    k = k + 1
if m == 2: 
    print("El numero ", numero, " es primo")
else:
    print("El numero ", numero, " no es primo")   
    