# Clasificador de notas
nota = 8.5  # Calificación del estudiante

if nota >= 9.0:
    clasificacion = "Excelente"
    mensaje = "¡Felicidades! Sigue así"
elif nota >= 7.0:  # elif significa "sino si"
    clasificacion = "Buena"
    mensaje = "Buen trabajo, puedes mejorar"
else:
    clasificacion = "Necesita mejorar"
    mensaje = "Estudia más para la próxima"

print("Tu nota es:", nota)
print("Clasificación:", clasificacion)
print("Comentario:", mensaje)
