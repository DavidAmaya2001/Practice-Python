# Metodos islower() lower() isupper() upper() ----------------------------------------------------------------------

# islower() y lower()
# verifica y convierte todas las letras de la cadena en minusculas

# isupper() y upper()
# verifica y convierte todas las letras de la cadena en mayusculas

variable = "TuTioElPollo"
print( variable.islower() )            # -> retorna (true o false) en este caso retorna false porque todas las letras no estan en minusculas
variable = variable.lower()            # -> retorna todas las letras de la caadena en minusculas ( tutioelpollo )
print(variable)
print( variable.isupper() )            # -> retorna (true o false) en este caso retorna false porque todas las letras no estan en mayusculas
variable = print(variable.upper())       # -> retorna todas las letras de la cadena en mayusculas ( TUTIOELPOLLO )