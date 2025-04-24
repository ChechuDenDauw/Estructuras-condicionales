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