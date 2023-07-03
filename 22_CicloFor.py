# Ciclo o Bucle for -------------------------------------------------------------------------------------------

# for <Variable> in <Objeto Iterable> :
# objeto iterable es aquel donde se pueden recorrer sus elementos uno a uno

string = "Hola"
for character in string:
    print( character )
print("Fin del programa")

# Ejercicio Practico 

string = input("Introduce un string para invertirlo ")
invert = ""

for caracter in string:
    invert = caracter + invert

print(f"String invertido: {invert}")