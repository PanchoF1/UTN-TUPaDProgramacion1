lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre del operador (solo letras): ")
while not operador.isalpha():
    operador = input("Error. Ingrese nombre del operador (solo letras): ")

opcion = ""
while opcion != "5":
    print(f"\n--- SISTEMA DE TURNOS - Operador: {operador} ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Día inválido. Elegir día (1=Lunes, 2=Martes): ")
        
        paciente = input("Nombre del paciente (solo letras): ")
        while not paciente.isalpha():
            paciente = input("Error. Nombre del paciente (solo letras): ")

        if dia == "1":
            # Verificar repetido
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: El paciente ya tiene un turno este día.")
            # Guardar en primer espacio libre
            elif lunes1 == "": lunes1 = paciente
            elif lunes2 == "": lunes2 = paciente
            elif lunes3 == "": lunes3 = paciente
            elif lunes4 == "": lunes4 = paciente
            else: print("No hay turnos disponibles para el Lunes.")
        
        else: # Martes
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: El paciente ya tiene un turno este día.")
            elif martes1 == "": martes1 = paciente
            elif martes2 == "": martes2 = paciente
            elif martes3 == "": martes3 = paciente
            else: print("No hay turnos disponibles para el Martes.")

    elif opcion == "2":
        dia = input("Elegir día de la cancelación (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente a cancelar: ")
        
        encontrado = False
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""; encontrado = True
            elif lunes2 == paciente: lunes2 = ""; encontrado = True
            elif lunes3 == paciente: lunes3 = ""; encontrado = True
            elif lunes4 == paciente: lunes4 = ""; encontrado = True
        else:
            if martes1 == paciente: martes1 = ""; encontrado = True
            elif martes2 == paciente: martes2 = ""; encontrado = True
            elif martes3 == paciente: martes3 = ""; encontrado = True
        
        if encontrado:
            print("Turno cancelado exitosamente.")
        else:
            print("No se encontró al paciente en ese día.")

    elif opcion == "3":
        dia = input("Ver agenda de (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == "4":
        occ_lunes = 0
        if lunes1 != "": occ_lunes += 1
        if lunes2 != "": occ_lunes += 1
        if lunes3 != "": occ_lunes += 1
        if lunes4 != "": occ_lunes += 1
        
        occ_martes = 0
        if martes1 != "": occ_martes += 1
        if martes2 != "": occ_martes += 1
        if martes3 != "": occ_martes += 1

        print(f"\nLunes: {occ_lunes} ocupados, {4 - occ_lunes} disponibles.")
        print(f"Martes: {occ_martes} ocupados, {3 - occ_martes} disponibles.")

        if occ_lunes > occ_martes:
            print("El día con más turnos es: Lunes")
        elif occ_martes > occ_lunes:
            print("El día con más turnos es: Martes")
        else:
            print("Empate en cantidad de turnos entre Lunes y Martes.")

    elif opcion == "5":
        print("Saliendo del sistema...")
    else:
        print("Opción no válida.")