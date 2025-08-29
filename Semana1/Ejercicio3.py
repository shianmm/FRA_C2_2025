# 3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y
# devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
# Fórmula: area = (b * h) / 2.

def area_triangulo(base,altura):
    area= (base * altura) / 2
    return area
    

base = float(input("dame la base:"))
altura= float(input("dame la altura:"))

area = area_triangulo(base, altura)
print(area)