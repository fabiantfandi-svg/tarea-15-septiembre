import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: El factorial no está definido para números negativos"
    return math.factorial(a)

def calculadora():
    print("Calculadora con operaciones básicas y avanzadas")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Potencia (^)")
    print("6. Raíz cuadrada (sqrt)")
    print("7. Factorial (!)")
    
    while True:
        operacion = input("\nElige la operación (1/2/3/4/5/6/7) o 'salir' para salir: ").strip().lower()
        
        if operacion == 'salir':
            print("¡Hasta luego!")
            break
        
        if operacion in ['1', '2', '3', '4', '5']:
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))
            except ValueError:
                print("Error: Por favor ingresa un número válido.")
                continue
            
            if operacion == '1':
                print(f"Resultado: {suma(a, b)}")
            elif operacion == '2':
                print(f"Resultado: {resta(a, b)}")
            elif operacion == '3':
                print(f"Resultado: {multiplicacion(a, b)}")
            elif operacion == '4':
                print(f"Resultado: {division(a, b)}")
            elif operacion == '5':
                print(f"Resultado: {potencia(a, b)}")
        
        elif operacion == '6':
            try:
                a = float(input("Introduce el número: "))
                print(f"Resultado: {raiz(a)}")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")
        
        elif operacion == '7':
            try:
                a = int(input("Introduce un número entero: "))
                print(f"Resultado: {factorial(a)}")
            except ValueError:
                print("Error: Por favor ingresa un número entero válido.")
        
        else:
            print("Error: Operación no válida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
