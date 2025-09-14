# Juego de adivinanza con múltiples intentos
numero_secreto = 7
intentos_maximos = 3
intento_actual = 1

print("¡Bienvenido al juego de adivinanza!")
print("Tienes", intentos_maximos, "intentos para adivinar el número del 1 al 10")

while intento_actual <= intentos_maximos:
    print("\n--- Intento", intento_actual, "de", intentos_maximos, "---")
    
    # Simulamos que el jugador eligió un número
    if intento_actual == 1:
        adivinanza = 3
    elif intento_actual == 2:
        adivinanza = 8
    else:
        adivinanza = 7

    print("Tu adivinanza:", adivinanza)

    if adivinanza == numero_secreto:
        print("¡GANASTE! El número era", numero_secreto)
        break  # Salimos del bucle
    elif adivinanza < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    
    intento_actual = intento_actual + 1

if intento_actual > intentos_maximos:
    print("\n¡Se acabaron los intentos! El número era", numero_secreto)
