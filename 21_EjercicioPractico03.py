# Ejercicio practico con Substring ------------------------------------------------------------------------

string = input("Ingrese una frase: ")
substring = input("Ingrese la palabra a eliminar: ")

newstring = ""
indicesub = string.find(substring)

longitudsub = len(substring)

newstring = string[0: indicesub] + string[indicesub + longitudsub :]

print(newstring)
        


