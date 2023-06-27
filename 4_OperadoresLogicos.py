# Operadores Logicos -------------------------------------------------------------------------------

# Conjunción ( Y )  -> and
# Disyunción ( o )  -> or
# Negación   ( no ) -> not

# Conjunción
print("Conjunción (and)")
num_uno = int(input("Escriba un numero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5 : 
    print("El numero ", num_uno, " cumple la condición.\n")

else:
    print("El numero ", num_uno, " NO cumple la condición.\n")


# Disyunción
print("Disyunción (or)")
palabra = input("Para cumplir la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido. \n")
    
else:
    print("La condición NO se ha cumplido")


# Negación
print("Negación (not)")
num_dos = int(input("Introduce un numero igual a 5: "))

if not num_dos == 5:
    print("El numero es diferente de cinco y SI cumple la condición.\n")

else:
    print("El numero es igual a cinco y NO cumple la condición.\n")