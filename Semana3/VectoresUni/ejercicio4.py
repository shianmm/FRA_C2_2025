# numeros_enteros = [0] * 8

# contador = 0

# for i in range(len(numeros_enteros)):
#     numeros_enteros[i] = int(input("Dame un numero: "))
#     if numeros_enteros[i] > 100:
#         contador += 1

# print(contador)


vector_cargado  = [123,234,465,12,15,65,61,76]
contador = 0

for i in range(len(vector_cargado)):
    if vector_cargado[i] > 100:
        contador += 1

print(contador)