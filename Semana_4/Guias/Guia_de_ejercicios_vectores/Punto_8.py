vec_1 = [0] * 5
vec_2 = [0] * 5

for i in range(5):
    vec_1[i] = int(input(f"Ingrese el elemento {i + 1} del primer array: "))


for i in range(5):
    vec_2[i] = int(input(f"Ingrese el elemento {i + 1} del segundo array: "))


iguales = True
for i in range(5):
    if vec_1[i] != vec_2[i]:
        iguales = False
        break

if iguales:
    print("Los arrays son iguales elemento a elemento")
else:
    print("Los arrays no son iguales elemento a elemento")