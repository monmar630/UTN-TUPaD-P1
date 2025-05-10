#Ejercicio 1
# Crear la lista con números múltiplos de 4
lista_multiplos_de_4 = list(range(4, 101, 4))

# Mostrar la lista
print(lista_multiplos_de_4)


#Ejercicio 2
# Crear una lista con cinco elementos
lista_favoritos = ["Python", "Café", "Música", "Viajes", "Libros"]

# Mostrar el penúltimo elemento
print(lista_favoritos[-2])


#Ejercicio 3
# Crear una lista vacía
lista_vacia = []

# Agregar tres palabras con append
lista_vacia.append("Sol")
lista_vacia.append("Luna")
lista_vacia.append("Estrellas")

# Imprimir la lista resultante
print(lista_vacia)


#Ejercicio 4
# Lista original
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo elemento (índice 1) con "loro"
animales[1] = "loro"

# Reemplazar el último elemento (índice -1) con "oso"
animales[-1] = "oso"

# Imprimir la lista resultante
print(animales)

#Ejercicio 5
# Lista original
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo elemento (índice 1) con "loro"
animales[1] = "loro"

# Reemplazar el último elemento (índice -1) con "oso"
animales[-1] = "oso"

# Imprimir la lista resultante
print(animales)


#Ejercicio 6
# Crear la lista con números del 10 al 30 con saltos de 5 en 5
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print(numeros[:2])


#Ejercicio 7
# Lista original
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores centrales
autos[1:3] = ["mustang", "corolla"]

# Imprimir la lista resultante
print(autos)


#Ejercicio 8
# Crear una lista vacía
dobles = []

# Agregar el doble de 5, 10 y 15 usando append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print(dobles)


#Ejercicio 9
# Lista original de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
indice_fideos = compras[1].index("fideos")  # Encontrar la posición de "fideos"
compras[1][indice_fideos] = "tallarines"  # Reemplazar por "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)

#Ejercicio 10
# Crear la lista anidada con los valores requeridos
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Imprimir la lista resultante
print(lista_anidada)
