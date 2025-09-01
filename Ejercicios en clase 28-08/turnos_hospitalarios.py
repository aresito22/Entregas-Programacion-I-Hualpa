from utiles_es import pedir_texto

nombre_completo = pedir_texto("Nombre completo: ", permitir_vacio = False)
while " " not in nombre_completo:
    print("Debe ingresar su nombre completo.")
    nombre_completo = pedir_texto("Nombre completo: ", permitir_vacio = False)

dni = int(input("Ingrese su DNI (sin puntos): "))
while dni < 1000000 or dni > 100000000:
    print("DNI Invalido.")
    dni = int(input("Ingrese su DNI (sin puntos): "))

edad = int(input("Ingrese su edad: "))
while edad < 0:
    print("Edad inválida.")
    edad = int(input("Ingrese su edad: "))

tiene_obra = input("Tiene obra social? S/N: ")
tiene_obra = tiene_obra.upper()
while tiene_obra != "S" or tiene_obra != "N":
    tiene_obra = input("Respuesta inválida, ingrese S/N: ")

prioridades = ["1", "2", "3"]
print("Ingrese su prioridad médica:")
print("1 - Emergencia")
print("2 - Urgente")
print("3 - Control")
prioridad_medica = input()

while prioridad_medica not in prioridades:
    prioridad_medica = input("Respuesta inválida, ingrese 1/2/3: ")

if prioridad_medica == "1":
    print("Turno asignado inmediatamente - dirigase a la guardia.")
elif prioridad_medica == "2":
    if tiene_obra == "S":
        print("Turno en menos de 24 horas.")
    else:
        print("Turno en 48 horas.")
elif prioridad_medica == "3":
    if edad > 65:
        print("Turno preferencial en 72 horas.")
    else:
        print("Turno normal en 7 días.")