from funciones import *

titulos = [""] * 20
ejemplares = [0] * 20

while True:

    print("Menu Biblioteca")
    print("1. Cargar títulos y ejemplares")
    print("2. Mostrar catálogo completo")
    print("3. Consultar disponibilidad")
    print("3. Consultar disponibilidad")
    print("4. Listar titulos agotado")
    print("5. Agregar un titulo nuevo")
    print("6. Actualizar ejemplares")
    print("7. Salir")


    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        cargar_titulos(titulos, ejemplares)
    elif opcion == 2:
        mostrar_catalogo(titulos, ejemplares)
    elif opcion == 3:
        consultar_disponibilidad(titulos, ejemplares)
    elif opcion == 4:
        listar_agotados(titulos, ejemplares)
    elif opcion == 5:
        agregar_titulo(titulos, ejemplares)
    elif opcion == 6:
        actualizar_ejemplares(titulos, ejemplares)
    elif opcion == 7:
        print("Saliendo del sistema")
        break
    else:
        print("Opcion no valida")