# Impresión de texto ---------------------------------------------------------------------------
print("Wasaaaaaaaaaaaaaa")

# Impresion de una suma de variables
x = 10
y = 20
z = x + y
print(z)  # 30

# Cadenas de caracteres ------------------------------------------------------------------------
 
# Asignación
mensaje = "hola"
mensaje += " "
mensaje += "Ernesto"
print("asignación: " + mensaje)   # hola Ernesto

# Concatenacion
mensaje = "hola"
espacio = " "
nombre = "Ernesto"
print("Concatenación: " + mensaje + espacio + nombre)   # hola Ernesto

numero_1 = 4
numero_2 = 6
resultado = numero_1 + numero_2
resultado = str(resultado)             # str -> Conversor de tipo numerico a string
print("Concatenación: " + resultado)   # 10

# Busqueda
mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto") 
buscar_subcadena = str(buscar_subcadena) 
print("Busqueda: " + buscar_subcadena)        # 5 (desde ese indice se encuentra la subcadena)

# Extracción
mensaje = "Hola Ernesto"
extraer_subcadena = mensaje[1:8]              # [a:b] extrae desde el indice a hasta b-1
print("Extracción: " + extraer_subcadena)     # ola Ern

# Comparación
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)             # True
mensaje_tres = "Wasa"
print(mensaje_uno == mensaje_tres)            # False

# Palabras reservadas
#  and  del  for  is  raise  assert  if else  elif  form  lambda  return  break  global  not
#  try  class  except  or  while  continue  exec  import  yield  def  finally  in  print

# Operadores Aritmeticos ------------------------------------------------------------------------------

# Suma
numero_1 = 5
numero_2 = 4
resultado = numero_1 + numero_2
print("El resultado de la suma es: " + str(resultado))

# Resta
resultado = numero_1 - numero_2
print("El resultado de la resta es: " +str(resultado))

# Multiplicación
resultado = numero_1 * numero_2
print("El resultado de la multiplicacion es: " + str(resultado))

# Potencia
resultado = numero_1 ** numero_2
print("El resultado de la potencia es: " + str(resultado))

# Division
resultado = numero_1 / numero_2
print("El resultado de la division es: " + str(resultado))

# Modulo o Residuo
resultado = numero_1 % numero_2
print("El resultado del residuo es: " + str(resultado))

# Division Entera (aunque tenga decimal no lo muestra)
resultado = numero_1 // numero_2
print("El resultado de la división entera es: " + str(resultado))

# Comentarios -------------------------------------------------------------------------------------------

# y "" para comentarios unilineas
""" Para comentarios multilineas """

# Tipos de Datos ----------------------------------------------------------------------------------------

""" Enteros, Largos (no tienen decimales y pueden ser positivos y negativos),
    Flotantes (tienen decimales y pueden ser positivos o negativos),
    Numeros complejos (tienen parte real e imaginaria),
    Cadenas (texto encerrado en '' o ""),
    Booleanos (tienen dos valores, true y false)
"""

# Entero o Largo
numero = 15
print(numero, type(numero))

# Flotante
numero_float = 15.25
print(numero_float, type(numero_float))

# Numero Complejo
numero_compl = 5 + 6j
print(numero_compl, type(numero_compl))

# Cadenas o String
caracter = 'cadena'
print(caracter, type(caracter))

# Booleano
boolean = 3 == 3    # Izquierda variable, derecha datos a comparar para devolver true o false
print(boolean, type(boolean))

# Entrada de Datos ----------------------------------------------------------------------------------------
palabra = input("Ingresa una cadena: ")
num_int = int(input("Introduce un numero entero: "))
num_float = float(input("Introduce un numero con decimal: "))
num_cmplx = complex(input("Introduce un numero complejo: "))

print("String" + palabra)
print("Entero: ", num_int)
print("Flotante: ", num_float)
print("Complejo: ", num_cmplx)

