# Actividad 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# Actividad 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Actividad 3
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Actividad 4
edad_categoria = int(input("Ingrese su edad para categorizarlo: "))
if edad_categoria < 12:
    print("Niño/a")
elif edad_categoria < 18:
    print("Adolescente")
elif edad_categoria < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Actividad 5
contrasena = input("Ingrese una contraseña (8 a 14 caracteres): ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

'''# Actividad 6
import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print("Lista de números:", numeros_aleatorios)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("No se puede determinar un sesgo claro con los valores obtenidos")'''

# Actividad 7
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# Actividad 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Capitalizado): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida.")
