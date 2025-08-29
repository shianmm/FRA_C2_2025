# 8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
# devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
# año de nacimiento del usuario y mostrar la edad calculada.

def calcular_edad(anio_nacimiento):
    edad_actual = 2025 - anio_nacimiento
    return edad_actual

nacimiento = int(input("año de nacimiento: "))
edad = calcular_edad(nacimiento)
print(f"tu edad actual es: {edad}")