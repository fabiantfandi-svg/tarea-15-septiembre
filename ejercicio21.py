# Mi primera función
def saludar(nombre):  # def define la función, nombre es el parámetro
    """Esta función saluda a una persona por su nombre"""
    mensaje = f"¡Hola {nombre}! ¿Cómo estás?"
    return mensaje  # return devuelve el resultado

# Usar la función (llamarla)
saludo1 = saludar("Ana")  # Llamamos la función con "Ana"
saludo2 = saludar("Carlos")  # La reutilizamos con "Carlos"
saludo3 = saludar("María")  # Y otra vez con "María"

print("Usando mi función de saludo:")
print(saludo1)
print(saludo2)
print(saludo3)

# También podemos usarla directamente
print("\nUsando directamente:")
print(saludar("Pedro"))
print(saludar("Laura"))
