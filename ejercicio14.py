# Detector de números pares
numero = 1  # Empezamos desde 1
limite = 20  # Hasta dónde buscar
pares_encontrados = 0  # Contador de pares

print("Buscando números pares entre 1 y", limite, ":")

while numero <= limite:
    if numero % 2 == 0:  # % es el operador módulo (resto de división)
        print(numero, "es par")
        pares_encontrados = pares_encontrados + 1
    numero = numero + 1

print("\nResumen:")
print("Se encontraron", pares_encontrados, "números pares")
