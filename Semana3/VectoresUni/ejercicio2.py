numeros_enteros = [0] * 10
suma = 0
for i in range(len(numeros_enteros)):
    numeros_enteros[i] = int(input("Dame un numero: "))
    suma += numeros_enteros[i]

print(suma)