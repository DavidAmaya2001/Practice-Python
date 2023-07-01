# Concatenación de caracteres ---------------------------------------------------------------------------------

# metodo format()
print("\nMetodo format()")
nombre = "Carlos"
edad = 22

print("Hola {} tienes {} años.".format(nombre,edad))

print("Hola {nombre} tienes {edad} años.".format(nombre="Juan", edad = 40))

nombre = "Pedro"
edad = 36
print("Hola {0} tienes {1} años.".format(nombre,edad))


# metodo f-Strings
print("\nMetodo f-Strings")

print(f"El resultado de la suma 4 + 1 = {4+1}")

nombre = "El Pepe"
estatura = 1.8
edad = 22

print(f"Hola {nombre} tienes {edad} años y mides {estatura} metros.")

nombre = input("¿Cúal es tu nombre?: ")
num_1 = int(input("Introduce un numero: "))
num_2 = int(input("Introduce un segundo numero: "))

print(f"Hola {nombre} el resultado de {num_1} + {num_2} = {num_1 + num_2}")

