##Mini Proyecto 2: Tienda, recibos, inputs y demas cosas##
##Codigo: 222452258 Braulio Sebastian Mercado Rodriguez 

# Miniproyecto: Recibo de compra - Tienda de postres y pasteles

IVA = 0.16

print("=== PASTELERIA Stocking Anarchy ===")
cliente = input("Nombre del cliente: ")

# Validar que el nombre no este vacio
while cliente == "":
    print("El nombre no puede estar vacio")
    cliente = input("Nombre del cliente: ")

subtotal = 0
lista_productos = ""   # aqui voy guardando las lineas del recibo porque si no se me pierden alv
continuar = "s"

while continuar == "s":
    producto = input("\nNombre del producto: ")
    while producto == "":
        print("El nombre no puede estar vacio")
        producto = input("Nombre del producto: ")

    # Precio (debe ser mayor a 0)
    precio = float(input("Precio: "))
    while precio <= 0:
        print("El precio debe ser mayor a 0")
        precio = float(input("Precio: "))

    # Cantidad (debe ser mayor a 0)
    cantidad = int(input("Cantidad: "))
    while cantidad <= 0:
        print("La cantidad debe ser mayor a 0")
        cantidad = int(input("Cantidad: "))

    importe = precio * cantidad
    subtotal = subtotal + importe
    lista_productos = lista_productos + f"{producto:<15} {cantidad:>3} {precio:>8.2f} {importe:>9.2f}\n"

    continuar = input("Quieres agregar otro producto? (s/n): ")
    while continuar != "s" and continuar != "n":
        print("Escribe s o n")
        continuar = input("Quieres agregar otro producto? (s/n): ")

# Calculos
iva = subtotal * IVA
total = subtotal + iva

# Mostrar el recibo
print("\n==================================")
print("     PASTELERIA Stocking AnarchyPanty ")
print("         RECIBO DE COMPRA")
print("==================================")
print(f"Cliente: {cliente}")
print("----------------------------------")
print(f"{'Producto':<15} {'Cant':>3} {'Precio':>8} {'Importe':>9}")
print(lista_productos, end="")
print("----------------------------------")
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"TOTAL: ${total:.2f}")
print("==================================")
print("Gracias por su compra!")