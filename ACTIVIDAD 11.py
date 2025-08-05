def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)
n = int(input("cuantos nombres quiere ingresar"))
nombres = []

for i in range (n):
    nombre=input("ingrese el nombre")
    nombres.append(nombre)

nombres_orden=quick_sort(nombres)

print("lista de nombres ordenada")
for nombre in nombres_orden:
    print(nombre)
