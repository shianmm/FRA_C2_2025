vector_cargado  = [123,234,465,12,15,65,61,76,1,123]

numero_solicitado = int(input("Dame un numero: "))

for i in range(len(vector_cargado)):
    
    if vector_cargado[i] == numero_solicitado:
        print(f"Se encuentra en la posicion {i+1}")
else:
    print("No se encontro el numero")