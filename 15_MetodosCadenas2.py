# Metodo swapcase() ----------------------------------------------------------------------------------------
# invierte todos los caracteres de una cadena (mayusculas -> minusculas) (minusculas -> mayusculas)

txtCadena = "TuTioElPollo"
print(txtCadena.swapcase())

txtCADENA = "TUTIOELPOLLO"
print(txtCADENA.swapcase())

txtcadena = "tutioelpollo"
print(txtcadena.swapcase())

txtnumber = "12345!-*"
print(txtnumber.swapcase())

print()
print(txtCadena)
print(txtCADENA)
print(txtcadena)
print(txtnumber)

# Metodo capitalize() ----------------------------------------------------------------------------------------
# convierte el primer caracter de la cadena en mayuscula y las demas en minusculas

string = "el ViaJe Es lA reComPenSa"
print(f"Antes de capitalize(): {string}")                    # -> el ViaJe Es lA reComPenSa

string = string.capitalize()
print(f"Despues de capitalize(): {string}" )                 # -> El viaje es la recompensa