# Metodo count() -----------------------------------------------------------------------------------------
# cuenta la cantidad de veces que esta una subcadena dentro de una cadena

# con un argumento
string = "Hola mundo"
print(string.count(""))                     # -> 11 (lo recore como un index)

# recorrido:             0  1  2  3  4  5  6  7  8  9 10
#                        |H |o |l |a |  |m |u |n |d |o |
#                        1  2  3  4  5  6  7  8  9  10 11   = 11

string = "mi mamá me mima"
print(string.count("M"))                    # -> 0

print(string.count("m"))                    # -> 6

print(string.count("ma"))                   # -> 2   (dfierencia las tildes)

# con dos argumentos

string = "mi mamá me mima"                  # el segundo argumento indica que se empezara desde el caracter

print(string.count("m", 3))                 # -> 5
                                            
print(string.count("m", 8))                 # -> 3

print(string.count("m", 100))               # -> 0 (si el numero excede los caracteres que tiene el string, este se ira al ultimo index pero su valor siempre será 0)

print(string.count("m", -3))                # -> 1 (los numeros negativos hacen que se tome un recorrido de reversa desde la derecha del string)

# con tres argumentos

string = "mi mamá me mima"                  # el tercer argumento indica hasta donde dejara de contar los caracteres este metodo

print(string.count("m", 3, 7))              # -> 2 

print(string.count("m", 100, 100))          # -> 0 (si los numeros exceden los caracteres del string ambos se situaran en el ultimo index pero su valor siempre será 0)

print(string.count("m", -4, -1))            # -> 2 (los numeros negativos hacen que se tome un recorrido en reversa desde la derecha del string)

print(string.count("m", -4, -8))            # -> 0 (si el segundo numero es mayor al primero en terminos negativos entonces su valor siempre será 0)
