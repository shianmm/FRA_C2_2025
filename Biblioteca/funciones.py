titulos = [""] * 20
ejemplares = [0] * 20

def cargar_titulos(titulos, ejemplares):
    i = 0
    while i < 20:
        titulo = input("Ingrese título (ENTER para terminar): ")
        if titulo == "":
            break
        cantidad = int(input("Ingrese cantidad de ejemplares: "))
        titulos[i] = titulo
        ejemplares[i] = cantidad
        i += 1

# def mostrar_matriz():
#     print(f" {titulos}\n {ejemplares}")


cargar_titulos(titulos,ejemplares)
# mostrar_matriz()


def mostrar_catalogo(titulos, ejemplares):
    print("Catalogo completo")
    for i in range(len(titulos)):
        if titulos[i] != "":
            print(f"{titulos[i]} → {ejemplares[i]} copias")

mostrar_catalogo(titulos, ejemplares)


def consultar_disponibilidad(titulos, ejemplares):
    titulo = input("Ingrese el titulo a consultar: ")
    for i in range(len(titulos)):
        if titulos[i] == titulo:
            print(f"{titulos[i]} tiene {ejemplares[i]} copias")
            break
    else:
        print("Título no encontrado.")

consultar_disponibilidad(titulos, ejemplares)

def listar_agotados(titulos, ejemplares):
    print("Titulos agotados")
    for i in range(len(titulos)):
        if titulos[i] != "" and ejemplares[i] == 0:
            print(titulos[i])