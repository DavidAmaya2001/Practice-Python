print("=================================================")
print(" Calculadora con una sola variable de asignación ")
print("=================================================")

print("*************************************************")
print("*               Menu de Opciones                *")
print("*************************************************")
print("               1.      Suma                      ")
print("               2.      Resta                     ")
print("               3.  Multiplicación                ")
print("               4.     División                   ")
print("               5.  División Entera               ")
print("               6.     Exponente                  ")
print("               7.  Modulo o Resto                \n\n")

option = int(input("Introduce la opción deseada:\n" ))

if option == 1 : print(" Elegiste la opción de la Suma")
elif option == 2 : print("Elegiste la opción de la Resta")
elif option == 3 : print("Elegiste la opción de la Multiplicación")
elif option == 4 : print("Elegiste la opción de la División")
elif option == 5 : print("Elegiste la opción de la División Entera")
elif option == 6 : print("Eligiste la opción del Exponente")
elif option == 7 : print("Elegiste la opción del Modulo o Resto")

num1 = int(input("Introduce el primer numero: "))

if option == 1 : 
    num1 += int(input("Introduce el segundo numero a sumar: ")) 
    print("\nEl resultado de la suma es:", num1)

elif option == 2 : 
    num1 -= int(input("Introduce el segundo numero a restar: "))
    print("\nEl resultado de la resta es:", num1)

elif option == 3 : 
    num1 *= int(input("Introduce el segundo numero a multiplicar: "))
    print("\nEl resultado de la multiplicación es:", num1)

elif option == 4 : 
    num1 /= int(input("Introduce el segundo numero a dividir: "))
    print("\nEl resultado de la división es:", round(num1,2))

elif option == 5 : 
    num1 //= int(input("Introduce el segundo numero a dividir: "))
    print("\nEl resultado de la división (entera) es:", num1)

elif option == 6 : 
    num1 **= int(input("Introduce el segundo numero que será el exponente: "))
    print("\nEl resultado de la potenciación es es:", num1)

elif option == 7 : 
    num1 %= int(input("Introduce el segundo numero a dividir para obtener su resto: "))
    print("\nEl residuo de la divisón es:", num1)

