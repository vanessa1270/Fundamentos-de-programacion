#Variables de boletos
precio_bebe = 0.0
precio_menores = 30.0
precio_mayores = 45.0


#DESCUENTOS
descuento_adulto = 0.12
descuento_profesor = 0.10
descuento_estudiante = 0.10
descuento_ninguno = 0
total = 0.0
descuento = 0.0

print("\t========================================================")
print("\t==========SISTEMA DE COBRO, MUSEO ANTROPOLOGÍA==========")
print("\t========================================================")
#TABLA DE DESCUENTOS
print("\t==================TABLA DE PRECIOS======================")
print("\t|          PERSONAS            |    PRECIO    |")
print("\t|NIÑOS MENORES DE 3 AÑOS       |    $0.0      |")
print("\t|PERSONAS DE 3 A 17 AÑOS       |    $30.00    |")
print("\t|PERSONAS MAYORES DE 18 AÑOS   |    $45.00    |")



total_visitantes = int(input(f"\n¿Cuantas boletos necesitas?: "))

for i in range (total_visitantes):
    print(f"\n -------Visitante {i + 1}-------")

    edad = int(input("¿Cuántos años tiene el visitante?: "))

    if edad <3:
        precio_inicial = precio_bebe
    elif edad >=3 and edad <=17:
        precio_inicial = precio_menores
    else:
        precio_inicial = precio_mayores

    if edad < 3:
        descuento = descuento_ninguno
    else:
        visitante = input("Seleccione el tipo de visitante que registra: (A)Adulto mayor, (B)Profesor, (C)Estudiante: ")        
        if (visitante in ("Adulto mayor", "A")):
            descuento = descuento_adulto
        elif (visitante in ("Profesor", "B") ):
            descuento = descuento_estudiante
        elif (visitante in ("Estudiante", "C")):
            descuento = descuento_profesor
        else:
            print("Menores de 3 años, no paga")
            
        

    descuento_final = (precio_inicial * descuento)
    sub_total = (precio_inicial - descuento_final)
    total += sub_total

    print(f"Precio Inicial: ${precio_inicial:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}({int(descuento * 100)}%)")

print(f"Total a pagar por los visitantes ${total:.2f}")

