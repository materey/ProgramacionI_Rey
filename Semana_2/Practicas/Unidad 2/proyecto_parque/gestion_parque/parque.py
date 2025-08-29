def mostrar_atracciones()-> None:
    print("======ATRACCIONES DISPONIBLES======")
    print("1. Montaña Rusa - $1500 -")
    print("2. Casa del Terror - $1200 -")
    print("3. Carrusel - $800 -")
    print("4. Salir")

def puede_subir (edad:int, atraccion:int):
    if atraccion == 1 and edad >= 12:
        return True
    elif atraccion == 2 and edad >= 6:
        return True
    elif atraccion == 3:
        return True
    else:
        return False

def calcular_precio (atraccion):
    if atraccion == 1:
        return 1500
    elif atraccion == 2:
        return 1200
    elif atraccion == 3:
        return 800
    else:
        return 0

def registrar_visita():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    resumen = f"Resumen de {nombre}:"
    resumen += "Atracciones elegidas:"
    total = 0
    cantidad = 0

    while True:
        mostrar_atracciones()
        eleccion = int(input("Elija una atracción (4 para salir): "))

        if eleccion == 4:
            break

        if puede_subir(edad, eleccion):
            precio = calcular_precio(eleccion)
            if eleccion == 1:
                resumen += f"- Montaña Rusa (aprobado, ${precio})"
            elif eleccion == 2:
                resumen += f"- Casa del Terror (aprobado, ${precio})"
            elif eleccion == 3:
                resumen += f"- Carrusel (aprobado, ${precio})"
            total += precio
            cantidad += 1
        else:
            if eleccion == 1:
                resumen += "- Montaña Rusa (no permitido por la edad)"
            elif eleccion == 2:
                resumen += "- Casa del Terror (no permitido por la edad)"
            elif eleccion == 3:
                resumen += "- Carrusel (no permitido por la edad)"
            else:
                resumen += "- Opción inválida"


    if cantidad >= 3:
        descuento = total * 0.10
        total -= descuento
        resumen += f"Descuento aplicado: -${descuento}"

    resumen += f"Costo total a pagar: ${total}"
    return resumen




