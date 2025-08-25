def saludar(nombre):
    print(f"Hola {nombre}")


def promedio(a:int, b:int, c:int)-> float:
    #resultado = (a + b + c) /3
    #return resultado
    return (a + b + c) /3


def operar(a:int, b:int)->int:
    suma = a + b
    resta = a - b 
    multiplicacion = a * b
    return suma, resta, multiplicacion