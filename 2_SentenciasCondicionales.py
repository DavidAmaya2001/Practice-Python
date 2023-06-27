# Sentencias condicinales simples -----------------------------------------------------------------
print("===========================================")
print("Sistema para calcular promedio de un alumno")
print("===========================================")
nombre = input("Ingresa tu nombre: ")
matematicas = float(input(nombre + ", ¿Cual es tu calificación en matemáticas?: "))
quimica = float(input(nombre + ", ¿Cual es tu calificación en quimica?: "))
biologia = float(input(nombre + ", ¿Cual es tu calificación en biología?: "))

promedio = (matematicas + quimica + biologia)/3

if promedio < 6 : print(nombre,"Has desaprobado tu ciclo escolar con un promedio de: ", round(promedio,2))
elif promedio >= 6 and promedio <=9.9 : print("Has aprobado tu ciclo escolar con un promedio de: ", round(promedio,2))
else : print("Has cursado perfectamente tu ciclo escolar con un promedio de: ", round(promedio,2))

print("Fin")

