# Metodo startswith() y endswith() -----------------------------------------------------------------------------

# Metodo startswith()
# se utiliza para comprobar si una cadena inicia con una subcadena en concreto (tiene una funcionalidad similar a los Metodos count())

string = "Diana se peina sola"                            # Con un solo argumento (retorna True or False)
string.startswith("D")                                    # -> true (porque la cadena inicia con la subcadena indicada)
string.startswith("d")                                    # -> false (porque la cadena inicia con la subcadena pero en minuscula)
string.startswith("Diana")                                # -> true (porque la cadena inicia con la subcadena indicada)

string = "Diana se peina sola"                            # con dos argumentos verifica desde la posicion asignada
string.startswith("se", 6)                                # -> true (porque la cadena desde donde se indico su inicio del recorrido inicia con la subcadena indicada)

string = "Diana se peina sola"                            # con tres argumentos cerifica dentro del rango asignado con ambos numeros
string.startswith("se", 6, 7)                             # -> false (porque se ha dedicado el analizar menos rango que la subcadena indicada y al no cumplir retorna false)
string.startswith("se", -4, -1)                           # -> false (en este caso se comienza a tomar desde el extremo izquierdo y no cumple con la subcadena indicada)


# Metodo endswith()
# se utiliza para comprobar si una cadena de caracteres termina con una subcadena en concreto (tiene una funcionalidad similar a los Metodos count())

string = "Diana se peina sola"                            # Con un solo argumento (retorna True or False)
string.endswith("a")                                      # -> true (porque la cadena termina con la subcadena indicada)
string.endswith("sola")                                   # -> true (porque la cadena termina con la subcadena indicada)

string = "Diana se peina sola"                            # con dos o tres argumentos sucede lo mismo que con el metodo startswith()
string.endswith("s", 9, 14)                               # -> false (porque en el rango establecido no termina con la subcadena indicada)
string.endswith("s", -4, -2)                              # -> false (aunque sean negativos pero si se usa endwith tendrá la misma ubicacion que colocarlos con numeros positivos)
