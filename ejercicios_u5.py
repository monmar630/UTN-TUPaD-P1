#Ejercicio 1
#Función que imprima saludo por pantalla
def imprimir_Hola_mundo():
    print ("Hola Mundo!")


#Programa principal
imprimir_Hola_mundo()

#Ejercicio 2
#Función que imprima en pantalla saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Programa principal
nombre = input("Cómo es tu nombre? ")
saludo = saludar_usuario(nombre)
print(saludo)

#Ejercicio 3
#Función que reciba 4 parámetros
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa principal
nombre = input("Cómo es tu nombre? ") 
apellido = input("Cómo es tu apellido? ") 
edad = int(input("Cuántos años tenés? "))
residencia = input("Dónde vivís? ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
#Función area y función perímetro
import math
def calcular_area_circulo(radio):
    return math.pi *(radio**2)

def calcular_perimetro_circulo(radio):
    return 2* math.pi * radio

#Programa principal
radio = float(input("Ingrese el radio del círculo: "))

area =  calcular_area_circulo (radio)
perimetro = calcular_perimetro_circulo(radio)


print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#Ejercicio 5
#Función segundo a horas
def segundos_a_horas(segundos):
    return segundos / 3600

#Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)


print(f"{segundos} segundos son equivalentes a {horas:.2f} horas")


#Ejercicio 6
#Función tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")


#Programa principal 
numero = int(input("Ingrese un número: "))

tabla_multiplicar(numero)


#Ejercicio 7
#Función operaciones
def operaciones_basicas(a, b):
    if b == 0:
        return (a + b, a - b, a * b, "No se puede dividir por cero")
    else:
        return (a + b, a - b, a * b, a / b)
    
#Programa principal
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print(f"Resustados de las operaciones básicas:")
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicación: {a} * {b} = {multiplicacion}")

if isinstance(division, str):
    print("División: {division}")
else:
    print(f"División: {a} / {b} = {division:.2f} ")
    


#Ejercicio 8
#Función Indice de masa muscular
def calcular_imc(peso, altura):
    if altura == 0:
        return "No se puede calcular el IMC con altura cero"
    else: 
        return peso / (altura ** 2)
    
# Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

if isinstance(imc, str):
    print(imc)
else:
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")


#Ejercicio 9
#Función para convertir Celsius a Fahrenhiet
def celsius_a_fahrenheit(celsius):
    #Fórmula para convertir Celsius a Fahrenhiet
    fahrenhiet = (celsius * 9/5) + 32
    #Devolver el resultado
    return fahrenhiet

#Programa principal
#Pedir al usuario que ingrese una temperatura en Celsius
celsius = float(input("Ingrese la temperatura en Celsius: "))

#Llamar a la función para convertir Celsius a Fahrenheit
fahrenheit = celsius_a_fahrenheit (celsius)

#Mostrar el resultado
print(f"{celsius}ºC es equivalente a {fahrenheit}ºF")



#Ejercicio 10
#Función para calcular el promedio de tres números
def calcular_promedio(a, b, c):
    #Calcular promedio
    promedio = (a + b + c)/3
    #Devolver el rdo.
    return promedio

#Programa principal
#Pedir al usuario que ingrese tres números
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

#Llamar a la función para calcular el promedio
promedio = calcular_promedio(a, b, c)

#Mostrar el resultado
print(f"El promedio de {a}, {b} y {c}es: {promedio}")








