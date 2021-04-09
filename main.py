"""
Ejercicio 3
Escribe un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar
el artículo y su precio por unidad. El artículo será la clave y el valor el precio, hasta que el usuario decida
terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
Artículo 1 Precio
Artículo 2 Precio
Artículo 3 Precio
. . . . . .
Total Precio Total
"""
cesta = {}
articulo = 0
while articulo != "x":
    articulo = str(input("Introduzca el artículo a añadir a la cesta, \"x\" para terminar: "))
    if articulo != "x":
        cesta[articulo] = float(input("Introduzca el precio de {}: ".format(articulo)))
    else:
        continue
cesta.items()
Total = 0
for key, value in cesta.items():
    print(key, "=", value)
    Total += value
print("")
print("Total precio cesta: {}".format(Total))