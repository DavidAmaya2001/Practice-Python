# Metodos istitle() y title() ---------------------------------------------------------------------------------

# Metodo istitle()
# verifica si en una cadena de caracteres cada palabra comienza con mayusculas y las demas sean minusculas (por cada palabra de la cadena), retorna true or false

nombre = "CarloS gallardo"
print(nombre.istitle())       # -> false (no cumple con mayusculas al inicio de las palabras y minusculas las demas)
nombre = nombre.title()       # lo modifica
print(nombre)                 # -> Carlos Gallardo

# Metodo title()
# Verifica si en una cadena de caracteres cada palabra comienza con mayusculas y las demas sean minusculas (por cada palabra de la cadena), retorna una corrección de esta cadena si la necesitara

nombre = "CarloS gallardo"
print(nombre.title())         # -> Solo imprime el .title() Carlos Gallardo pero no modifica el valor de la variable
print(nombre)                 # -> CarloS gallardo


# Ejemplo
first_name = input("Nombre: ")
last_name = input("Apellido: ")
full_name = f"{first_name} {last_name}"

print()
print(f"¿El formato del metodo title() se ha aplicado?: {full_name.istitle()}")
print(f"Aplicando el metodo title(): {full_name.title()}")
print(f"Volvemos a imprimir el nombre: {full_name}")