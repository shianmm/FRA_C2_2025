from gestion_parque.parque import *

def main():
    nombre, edad, atracciones_texto, costo_total = registrar_visita()


    mostrar_resumen(nombre, edad, atracciones_texto, costo_total)

main()