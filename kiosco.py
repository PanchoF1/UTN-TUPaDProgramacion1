nombre = input("Cliente: ")
while not nombre.isalpha():
    print("ERROR: NOMBRE INVALIDO, SOLO DEBE TENER LETRAS Y NO ESTAR VACIO")
    nombre = input("Cliente: ")

cantidad_str = input("Cantidad de productos: ")

while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    print("ERROR: DEBE INGRESAR NUMERO ENTERO POSITIVO MAYOR A 0.")
    cantidad_str = input("Cantidad de productos: ")

cantidad = int(cantidad_str)

total_sin_descuento = 0.0
total_con_descuento = 0.0

for i in range(1, cantidad + 1):
    print(f"\nProducto {i}:")
    
    precio_str = input(f"  Precio: ")
    while not precio_str.isdigit():
        print("  ERROR: INGRESE PRECIO VALIDO (ENTERO).")
        precio_str = input(f"  Precio: ")
    
    precio = int(precio_str)
    
    tiene_desc = input("  Descuento (S/N): ").lower()
    while tiene_desc not in ['s', 'n']:
        print("  ERROR: INGRESE 's' PARA Si o 'n' PARA No.")
        tiene_desc = input("  Descuento (S/N): ").lower()
    
    precio_final = precio
    if tiene_desc == 's':
        precio_final = precio * 0.90  # Aplica el 10% de descuento
        
    total_sin_descuento += precio
    total_con_descuento += precio_final


ahorro_total = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad


print("\n")
print(f"Total sin descuentos: ${total_sin_descuento:.0f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")