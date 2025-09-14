# Calculadora de descuentos
precio_total = 120  # Total de la compra
descuento = 0  # Inicializamos el descuento en 0

if precio_total > 100:  # Si gasta más de $100
    descuento = precio_total * 0.10  # 10% de descuento
    precio_final = precio_total - descuento
    print("¡Felicidades! Tienes un descuento del 10%")
    print("Descuento aplicado: $", descuento)
else:
    precio_final = precio_total
    print("No hay descuento disponible")

print("Precio original: $", precio_total)
print("Precio final: $", precio_final)
