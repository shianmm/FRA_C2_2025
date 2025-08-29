def mostrar_atracciones():
    print("Atracciones disponibles:")
    print("1.Montaña Rusa")
    print("2.Casa del Terror")
    print("3.Carrusel")


def puede_subir(edad, atraccion):
    if atraccion == 1 and edad >= 12:
        return True
    elif atraccion == 2 and edad >= 6:
        return True
    elif atraccion == 3:
        return True
    else:
        return False


def calcular_precio(atraccion):
    if atraccion == 1:
        return 1500
    elif atraccion == 2:
        return 1200
    elif atraccion == 3:
        return 800
    else:
        return 0

def registrar_visita():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    mostrar_atracciones()
    cantidad = int(input("Cuantas atracciones quiere usar?: "))