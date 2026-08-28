#REGISTRO A LA BIENVENIDA DE TECMILENIO
#Avance de Proyecto


print("Bienvenido a la fiesta de bienvenida de Tecmilenio")

nombre = input("\nIngrese tu nombre: ")
edad = int(input("Ingrese tu edad: "))
invitado = input("¿Vienes con algún invitado? (si/no): ")

if invitado == "si":
    nombre_invitado = input("Ingrese el nombre del invitado: ")
    edad_invitado = int(input("Ingrese la edad del invitado: "))
else: 
    nombre_invitado = None
    edad_invitado = None

if edad < 18 and edad_invitado < 18:
    print("Pulsera azul para invitado y para alumno tecmilenio")
elif edad < 18 and edad_invitado >= 18:
    print("Pulsera roja para invitado y pulsera azul para alumno tecmilenio")
elif edad >= 18 and edad_invitado < 18:
    print("Pulsera roja para invitado y pulsera azul para alumno tecmilenio")
else:
    print("Pulsera roja para invitado y pulsera roja para alumno tecmilenio")
