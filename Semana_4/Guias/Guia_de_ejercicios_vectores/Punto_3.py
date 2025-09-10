reales = [0] * 6


suma_reales = 0

for numero in range(len(reales)):
    reales[numero] = float(input(f"Ingrese el numero {numero + 1}: "))

for numero in range(len(reales)):
    suma_reales += reales[numero]

promedio = suma_reales / len(reales)

print(f"El promedio de los reales es {promedio}")