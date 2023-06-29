print("====================================")
print(" Sistema Vacaciones por Departamento")
print("====================================")

print("Ingrese los siguientes datos solicitados antes de continuar")
name = input("¿Cual es su nombre?: ")

print("Ingrese Clave del departamento segun usted se encuentre: \n")
print("(Clave 1) Departamento de Atención al cliente")
print("(Clave 2) Departamento de Logistica")
print("(Clave 3) Gerencia\n")
key = int(input("Ingrese la clave de su departamento: "))

years = int(input("¿Cuantos años lleva trabajando dentro de la empresa?: "))

#Variable que almacena vacaciones
vacationDays = 0

if key == 1 :
    if years == 1 :
        vacationDays = 6
    elif years >= 2 and years <= 6 :
        vacationDays = 14
    elif years >= 7 :
        vacationDays = 20
    else:
        vacationDays = 0

elif key == 2 :
    if years == 1 :
        vacationDays = 7
    elif years >= 2 and years <= 6 :
        vacationDays = 15
    elif years >= 7 :
        vacationDays = 22   
    else:
        vacationDays = 0

elif key == 3 :
    if years == 1 :
        vacationDays = 10
    elif years >= 2 and years <= 6 :
        vacationDays = 20
    elif years >= 7 :
        vacationDays = 30
    else:
        vacationDays = 0

else:
    print("Error de departamento ingresado")


if vacationDays != 0 :
    print("Al trabajador de nombre:", name , " del departamento:", key , "con:", years , "años de trabajo, le corresponden:", vacationDays, " días de vacaciones")

else:
    print("Al trabajador de nombre:", name , " del departamento:", key , "con:", years , "años de trabajo, no le corresponden dias de vacaciones")
