# Substrings ------------------------------------------------------------------------------------------------

# variable[ inicio : final : saltos]
# Inicio: establece al indice donde se iniciará la subcadena
# final:  establece al indice donde se terminará la subcadena
# saltos: establece el numero de saltos que realizará el indice para generar la subcadena

string = "0123456789"
string[0]                              # son un solo elemento para substring solo retornara un caracter -> "0"
string[5]                              # -> 5
string[-4]                             # -> 6 (en negativos toma el siguiente indice del indicado de derecha a izquierda de la cadena)

string[0:3]                            # con dos elementos para substring retornara un rango de elementos entre el rango a: b -> "012"
string[:3]                             # si no se indica posicion inicial se toma por default en 0 -> "012"
string[5:]                             # si no se indica posicion final se toma por default en el ultimo de la cadena -> "56789"
string[-4:-1]                          # -> "678"
string[:]                              # comienza por defecto en 0 y por defecto posiciona al final -> "0123456789"

string[1:6:2]                          # con tres elementospara substring indicara inicio, final y saltos de indices ->"135"
string[::3]                            # comienza de inicio a final por default pero saltando de 3 en 3 en indices -> "0369"
