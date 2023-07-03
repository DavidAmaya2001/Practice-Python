# Metodos de formato de alineación ----------------------------------------------------------------------------------------

# Metodo center()
# centra un string añadiendo espacios o caracteres segun le indiquemos tanto al inicio como al final del string para finalmente mostrar el mismo string
# (primer argumento) se indicara un int de valor mayor a la longitud del string de la variable
# (segundo argumento) se indicara UN SOLO caracter entre comillas

string = "menú"
string.center(10)                     # .center(10)        ->  1 2 3 m e n ú 8 9 10  (los numeros son espacios en blanco)

string = string.center(10, "=")       # .center(10, "=")   ->  = = = m e n ú = = =
print(string)

# Metodo ljust() (justificado a la izquierda)
# alinea el string a la izquierda con espacios o caracteres segun se indique en el argumento del metodo

string = "menú"
string.ljust(10)                      # .ljust(10)         -> m e n ú 5 6 7 8 9 10   (los numeros son espacios en blanco)

string = string.ljust(10, "=")        # .ljust(10, "=")    -> m e n ú = = = = = =
print(string)

# Metodo rjust() (justificado a la derecha)
# alinea el string a la derecha con espacios o caracteres segun se indique en el argumento del metodo

string = "menú"
string.rjust(10)                      # .rjust(10)         -> 1 2 3 4 5 6 m e n ú   (los numeros son espacios en blanco)

string = string.rjust(10, "=")        # .rjust(10, "=")    -> = = = = = = m e n ú
print(string)