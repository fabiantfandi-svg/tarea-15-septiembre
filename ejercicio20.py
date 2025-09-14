# Organizador de lista
numeros = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]

print("Lista original:", numeros)
print("Cantidad de elementos:", len(numeros))
# Crear copias para no modificar la original
numeros_ascendente = numeros.copy() # copy() crea una copia
numeros_descendente = numeros.copy()
# Ordenar de menor a mayor
numeros_ascendente.sort() # sort() ordena la lista
print("\nOrdenada ascendente:", numeros_ascendente)
# Ordenar de mayor a menor
numeros_descendente.sort(reverse=True) # reverse=True para descendente
print("Ordenada descendente:", numeros_descendente)
# Mezclar la lista
import random # Importamos la librería random
numeros_mezclados = numeros.copy()
random.shuffle(numeros_mezclados) # shuffle() mezcla aleatoriamente
print("Lista mezclada:", numeros_mezclados)
# Invertir orden
numeros_invertidos = numeros.copy()
numeros_invertidos.reverse() # reverse() invierte el orden actual
print("Orden invertido:", numeros_invertidos)
print("\nLista original (sin cambios):", numeros)