# Definir los productos en el inventario
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = [
            Producto("Laptop", 999.99, 10),
            Producto("Smartphone", 499.99, 20),
            Producto("Auriculares", 89.99, 50),
            Producto("Teclado", 29.99, 30),
            Producto("Ratón", 19.99, 25),
        ]

    def mostrar_inventario(self):
        print("\nInventario disponible:")
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto}")

    def obtener_producto(self, indice):
        if 0 <= indice < len(self.productos):
            return self.productos[indice]
        return None

    def actualizar_stock(self, producto, cantidad):
        producto.cantidad -= cantidad


class Carrito:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]["cantidad"] += cantidad
        else:
            self.productos[producto.nombre] = {"producto": producto, "cantidad": cantidad}

    def mostrar_carrito(self):
        if not self.productos:
            print("\nTu carrito está vacío.")
        else:
            print("\nProductos en tu carrito:")
            total = 0
            for item in self.productos.values():
                producto = item["producto"]
                cantidad = item["cantidad"]
                total_item = producto.precio * cantidad
                total += total_item
                print(f"{producto.nombre} - {cantidad} x ${producto.precio:.2f} = ${total_item:.2f}")
            print(f"\nTotal en carrito: ${total:.2f}")
        return total


class Pedido:
    def __init__(self, carrito):
        self.carrito = carrito
        self.estado = "Pendiente"

    def procesar_pago(self):
        total = self.carrito.mostrar_carrito()
        if total == 0:
            print("No hay productos en el carrito para procesar.")
            return False
        print(f"\nProcesando el pago de ${total:.2f}...")
        # Simulación del proceso de pago
        return True

    def actualizar_estado(self, estado):
        self.estado = estado

    def mostrar_estado(self):
        print(f"\nEstado del pedido: {self.estado}")


def realizar_compra(inventario, carrito):
    while True:
        inventario.mostrar_inventario()
        try:
            eleccion = int(input("\nSelecciona el número del producto que deseas agregar al carrito (0 para terminar): "))
            if eleccion == 0:
                break

            producto = inventario.obtener_producto(eleccion - 1)
            if producto is None:
                print("Selección inválida, intenta nuevamente.")
                continue

            cantidad = int(input(f"¿Cuántos de {producto.nombre} deseas agregar? "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
                continue

            if cantidad > producto.cantidad:
                print(f"No hay suficiente stock de {producto.nombre}. Solo hay {producto.cantidad} unidades disponibles.")
                continue

            carrito.agregar_producto(producto, cantidad)
            inventario.actualizar_stock(producto, cantidad)
            print(f"Agregaste {cantidad} x {producto.nombre} al carrito.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


def main():
    inventario = Inventario()
    carrito = Carrito()

    while True:
        print("\n--- Menú ---")
        print("1. Ver inventario")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Procesar pedido")
        print("5. Salir")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                inventario.mostrar_inventario()

            elif opcion == 2:
                realizar_compra(inventario, carrito)

            elif opcion == 3:
                carrito.mostrar_carrito()

            elif opcion == 4:
                pedido = Pedido(carrito)
                if pedido.procesar_pago():
                    pedido.actualizar_estado("Procesado")
                pedido.mostrar_estado()

            elif opcion == 5:
                print("¡Gracias por usar nuestro sistema!")
                break
            else:
                print("Opción no válida, por favor intenta nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


if __name__ == "__main__":
    main()
