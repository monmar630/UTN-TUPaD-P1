#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")#Solo muestra este mensaje si su edad es mayor o igual a 18.

#Ejercicio 2
nota =  int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")#para notas mayores a 6
else:
    print("Desaprobado")#para notas menores a 6 

#Ejercicio 3
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:#si un numero es divisible por 2 sin resto significa que es par
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un nº par")

#Ejercicio 4
edad = int(input("Por favor, ingresa tu edad: "))

# Determinar la categoría
if edad < 12:
    print("Eres un/a Niño/a.")
elif edad >= 12 and edad < 18:
    print("Eres un/a Adolescente.")
elif edad >= 18 and edad < 30:
    print("Eres un/a Adulto/a joven.")
else:
    print("Eres un/a Adulto/a.")

#Ejercicio 5    
# Solicitar la contraseña al usuario    
contraseña = input("Ingrese una contraseña: ")

# Verifica la longitud de la contraseña
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Ejercicio 6
#Crear la lista de numeros aleatorios   
import random
from statistics import mode, median, mean

# Generar lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar el tipo de sesgo
if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

# Imprimir resultados
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Distribución: {sesgo}")

#Ejercicio 7
# Solicitar una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verificar si la última letra es una vocal
if texto[-1].lower() in "aeiou":
    texto += "!"

# Imprimir el resultado
print(texto)

#Ejecicio 8
# Solicitar el nombre y la opción al usuario
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese el número 1, 2 o 3 según la opción que prefiera:\n"
                   "1. Nombre en mayúsculas\n"
                   "2. Nombre en minúsculas\n"
                   "3. Nombre con la primera letra mayúscula\n"))

# Aplicar la transformación según la opción elegida
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")


#Ejercicio 9
# Solicitar la magnitud del terremoto al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificar la magnitud según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#Ejercicio 10
# Solicitar información al usuario
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

# Determinar la estación según el hemisferio
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido. Por favor, ingrese 'N' o 'S'."

# Imprimir el resultado
print(f"La estación en la que se encuentra es: {estacion}")











