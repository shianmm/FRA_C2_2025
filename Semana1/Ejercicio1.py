# 1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprimaun saludo.
#  Luego, el programa debe pedir el nombre del usuario y llamar a la función.


def saludar(nombre):
    print(f"Hola {nombre}")

nombre = input("Ingresa tu nombre: ")
saludar(nombre)