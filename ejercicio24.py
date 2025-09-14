import random
import string

def generar_contraseña(longitud=8, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=False):
    """
    Genera una contraseña aleatoria con las características especificadas
    """
    caracteres = string.ascii_lowercase  # letras minúsculas
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # agregar mayúsculas
    if incluir_numeros:
        caracteres += string.digits  # agregar números 0-9
    if incluir_simbolos:
        caracteres += "!@#$%&*"  # agregar algunos símbolos
    
    # Generar la contraseña
    contraseña = ""
    for i in range(longitud):
        caracter_aleatorio = random.choice(caracteres)
        contraseña += caracter_aleatorio
    return contraseña

def evaluar_fortaleza(contraseña):
    """Evalúa qué tan fuerte es una contraseña"""
    puntos = 0
    comentarios = []

    # Longitud
    if len(contraseña) >= 8:
        puntos += 2
        comentarios.append("Longitud adecuada")
    else:
        comentarios.append("Muy corta (mínimo 8 caracteres)")
    
    # Mayúsculas
    if any(c.isupper() for c in contraseña):
        puntos += 1
        comentarios.append("Contiene mayúsculas")
    else:
        comentarios.append("Sin mayúsculas")
    
    # Números
    if any(c.isdigit() for c in contraseña):
        puntos += 1
        comentarios.append("Contiene números")
    else:
        comentarios.append("Sin números")
    
    # Evaluar fortaleza
    if puntos >= 4:
        fortaleza = "Muy fuerte"
    elif puntos >= 3:
        fortaleza = "Fuerte"
    elif puntos >= 2:
        fortaleza = "Moderada"
    else:
        fortaleza = "Débil"

    return fortaleza, comentarios

# Probando el generador
print("GENERADOR DE CONTRASEÑAS")
print("=" * 40)

# Generar diferentes tipos de contraseñas
contraseña1 = generar_contraseña(12, True, True, False)
contraseña2 = generar_contraseña(8, True, True, True)
contraseña3 = generar_contraseña(6, False, False, False)

contraseñas = [
    ("Estándar (12 caracteres)", contraseña1),
    ("Con símbolos (8 caracteres)", contraseña2),
    ("Solo minúsculas (6 caracteres)", contraseña3)
]

for descripcion, contraseña in contraseñas:
    fortaleza, comentarios = evaluar_fortaleza(contraseña)
    print(f"\n{descripcion}:")
    print(f"Contraseña: {contraseña}")
    print(f"Fortaleza: {fortaleza}")
    for comentario in comentarios:
        print(f"  {comentario}")
