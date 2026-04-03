nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")

# Inicialización de Estadísticas
vida_jugador = 100        # int
vida_enemigo = 100        # int
pociones = 3              # int
dano_ataque_pesado = 15  # int
dano_enemigo = 12        # int
juego_activo = True       # boolean (para controlar el ciclo)

print("\n=== INICIO DEL COMBATE ===")

#El Ciclo de Combate
while vida_jugador > 0 and vida_enemigo > 0:
    # Mostrar estado actual
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # Validación del Menú
    opcion = input("Opción: ")
    while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
        print("Error: Ingrese un número válido (1, 2 o 3).")
        opcion = input("Opción: ")

    #Lógica de las Acciones del Jugador
    
    # Opción 1: Ataque Pesado
    if opcion == "1":
        dano_final = float(dano_ataque_pesado)
        # Golpe Crítico si el enemigo tiene poca vida
        if vida_enemigo < 20:
            dano_final = dano_ataque_pesado * 1.5 
            print("¡GOLPE CRÍTICO!")
        
        vida_enemigo -= int(dano_final)
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

    # Opción 2: Ráfaga Veloz
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # Opción 3: Curar
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f">> Usaste una poción. +30 de vida. Te quedan {pociones}.")
            if vida_jugador > 100:
                vida_jugador = 100
        else:
            print("¡No quedan pociones!")

    #Turno del Enemigo
    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f">> ¡El enemigo te atacó por {dano_enemigo} puntos de daño!")
        print("=== NUEVO TURNO ===")

print("\n" + "="*20)
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("="*20)