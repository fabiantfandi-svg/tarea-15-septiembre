# Lista de compras inteligente
compras = ["pan", "leche", "huevos"]
print("Lista inicial:")
print(compras)
# Agregar elementos
compras.append("queso") # append() agrega al final
compras.append("yogur")
print("\nDespués de agregar queso y yogur:")
print(compras)
# Insertar en posición específica
compras.insert(1, "mantequilla") # insert(posición, elemento)
print("\nDespués de insertar mantequilla en posición 1:")
print(compras)
# Eliminar elementos
compras.remove("huevos") # remove() elimina la primera aparición
print("\nDespués de eliminar huevos:")
print(compras)
# Eliminar por posición
elemento_eliminado = compras.pop(0) # pop() elimina y devuelve el elemento
print("\nEliminamos el primer elemento:", elemento_eliminado)
print("Lista final:", compras)