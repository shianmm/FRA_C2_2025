vector_cargado  = [123,234,465,2,15,64,61,76,2,123]

def buscar_valor(vector_cargado,num):
    for i in range(len(vector_cargado)):
        if vector_cargado[i] == num:
            print(i)
            break
    else:
        print(-1)
buscar_valor(vector_cargado,2)
