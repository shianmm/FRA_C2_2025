vector_cargado  = [123,234,465,12,15,65,61]
mayor = vector_cargado[0]
posicion = 0


for i in range(len(vector_cargado)):
    if vector_cargado[i] > mayor:
        mayor = vector_cargado[i]
        posicion = i+1
print(f"La posicion es {posicion} y el numero es {mayor}")
