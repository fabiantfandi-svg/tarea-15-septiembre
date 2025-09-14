def ordenamiento_burbuja(lista):
    """
    Implementa el algoritmo de ordenamiento burbuja
    Compara elementos adyacentes y los intercambia si es necesario
    """
    n = len(lista)
    lista_copia = lista.copy()  # Trabajamos con una copia
    comparaciones = 0
    intercambios = 0

    print(f"Lista original: {lista_copia}")
    print("\nProceso paso a paso:")

    # Bucle externo: número de pasadas
    for i in range(n):
        print(f"\n--- Pasada {i + 1} ---")
        hubo_intercambio = False
        # Bucle interno: comparaciones en esta pasada
        for j in range(0, n - i - 1):
            comparaciones += 1
            print(f"Comparando {lista_copia[j]} y {lista_copia[j + 1]}")
            # Si el elemento actual es mayor que el siguiente, intercambiar
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                intercambios += 1
                hubo_intercambio = True
                print(f"Intercambio realizado: {lista_copia}")
            else:
                print("No hay intercambio")

        print(f"Estado después de pasada {i + 1}: {lista_copia}")

        # Optimización: si no hubo intercambios, la lista ya está ordenada
        if not hubo_intercambio:
            print("¡No hubo intercambios! La lista ya está ordenada.")
            break

    print(f"\nResultado final: {lista_copia}")
    print(f"Estadísticas:")
    print(f" - Total de comparaciones: {comparaciones}")
    print(f" - Total de intercambios: {intercambios}")
    return lista_copia

# Probando el ordenamiento burbuja
numeros = [64, 34, 25, 12, 22, 11, 90]
print("ALGORITMO DE ORDENAMIENTO BURBUJA")
print("=" * 45)
resultado = ordenamiento_burbuja(numeros)
