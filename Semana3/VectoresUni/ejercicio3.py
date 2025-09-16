numeros_flotantes = [0.0] * 6
suma = 0

for i in range(len(numeros_flotantes)):
    numeros_flotantes[i] = float(input("Dame un numero: "))
    suma += numeros_flotantes[i]

promedio = suma / len(numeros_flotantes)

print(promedio)
