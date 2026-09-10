#Menu modular

def sumar_elementos(tupla_numeros):
    return sum(tupla_numeros)

def tupla_ordenada():
    print("\nSECCIÓN TUPLAS")
    numeros = (10, 25, 5, 40, 15)
    print(f"Tupla inicial: {numeros}")
    print(f"Tercer elemento de la tupla: {numeros[2]}")

    try: 
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        nueva_tupla = numeros + (num1, num2)
        print(f"Nueva tupla: {nueva_tupla}")
        lista_ordenada = list(nueva_tupla)
        lista_ordenada.sort()
        print(f"Lista ordenada de elementos: {lista_ordenada}")
        suma_total = sumar_elementos(nueva_tupla)
        print(f"La suma total de los elemntos es: {suma_total}")
    except:
        print("Error inesperado")

def buscar_telefono(contactos, nombre):
    return contactos.get(nombre)

def seccion_contactos():
    print("\nCONTACTOS")

    agenda = {
        "Ana": "555-0101",
        "Luis": "555-0102",
        "Mía": "555-0103"
    }

    nuevo = input("Ingresa el nombre del nuevo contacto: ")
    tel = input("Ingresa el télefono del nuevo contacto: ")
    agenda[nuevo] = tel
    print("Contacto guardado con éxito!")
    for clave in agenda.keys():
        print(f"- {clave}")

    nombre = input("\nIngresa el nombre del contacto a buscar:")
    telefono = buscar_telefono(agenda, nombre)

    if telefono:
        print(f"El telefono de {nombre} es: {telefono}")
    else:
        print("No existe el contacto")

def sumar_numeros():
    try:
        num1 = int(input("Ingresa un número entero: "))
        num2 = int(input("Ingresa un número entero: "))
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es: {suma}")
        division = num1 / num2
        print(f"La división de {num1} entre {num2} es: {division}")
    except ValueError:
        print("Error: Debes ingresar un número entero.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print()

def conteo_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def conteo_frase():
    frase = input("Ingresa una frase: ")
    print(f"Longitud de la frase: {len(frase)} caracteres")

    print(f"En mayúsculas: {frase.upper()}")

    palabra_original = input("Palabra que desea remplazar: ")
    palabra_remplazada = input("La nuecva palabra es: ")
    mensaje_modificado = frase.replace(palabra_original, palabra_remplazada)
    print(f"Mensaje remplazado: {mensaje_modificado}")
    total_palabras = conteo_palabras(frase)
    print(f"El mensaje contiene {total_palabras} palabras.")


while True:
    print("\t------Menú principal------")
    print("\t1. Mostrar tupla ordenada")
    print("\t2. Buscar télefono en contactos")
    print("\t3. Dividir dos números ")
    print("\t4. Analizar frase")
    print("\t5. Salir del programa")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        tupla_ordenada()
    elif opcion == "2":
        seccion_contactos()
    elif opcion == "3":
        sumar_numeros()
    elif opcion == "4":
        conteo_frase()
    elif opcion == "5":
        print("Programa finalizado")
        break
    else:
        print("Elige una opción válida del 1 al 5")






