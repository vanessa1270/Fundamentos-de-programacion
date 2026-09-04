

def tabla_pitagoras(n):
    tabla = []

    for fila in range(1, n + 1):
        renglon = []

        for columna in range(1, n + 1):
            producto = 0

            for i in range(columna):
                producto = producto + fila

            renglon.append(producto)
        tabla.append(renglon)
    return tabla

def imprimir_tabla(tabla):
    n = len(tabla)
    print("X", end="\t")

    for i in range(1, n + 1):
        print(i, end="\t")
    print()
    for i, fila in enumerate(tabla, start=1):
        print(i, end="\t")
        
        for elemento in fila:
            print(elemento, end="\t")
        print()

def consultar_tabla(tabla, renglon, columna):
    resultado = tabla[renglon - 1][columna - 1]
    return resultado

tamaño = 10

tabla = tabla_pitagoras(tamaño)

print("Tabla de Pitágoras")
imprimir_tabla(tabla)

renglon = int(input("Ingrese el número de fila: "))
columna = int(input("Ingrese el número de columna: "))

resultado = consultar_tabla(tabla, renglon, columna)
print(f"El resultado de la multiplicación en la fila {renglon} y columna {columna} es: {resultado}")



