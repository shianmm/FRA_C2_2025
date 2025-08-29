def precio_atraccion(opcion):
    if opcion == 1:
        return 1500
    elif opcion == 2:
        return 1200
    elif opcion == 3:
        return 800
    else:
        return 0
    

def nombre_atraccion(opcion):
    if opcion == 1:
        return "Montaña Rusa"
    elif opcion == 2:
        return "Casa del Terror"
    elif opcion == 3:
        return "Carrusel"
    else:
        return "Opcion invalida"


def puede_subir(opcion, edad):
    if opcion == 1 and edad >= 12:
        return True
    elif opcion == 2 and edad >= 6:
        return True
    elif opcion == 3:
        return True
    else:
        return False