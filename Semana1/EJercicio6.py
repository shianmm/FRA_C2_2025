# 6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
# cuántas horas y minutos sobran.

def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_sobrantes = minutos % 60
    print(f"{horas} horas con {minutos_sobrantes} minutos")

minutos = float(input("dame los minutos: "))
convertir_minutos(minutos)
