from collections import Counter
import heapq

class NodoHuffman:
    """Nodo para el árbol de codificación Huffman"""
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        # Compara nodos para ordenar en el heap
        return self.freq < other.freq

def comprimir_repeticion_simple(texto):
    """
    Compresión simple: reemplaza secuencias repetidas
    Ejemplo: "aaaa" -> "4a"
    """
    print("Compresión por repetición simple:")
    resultado = []
    contador = 1

    for i in range(1, len(texto)):
        if texto[i] == texto[i-1]:
            contador += 1
        else:
            if contador > 1:
                resultado.append(f"{contador}{texto[i-1]}")
            else:
                resultado.append(texto[i-1])
            contador = 1
    # Agregar el último grupo
    if contador > 1:
        resultado.append(f"{contador}{texto[-1]}")
    else:
        resultado.append(texto[-1])

    compresion = ''.join(resultado)
    print(f"Texto original: {texto}")
    print(f"Texto comprimido: {compresion}")
    return compresion

def construir_arbol_huffman(texto):
    """
    Construye el árbol de Huffman y retorna el diccionario de códigos
    """
    # Contar la frecuencia de cada carácter
    frecuencia = Counter(texto)
    
    # Crear una lista de nodos
    heap = [NodoHuffman(char, freq) for char, freq in frecuencia.items()]
    
    # Convertir la lista en un heap (min-heap)
    heapq.heapify(heap)
    
    # Crear el árbol de Huffman
    while len(heap) > 1:
        # Extraer los dos nodos con menor frecuencia
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)
        
        # Crear un nuevo nodo con estos dos como hijos
        nuevo_nodo = NodoHuffman(None, izquierda.freq + derecha.freq, izquierda, derecha)
        
        # Insertar el nuevo nodo de vuelta en el heap
        heapq.heappush(heap, nuevo_nodo)
    
    # El único nodo restante es la raíz del árbol
    raiz = heap[0]
    
    # Generar los códigos de Huffman
    def generar_codigos(nodo, prefijo="", codigos={}):
        if nodo is not None:
            if nodo.char is not None:
                codigos[nodo.char] = prefijo
            generar_codigos(nodo.left, prefijo + "0", codigos)
            generar_codigos(nodo.right, prefijo + "1", codigos)
        return codigos
    
    codigos_huffman = generar_codigos(raiz)
    
    return codigos_huffman

def comprimir_huffman(texto):
    """
    Comprime un texto usando el algoritmo de Huffman
    """
    print("\nCompresión con Huffman:")
    codigos_huffman = construir_arbol_huffman(texto)
    print(f"Códigos Huffman: {codigos_huffman}")
    
    # Comprimir el texto utilizando los códigos generados
    texto_comprimido = ''.join(codigos_huffman[char] for char in texto)
    print(f"Texto original: {texto}")
    print(f"Texto comprimido: {texto_comprimido}")
    return texto_comprimido, codigos_huffman

# Ejemplo de uso
if __name__ == "__main__":
    texto = "aaaaabbbcccdde"
    
    # Comprimir por repetición simple
    comprimir_repeticion_simple(texto)
    
    # Comprimir usando Huffman
    comprimir_huffman(texto)
