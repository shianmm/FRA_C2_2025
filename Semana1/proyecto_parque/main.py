from funciones import *

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Atracciones disponibles:")
print("1.Montaña Rusa")
print("2.Casa del Terror")
print("3.Carrusel")

cantidad_atracciones = int(input("Cuantas atracciones quiere usar?: "))

costo_total = 0


for i in range(1, cantidad_atracciones + 1):
    opcion = int(input(f"Elija la atraccion (1-3): "))
    atraccion = nombre_atraccion(opcion)
    
    if puede_subir(opcion, edad):
        print(f"Puede subir a {atraccion}")
        costo_total += precio_atraccion(opcion)
    else:
        print(f"No puede subir a {atraccion} por su edad")

print("RESUMEN")
print("Nombre:", nombre)
print("Edad:", edad)
print("Costo total a pagar: $", costo_total)