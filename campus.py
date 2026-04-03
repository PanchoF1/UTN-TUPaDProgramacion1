usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 1
acceso = False

while intentos <= 3:
    print(f"\nIntento {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("\nCuenta bloqueada.")
else:
    
    opcion = ""
    while opcion != "4":
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")
        
        
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        
        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
            continue
            
        if opcion == "1":
            print("Estado: Inscripto")
        
        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")
            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirme clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: las claves no coinciden.")
                    
        elif opcion == "3":
            print("El destino mezcla las cartas, y nosotros las jugamos")
            
    print("Sesión cerrada.")