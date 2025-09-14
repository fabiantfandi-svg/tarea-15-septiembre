# Tabla de multiplicar
numero = 5  # Número para la tabla
multiplicador = 1  # Empezamos multiplicando por 1

print("Tabla de multiplicar del", numero, ":")
print("=" * 25)  # Línea decorativa

while multiplicador <= 10:
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)
    multiplicador = multiplicador + 1

print("=" * 25)
print("¡Tabla completa!")
