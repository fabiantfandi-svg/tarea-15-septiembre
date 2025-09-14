# Buscador en lista
animales = ["perro", "gato", "pájaro", "pez", "hamster", "conejo", "gato"]
print("Lista de animales:", animales)

# Buscar si un elemento existe
animal_buscado = "gato"
if animal_buscado in animales:  # 'in' verifica si existe
    print(f"\n{animal_buscado} está en la lista")
    
    # Encontrar la primera posición
    posicion = animales.index(animal_buscado)  # index() devuelve la posición
    print(f"Primera aparición en posición: {posicion}")
    
    # Contar cuántas veces aparece
    cantidad = animales.count(animal_buscado)  # count() cuenta apariciones
    print(f"Aparece {cantidad} veces en total")
else:
    print(f"\n{animal_buscado} no está en la lista")

# Buscar múltiples elementos
buscados = ["gato", "serpiente", "pájaro"]
print(f"\nBuscando: {buscados}")
for animal in buscados:
    if animal in animales:
        posicion = animales.index(animal)
        print(f"{animal} encontrado en posición {posicion}")
    else:
        print(f"{animal} no encontrado")
