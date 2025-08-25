import funciones

print("Bienvenidos al programa")

nombre = input("Ingresar nombre: ")
funciones.saludar(nombre)

numero_1 = int(input("Numero 1: "))
numero_2 = int(input("Numero 2: "))
numero_3 = int(input("Numero 3: "))

resultado_promedio = funciones.promedio(numero_1, numero_2, numero_3)

#Al ser una funcion que devuelve el resultado en un dato especifico, se necesita de guardarlo en una variable



resultado_suma, resultado_resta, resultado_multiplicacion = funciones.operar(numero_1, numero_2)
#Se debe respetar el orden de las variables puestas en la funcion
