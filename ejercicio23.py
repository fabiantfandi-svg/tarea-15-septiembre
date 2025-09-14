# Analizador de texto
def contar_palabras(texto):
    """Cuenta cuántas palabras hay en un texto"""
    palabras = texto.split()  # split() divide el texto en palabras
    return len(palabras)

def contar_caracteres(texto, incluir_espacios=True):
    """Cuenta los caracteres del texto"""
    if incluir_espacios:
        return len(texto)
    else:
        return len(texto.replace(" ", ""))  # replace() quita los espacios

def encontrar_palabra_mas_larga(texto):
    """Encuentra la palabra más larga en el texto"""
    palabras = texto.split()
    palabra_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    return palabra_larga

def es_palindromo(texto):
    """Verifica si un texto es palíndromo (se lee igual al revés)"""
    # Convertir a minúsculas y quitar espacios
    texto_limpio = texto.lower().replace(" ", "")
    texto_invertido = texto_limpio[::-1]  # [::-1] invierte el texto
    return texto_limpio == texto_invertido

# Probando el analizador
frase = "La programación es divertida y educativa"
print("ANALIZADOR DE TEXTO")
print(f"Texto: '{frase}'")
print("-" * 50)
print(f"Palabras: {contar_palabras(frase)}")
print(f"Caracteres (con espacios): {contar_caracteres(frase)}")
print(f"Caracteres (sin espacios): {contar_caracteres(frase, False)}")
print(f"Palabra más larga: '{encontrar_palabra_mas_larga(frase)}'")
print(f"¿Es palíndromo?: {es_palindromo(frase)}")

# Probando con un palíndromo
palindromo = "anita lava la tina"
print(f"\nProbando palíndromo: '{palindromo}'")
print(f"¿Es palíndromo?: {es_palindromo(palindromo)}")
