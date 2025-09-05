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

    costo_total = 0
    atracciones_texto = ""

    i = 1
    while i <= cantidad:
        opcion = int(input("Elija la atraccion " + str(i) + " (1-3): "))

        if puede_subir(edad, opcion):
            print("Puede subir a la atraccion", opcion)
            costo_total += calcular_precio(opcion)
            atracciones_texto += str(opcion) + " "
        else:
            print("No puede subir a la atracción", opcion, "por su edad")

        i += 1

    if cantidad >= 3:
        costo_total = costo_total * 0.9
        print("Se aplico un descuento del 10% por comprar 3 o mas atracciones")


    return nombre, edad, atracciones_texto, costo_total


def mostrar_resumen(nombre, edad, atracciones_texto, costo_total):
    print("Visitante:", nombre)
    print("Edad:", edad)
    print("Atracciones elegidas:", atracciones_texto)
    print("Costo total a pagar: $", costo_total)