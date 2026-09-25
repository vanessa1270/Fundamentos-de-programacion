#REGISTRO A LA BIENVENIDA DE TECMILENIO

import csv #para leer y escribir el archivo de asistencia
import os #para verificar si el archivo ya existe antes de crearlo

print("Bienvenido a la fiesta de bienvenida de Tecmilenio")

# Nombre del archivo donde se guarda la info de los invitados
ARCHIVO = "asistencia.tecmilenio.csv"

# Verifica si el archivo existe y evita que se borren ejecuciones pasadas 
if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # CORRECCIÓN: Separamos los nombres de las columnas en elementos individuales
        writer.writerow(["NOMBRE", "EDAD", "PULSERA", "NOMBRE INV.", "EDAD INV.", "PULSERA INV."])

def nombre_alumno(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if nombre.isalpha():
            return nombre
        else:
            print("Error: Escribe un nombre válido (solo letras, sin números ni símbolos).")

def edad_alumno(mensaje):
    while True:
        try:
            edad = int(input(mensaje))
            if edad >= 17 and edad < 25:
                return edad
            else:
                print("La edad para asistir debe estar dentro del rango (17 a 24).")
        except ValueError:
            print("Ingresa un número entero válido.")

def registrar_datos():
    print("\tREGISTRO")

    nombre = nombre_alumno("Ingrese tu nombre: ")
    edad = edad_alumno("Ingrese tu edad: ")
    invitado = input("¿Vienes con algún invitado? (si/no): ").strip().lower()
    pulsera_alumno = "Roja" if edad >= 18 else "Azul"

    if invitado == "si":
        nombre_invitado = nombre_alumno("Ingrese el nombre del invitado: ")
        edad_invitado = edad_alumno("Ingrese la edad del invitado: ")
        pulsera_invitado = "Roja" if edad_invitado >= 18 else "Azul"
    else:
        nombre_invitado = "N/A"
        edad_invitado = "N/A"
        pulsera_invitado = "N/A"

    print(f"\nPulsera {pulsera_alumno} para alumno ({nombre})")
    if invitado == "si":
        print(f"Pulsera {pulsera_invitado} para invitado ({nombre_invitado})")

    # CORRECCIÓN: Se agrega newline="" y encoding="utf-8" para evitar saltos de línea vacíos
    with open(ARCHIVO, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([nombre, edad, pulsera_alumno, nombre_invitado, edad_invitado, pulsera_invitado])
        
    print("Registro guardado exitosamente en el archivo.")

def generar_reporte():
    print("\nREPORTES REGISTRADOS")
    if not os.path.exists(ARCHIVO):
        print("Aún no hay registros en el sistema.")
        return

    # Encabezados más claros que las columnas del CSV
    encabezados = ["ALUMNO", "EDAD", "PULSERA", "INVITADO", "EDAD INV.", "PULSERA INV."]

    with open(ARCHIVO, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # saltamos la fila de encabezado del CSV, ya imprimimos la nuestra

        # Ancho total = suma de columnas + separadores " | " (3 caracteres x 5 separadores)
        ancho_total = 15 + 8 + 10 + 15 + 10 + 12 + (3 * 5)

        print("-" * ancho_total)
        print(f"{encabezados[0]:<15} | {encabezados[1]:^8} | {encabezados[2]:^10} | {encabezados[3]:<15} | {encabezados[4]:^10} | {encabezados[5]:^12}")
        print("=" * ancho_total)

        hay_datos = False
        for fila in reader:
            if len(fila) == 6: #solo imprime 6 columnas completas
                hay_datos = True
                print(f"{fila[0]:<15} | {fila[1]:^8} | {fila[2]:^10} | {fila[3]:<15} | {fila[4]:^10} | {fila[5]:^12}")

        if not hay_datos:
            print("(sin registros todavía)".center(ancho_total))

        print("-" * ancho_total)
# Menú Principal
while True:
    print("\n¿Qué deseas hacer?")
    print("1. Registrarte")
    print("2. Ver reporte de registrados")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1-3): ").strip()
    
    if opcion == "1":
        registrar_datos()
    elif opcion == "2":
        generar_reporte()
    elif opcion == "3":
        print("\n¡Gracias por usar el sistema! Hasta luego.")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")