def verificar_acceso (edad:int) -> None:
    while edad >= 18:
        return True



edad = int(input("Ingrese su edad: "))

if verificar_acceso(edad):
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
