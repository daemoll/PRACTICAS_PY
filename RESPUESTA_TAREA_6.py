"""Ejercicio 1
Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
sean desde el número 1 hasta el número indicado. Los valores de cada clave serán las propias claves elevadas
al cubo."""
num = int(input("Introduzca un número entero para hacer el diccionario: "))
dicc = {}
for i in range(num):
    dicc[i + 1] = (i + 1) ** 3
print(dicc)


###################################################################################################

"""
Ejercicio 2
Escribe un programa que pregunte al usuario su nombre, edad y teléfono y lo guarde en un diccionario.
Después, debe mostrar por pantalla el mensaje ‘{nombre} tiene {edad} años y su número de teléfono es
{teléfono}."""
dicc = {"Nombre": 0, "Edad": 0, "Telefono": 0}
dicc["Nombre"] = str(input("Escriba su nombre: "))
dicc["Edad"] = int(input("Introduzca su edad: "))
dicc["Telefono"] = int(input("Introduzca su número de teléfono: "))
print("{} tiene {} años y su número de teléfono es {}.".format(dicc["Nombre"], dicc["Edad"], dicc["Telefono"]))


####################################################################################################
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

###################################################################################################

"""
Ejercicio 4
Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
cantidad números positivos y negativos introducidos.
"""
numeros = {}
control = 1
n_negativos = 0
n_positivos = 0
while control != 0:
    control = int(input("Introduzca un número entero, \"0\" para terminar: "))
    if control != 0:
        if control < 0:
            n_negativos += 1
            numeros["numeros_negativos"] = n_negativos
        else:
            n_positivos += 1
            numeros["numeros_positivos"] = n_positivos
    else:
        continue
numeros.items()
for key, value in numeros.items():
    print(key, "=", value)
print(numeros)
print(numeros.items())

####################################################################################
"""
Ejercicio 5
Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
cantidad números pares e impares introducidos.
"""
numeros = {}
control = 1
n_par = 0
n_impar = 0
while control != 0:
    control = int(input("Introduzca un número entero, \"0\" para terminar: "))
    if control != 0:
        if control % 2 == 0:
            n_par += 1
            numeros["numeros_pares"] = n_par
        else:
            n_impar += 1
            numeros["numeros_impares"] = n_impar
    else:
        continue
numeros.items()

for key, value in numeros.items():
    print(key, "=", value)
print(numeros)
print(numeros.items())


###################################################################################

"""
Ejercicio 6
Crea un programa que permita al usuario introducir los nombres de los alumnos de una clase y las notas que
han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario
cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
1
El programa va a pedir el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus
notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos
y la nota media obtenida por cada uno de ellos.
PISTA: Vas a necesitar la función sum().##
"""
n_alumnos = int(input("Introduzca el número de alumnos de la clase: "))
alum_clase = []
n_media = {}
alumnos = {}
dicc_nmedia = {}
for i in range(n_alumnos):
    alum_clase.append(str(input("Introduzca nombre del alumno numero {}: ".format(i + 1))))
for key in range(len(alum_clase)):
    asignatura = "0"
    asig_nota = []
    while asignatura != "-1":
        asignatura = str(input("Introduzca asignatura del alumno {}, o escriba \"-1\" para seguir: ".format(alum_clase[key])))
        if asignatura != "-1":
            nota = float(input("Introduaca las nota que ha obtenido el alumno {} en la asignatura {}: ".format(alum_clase[key], asignatura)))
            asig_nota.append([asignatura, nota])
            print(asig_nota)
        else:
            continue
    alumnos[key] = dict(asig_nota)
for j in alumnos:
    suma = 0
    for k in alumnos[j]:
        suma = sum(alumnos[j].values())
    nota_media = suma / (len(alumnos[j]))
    n_media = {alum_clase[j]: nota_media}
    dicc_nmedia.update(n_media)
dicc_nmedia.items()
print("")
for key, value in dicc_nmedia.items():
    print("La nota media del alumno", key, "es de: ", value)

####################################################################


"""
Ejercicio 7
Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
sean desde el número 1 hasta el número indicado. Los valores de cada clave serán tantos símbolos "*" como
indique la clave.
"""
num = int(input("Introduzca un valor entero positivo: "))
dicc_temp = {}
dicc = {}

for i in range(num):
    clave = i + 1
    valor = str("*" * (i + 1))
    dicc_temp = {clave: valor}
    dicc.update(dicc_temp)
print(dicc)


#########################################################################

"""
Ejercicio 8
Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
de valor la longitud de dicha palabra.
"""
num_palabras = int(input("Introduzca el numero de palabras para el dicconario: "))
dicc_temp = {}
diccionario = {}
for i in range(num_palabras):
    palabra = str(input("Introduzca la palabra {} de {}: ".format(i + 1, num_palabras)))
    long = int(len(palabra))
    dicc_temp = {palabra: long}
    diccionario.update(dicc_temp)
print(diccionario)


###########################################################################


"""
Ejercicio 9
Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
de valor el número de vocales de la palabra.
"""
num_palabras = int(input("Introduzca el numero de palabras para el dicconario: "))
dicc_temp = {}
diccionario = {}
for i in range(num_palabras):
    PALABRA = str(input("Introduzca la palabra {} de {}: ".format(i + 1, num_palabras)))
    palabra = PALABRA.lower()
    plbr = []
    for j in palabra:
        if j != "a" and j != "e" and j != "i" and j != "o" and j != "u" and j!= " ":
            plbr.append([j])
        else:
            continue
        long = int(len(plbr))
        dicc_temp = {PALABRA: long}
        diccionario.update(dicc_temp)
print(diccionario)

####################################################################################

"""
Ejercicio 10
Dada una matriz, crea un diccionario que guarde el número de filas, el de columnas y cada fila en una entrada
de un diccionario
"""
import numpy as np
m1 = int(input("Inserte la dimensión m (filas) de una matriz m x n: "))
n1 = int(input("Inserte la dimensión n (columnas) de una matriz m x n: "))
matriz = np.empty((m1, n1))
dic_temp = {}
diccionario = {}
for i in range(m1):
    for j in range(n1):
        matriz[i][j] = float(input("Inserte el valor {},{} de la matriz: ".format(i + 1, j + 1)))
print(matriz)
filas =  []
for k in range(len(matriz)):
    filas.append(matriz[k])
    dic_temp = {"n_filas": m1, "n_columnas": n1, "fila": filas}
    diccionario.update(dic_temp)
print(diccionario)