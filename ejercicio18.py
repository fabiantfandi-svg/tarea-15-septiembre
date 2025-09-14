# Calculadora de calificaciones
calificaciones = [8.5, 9.2, 7.8, 9.5, 6.9, 8.8, 9.1, 7.5]

print("Calificaciones del estudiante:")
print(calificaciones)

# Estadísticas básicas
total_materias = len(calificaciones)
suma_notas = sum(calificaciones)  # sum() suma todos los elementos
promedio = suma_notas / total_materias
nota_mayor = max(calificaciones)  # max() encuentra el mayor
nota_menor = min(calificaciones)  # min() encuentra el menor

print(f"\n--- ESTADÍSTICAS ---")
print(f"Total de materias: {total_materias}")
print(f"Suma de todas las notas: {suma_notas}")
print(f"Promedio: {promedio:.2f}")  # :.2f redondea a 2 decimales
print(f"Nota más alta: {nota_mayor}")
print(f"Nota más baja: {nota_menor}")

# Contar notas aprobadas (>=7.0)
aprobadas = 0
for nota in calificaciones:  # for recorre cada elemento
    if nota >= 7.0:
        aprobadas = aprobadas + 1

print(f"Materias aprobadas: {aprobadas} de {total_materias}")
