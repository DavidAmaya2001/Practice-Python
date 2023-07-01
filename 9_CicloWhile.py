# Ciclo While -----------------------------------------------------------------------------------------

#Ejemplo 1
x = 1

while x < 3:
    print(x)
    x += 1

print("Termino.")

#Ejemplo 2

x = 1
while x <= 5:
    print("Tilin")
    x += 1

print("Termino.")


# Ejercicio 
y = 0; x = 1
while y <= 1597:
    print(y,x,end=" ")          
    y += x
    x += y

# break y continue ------------------------------------------------------------------------------------

# Break
print("\n\nwhile con sentencia break\n")
contador = 0

while contador < 10:
    contador += 1
    if contador == 5:
        break
    print("Valor actual de la variable: ", contador)

print("Fin del programa, la sentencia break se ejecuto.")

# Continue

print("\nwhile con sentencia continue\n")
contador = 0

while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print("Valor actual de la variable: ", contador)

print("Fin del programa.")

