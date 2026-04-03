energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidos = 0
bloqueo_sistema = False

nombre_agente = input("Ingrese nombre del agente (solo letras): ")
while not nombre_agente.isalpha():
    nombre_agente = input("Error. Ingrese un nombre válido (solo letras): ")

print(f"\n--- Bienvenido Agente {nombre_agente} a 'La Bóveda' ---")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo_sistema:
    
    if alarma == True and tiempo <= 3:
        bloqueo_sistema = True
        break

    print(f"\nESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ON' if alarma else 'OFF'} | Código: [{codigo_parcial}]")
    
    print("\nMenú de acciones:")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        opcion = input("Opción inválida. Elija 1, 2 o 3: ")

    
    # OPCIÓN 1: FORZAR CERRADURA
    if opcion == "1":
        forzar_seguidos += 1
        energia -= 20
        tiempo -= 2
        
        # Regla Anti-spam (3ra vez seguida)
        if forzar_seguidos == 3:
            print("¡La cerradura se trabó por intentar forzar repetidamente!")
            alarma = True
        else:
            # Riesgo de alarma si energía < 40
            if energia < 40:
                print("¡RIESGO DE ALARMA!")
                num_riesgo = input("Para evitar la alarma, elija un número (1-3): ")
                while not num_riesgo.isdigit() or num_riesgo not in ["1", "2", "3"]:
                    num_riesgo = input("Número inválido. Elija 1, 2 o 3: ")
                
                if num_riesgo == "3":
                    alarma = True
                    print("¡Activaste la alarma!")
            
            # Si no hay alarma, abre cerradura
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con éxito!")

    # OPCIÓN 2: HACKEAR PANEL
    elif opcion == "2":
        forzar_seguidos = 0 # Rompe la racha de forzar
        energia -= 10
        tiempo -= 3
        
        print("Hackeando...")
        # Bucle de progreso
        for i in range(1, 5):
            print(f"Paso {i}...")
            codigo_parcial += "A" # Sumamos una letra
        
        # Si llega a 8 letras, abre cerradura
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = "" # Opcional: limpiar para el siguiente hackeo
                print("¡Hackeo completado! Se abrió una cerradura.")

    # OPCIÓN 3: DESCANSAR
    elif opcion == "3":
        forzar_seguidos = 0 # Rompe la racha de forzar
        tiempo -= 1
        
        recuperacion = 15
        if alarma:
            recuperacion -= 10 # -10 energía extra si la alarma está ON
            print("Es difícil descansar con la alarma sonando...")
        
        energia += recuperacion
        if energia > 100:
            energia = 100
        print(f"Has descansado. Energía actual: {energia}")

print("\n" + "="*30)
if cerraduras_abiertas >= 3:
    print(f"¡VICTORIA! El agente {nombre_agente} ha abierto la bóveda.")
elif bloqueo_sistema:
    print("DERROTA: El sistema se ha bloqueado por la alarma. ¡Atrapado!")
elif energia <= 0:
    print("DERROTA: Te has quedado sin energía.")
elif tiempo <= 0:
    print("DERROTA: Se acabó el tiempo.")
print("="*30)