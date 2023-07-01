# Metodos de Cadenas -----------------------------------------------------------------------------

# Metodo strip()
# Elimina caracteres especificos o espacios en blanco al inicio y final de la cadena

cadena = " Hola Ernesto "
cadena = cadena.strip("s tHo")  # -> Verifica cada caracter en strip de izquierda a derecha y si la cadena lo contiene al inicio o al final los elimina en orden y repite el proceso
                                # -> caracter "s" a verificar primero                   " Hola Ernesto "
                                # -> caracter " " a verificar segundo                   "Hola Ernesto"
                                # -> caracter "s" a verificar tercero (repite)          "Hola Ernesto"
                                # -> caracter " " a verificar cuarto  (repite)          "Hola Ernesto"
                                # -> caracter "t" a verificar quinto                    "Hola Ernesto"
                                # -> caracter "H" a verificar sexto                     "ola Ernesto"
                                # -> caracter "s" a verificar septimo (repite)          "ola Ernesto"
                                # -> caracter " " a verificar octavo  (repite)          "ola Ernesto"
                                # -> caracter "t" a verificar noveno  (repite)          "ola Ernesto"
                                # -> caracter "H" a verificar decimo  (repite)          "ola Ernesto"
                                # -> caracter "o" a verificar decimo primero            "la Ernest"
                                # -> caracter "s" a verificar decimo segundo (repite)   "la Ernest"
                                # -> caracter " " a verificar decimo tercero (repite)   "la Ernest"
                                # -> caracter "t" a verificar decimo cuarto  (repite)   "la Ernes"
                                # -> caracter "s" a verificar decimo quinto  (repite)   "la Erne"
                                # -> caracter "s" a verificar decimo sexto   (repite)   "la Erne"
                                # -> caracter " " a verificar decimo septimo (repite)   "la Erne"
                                # -> caracter "t" a verificar decimo octavo  (repite)   "la Erne"
                                # -> caracter "H" a verificar decimo noveno  (repite)   "la Erne"
                                # -> caracter "o" a verificar vigesimo                  "la Erne"
                                # -> repite todo y no elimina nada mas porque no hay similitud de caracter
print(cadena) 

# Metodo rstrip()
# Elimina unicamente caracteres especificados al final de una cadena (right)

cadena = " Hola Ernesto "
cadena = cadena.rstrip(" oH")   # -> Verifica cada caracter en rstrip de izquierda a derecha y si la cadena lo contiene al inicio o al final los elimina en orden y repite el proceso
                                # -> caracter " " a verificar primero                   " Hola Ernesto"
                                # -> caracter " " a verificar segundo (repite)          " Hola Ernesto"
                                # -> caracter "o" a verificar tercero                   " Hola Ernest"
                                # -> caracter " " a verificar cuarto  (repite)          " Hola Ernest"
                                # -> caracter "o" a verificar quinto  (repite)          " Hola Ernest"
                                # -> caracter "H" a verificar sexto                     " Hola Ernest"
print(cadena)

# Metodo lstrip()
# Elimina unicamente caracteres especificados al inicio de una cadena (left)

cadena = " Hola Ernesto "
cadena = cadena.lstrip(" oH")   # -> Verifica cada caracter en lstrip de izquierda a derecha y si la cadena lo contiene al inicio o al final los elimina en orden y repite el proceso
                                # -> caracter " " a verificar primero                   "Hola Ernesto "
                                # -> caracter " " a verificar segundo (repite)          "Hola Ernesto "
                                # -> caracter "o" a verificar tercero                   "Hola Ernesto "
                                # -> caracter "H" a verificar cuarto                    "ola Ernesto "
                                # -> caracter " " a verificar quinto  (repite)          "ola Ernesto "
                                # -> caracter "o" a verificar sexto   (repite)          "la Ernesto "
                                # -> repite todo y no elimina nada mas porque no hay similitud de caracter
print(cadena)