# Operadores Relacionales --------------------------------------------------------------------------------

# Menor que          (a < b)
# Mayor que          (a > b)
# Igual a            (a == b)
# Diferente a        (a != b)
# Menor o igual que  (a <= b)
# Mayor o igual que  (a >= b)

print("Introduce dos numeros para comparar: ")

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

print("Los numeros a comparar son: ", num1, " y ",  num2)

if num1 != num2 and num1 > num2 : 
    print("Es diferente a...")
    print("Es mayor que...")
    print("Es mayor ao igual que..")

elif num1 != num2 and num1 < num2 :
    print("Es diferente a...")
    print("Es menor que...")
    print("Es menor o igual que...")

elif num1==num2 :
    print("Son iguales")
    print("Es mayor o igual que...")
    print("Es menor o igual que...")