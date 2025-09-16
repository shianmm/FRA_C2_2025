vector_cargado  = [123,234,465,12,15,64,61,76,2,123]

for i in range(len(vector_cargado)):
    if vector_cargado[i] % 2 == 0:
        vector_cargado[i] = 0

print(vector_cargado)