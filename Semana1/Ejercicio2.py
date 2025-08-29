# 2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
# resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
# función.


def operaciones(num1,num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    print(f"Suma: {suma}, Resta: {resta}, Multiplicacion: {multiplicacion}")

numero1 = int(input("Dame un numero: "))
numero2 = int(input("Dame un numero: "))

operaciones(numero1, numero2)