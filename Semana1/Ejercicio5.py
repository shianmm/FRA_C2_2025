# 5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si
# es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("dame un numero: "))

par_o_impar = es_par(numero)
print(par_o_impar)