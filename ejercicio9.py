# Juego de adivinanza
numero_secreto = 7  # El número que hay que adivinar
adivinanza = 5  # El número que el jugador eligió

print("El número secreto es:", numero_secreto)
print("Tu adivinanza es:", adivinanza)

if adivinanza == numero_secreto:  # == significa "es igual a"
    print("¡FELICIDADES! Adivinaste el número")
elif adivinanza < numero_secreto:
    print("Tu número es menor. Intenta con uno más grande")
else:
    print("Tu número es mayor. Intenta con uno más pequeño")
