# Calculadora con funciones
def sumar(a, b):
    """Suma dos números y devuelve el resultado"""
    resultado = a + b
    return resultado

def restar(a, b):
    """Resta b de a y devuelve el resultado"""
    resultado = a - b
    return resultado

def multiplicar(a, b):
    """Multiplica dos números y devuelve el resultado"""
    resultado = a * b
    return resultado

def dividir(a, b):
    """Divide a entre b y devuelve el resultado"""
    if b != 0:  # Verificamos que no sea división entre cero
        resultado = a / b
        return resultado
    else:
        return "Error: No se puede dividir entre cero"

# Probando la calculadora
num1 = 15
num2 = 3

print("CALCULADORA CON FUNCIONES")
print(f"Números a operar: {num1} y {num2}")
print("-" * 30)
print(f"{num1} + {num2} = {sumar(num1, num2)}")
print(f"{num1} - {num2} = {restar(num1, num2)}")
print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
print(f"{num1} / {num2} = {dividir(num1, num2)}")

# Probando división entre cero
print(f"{num1} / 0 = {dividir(num1, 0)}")
