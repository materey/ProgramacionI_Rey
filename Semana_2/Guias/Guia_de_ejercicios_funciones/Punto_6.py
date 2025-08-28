def convertir_minutos (min):
    horas = 0
    while min >= 60:
        min -= 60
        horas += 1
    return str(horas) + " horas y " + str(min) + " minutos"


minutos = int(input("Ingresa la cantidad de minutos: "))

minutos_convertidos = convertir_minutos(minutos)
print(f"{minutos} minutos son {minutos_convertidos}")
