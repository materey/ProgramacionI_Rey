print("==============BIENVENIDOS AL PARQUE DE DIVERSIONES PYTHONLAND=============")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
cantidad = input("Cuantas atracciones desea usar? Entre 1 y 3: ")
if cantidad < 1 and cantidad > 3:
    print("ERROR, POR FAVOR ELEGIR CANTIDAD DEL RANGO ESPECIFICADO")



precio_montaña = 1500
precio_terror = 1200
precio_carrusel = 800

print("EL PARQUE CUENTA CON CONDICIONES DE ACCESO PARA LAS ATRACCIONES")

total = 0
for i in range(cantidad):
    print("Atracciones disponibles: ")
    print(f"1. Montaña Rusa (${precio_montaña})")
    print(f"2. Casa del Terror (${precio_terror})")
    print(f"3. Carrusel (${precio_carrusel})")

    eleccion = int(input("Elija una atracción (1-3): "))
    if eleccion == 1:
        if edad >= 12:
            print(f"{nombre} puede subir a la Montaña Rusa")
            total += precio_montaña
        else:
            print(f"{nombre} no puede subir a la Montaña Rusa")
    elif eleccion == 2:
        if edad >= 6:
            print(f"{nombre} puede subir a la Casa del Terror")
            total += precio_terror
        else:
            print(f"{nombre} no puede subir a la Casa del Terror")
    elif eleccion == 3:
        print(f"{nombre} puede subir al Carrusel.")
        total += precio_carrusel
    else:
        print("Opción no válida, por favor seleccione en el rango especificado")


print("=====RESUMEN=====")

print(f"El visitante {nombre} eligio'")
