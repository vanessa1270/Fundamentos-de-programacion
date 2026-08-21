# Actividad 2 - Cobro de Entradas del Museo

total_general = 0

# 1. Capturar la cantidad total de visitantes
total_visitantes = int(input("¿Cuántos visitantes se van a registrar?: "))

# 2. Ciclo para procesar cada visitante
for i in range(total_visitantes):
    print(f"\n--- Visitante {i + 1} ---")
    
    edad = int(input("Ingrese la edad: "))
    
    # Manejo de entrada inválida con 'continue'
    if edad < 0:
        print("Edad no válida. Se salta este visitante.")
        continue

    # Determinar precio base según la edad
    if edad < 3:
        precio_base = 0
    elif edad <= 17:
        precio_base = 30
    else:
        precio_base = 45

    # Aplicar descuento único (Tabla de verdad)
    descuento = 0
    
    if edad >= 18:
        print("Tipos de visitante: [1] Adulto mayor | [2] Profesor | [3] Estudiante | [4] Ninguno")
        tipo = input("Seleccione una opción: ")
        
        if tipo == "1":
            descuento = 0.12  # Adulto mayor 12%
        elif tipo == "2":
            descuento = 0.10  # Profesor 10%
        elif tipo == "3":
            descuento = 0.10  # Estudiante 10%
            
    elif 3 <= edad <= 17:
        es_estudiante = input("¿Es estudiante? (s/n): ").lower()
        if es_estudiante == 's':
            descuento = 0.10  # Estudiante 10%

    # Opción para cancelar el registro usando 'break'
    cancelar = input("¿Desea cancelar el resto del registro? (s/n): ").lower()
    if cancelar == 's':
        print("Cancelando el proceso...")
        break

    # Cálculo y acumulador
    pago_final = precio_base * (1 - descuento)
    total_general += pago_final

    # Despliegue individual
    print(f"Precio base: ${precio_base}")
    print(f"Descuento: {descuento * 100}%")
    print(f"Total a pagar por este boleto: ${pago_final:.2f}")

# 3. Total detallado global
print("\n=================================")
print(f"TOTAL A PAGAR DE TODOS LOS BOLETOS: ${total_general:.2f}")
print("=================================")