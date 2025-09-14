import random
import math
from itertools import permutations

def calcular_distancia(ciudad1, ciudad2):
    """
    Calcula la distancia euclidiana entre dos ciudades
    Cada ciudad tiene coordenadas (x, y)
    """
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distancia, 2)

def calcular_distancia_total_ruta(ciudades, ruta):
    """
    Calcula la distancia total de una ruta completa
    La ruta es una lista de índices de ciudades
    """
    distancia_total = 0
    # Calcular distancia entre ciudades consecutivas
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]
        siguiente_ciudad = ciudades[ruta[(i + 1) % len(ruta)]]  # % para volver al inicio
        distancia = calcular_distancia(ciudad_actual, siguiente_ciudad)
        distancia_total += distancia
    return round(distancia_total, 2)

def metodo_fuerza_bruta(ciudades):
    """
    Encuentra la ruta óptima probando todas las combinaciones posibles
    ¡ADVERTENCIA: Solo usar con pocas ciudades por complejidad computacional!
    """
    num_ciudades = len(ciudades)
    print(f"Buscando la ruta óptima entre {num_ciudades} ciudades...")
    
    # Generar todas las posibles rutas (permutaciones)
    indices = list(range(num_ciudades))
    permutaciones_rutas = permutations(indices)
    
    ruta_optima = None
    distancia_minima = float('inf')
    
    # Evaluar cada ruta posible
    for ruta in permutaciones_rutas:
        distancia_actual = calcular_distancia_total_ruta(ciudades, ruta)
        if distancia_actual < distancia_minima:
            distancia_minima = distancia_actual
            ruta_optima = ruta
            
    print(f"\nRuta óptima encontrada: {ruta_optima}")
    print(f"Distancia total de la ruta óptima: {distancia_minima} unidades")
    return ruta_optima, distancia_minima

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ciudades con coordenadas (x, y)
    ciudades = [
        (0, 0),  # Ciudad 1
        (2, 4),  # Ciudad 2
        (5, 2),  # Ciudad 3
        (8, 3)   # Ciudad 4
    ]
    
    # Buscar la ruta óptima
    ruta_optima, distancia_optima = metodo_fuerza_bruta(ciudades)
