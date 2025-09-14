def inicio():
    print("¡Bienvenido a la Aventura de Texto!")
    print("Te encuentras en un bosque misterioso. El sol se está poniendo y el camino se bifurca en dos direcciones.")
    print("¿Qué camino eliges?")
    print("1. Ir por el camino oscuro.")
    print("2. Seguir el sendero iluminado.")
    
    decision = input("Elige 1 o 2: ")
    
    if decision == "1":
        camino_oscuro()
    elif decision == "2":
        sendero_iluminado()
    else:
        print("Opción no válida. Por favor elige 1 o 2.")
        inicio()

def camino_oscuro():
    print("\nHas elegido el camino oscuro.")
    print("El bosque se hace cada vez más oscuro y una extraña niebla comienza a rodearte.")
    print("De repente, te encuentras con un lobo enorme.")
    print("El lobo te mira fijamente.")
    print("¿Qué haces?")
    print("1. Intentar huir.")
    print("2. Hacer frente al lobo.")
    
    decision = input("Elige 1 o 2: ")
    
    if decision == "1":
        huir_del_lobo()
    elif decision == "2":
        enfrentarse_al_lobo()
    else:
        print("Opción no válida. Por favor elige 1 o 2.")
        camino_oscuro()

def sendero_iluminado():
    print("\nHas elegido el sendero iluminado.")
    print("El camino es tranquilo y rodeado de flores y árboles frondosos.")
    print("Al final del sendero, ves una cueva. De la cueva emana una extraña luz.")
    print("¿Qué haces?")
    print("1. Entrar en la cueva.")
    print("2. Ignorar la cueva y seguir caminando.")
    
    decision = input("Elige 1 o 2: ")
    
    if decision == "1":
        entrar_en_la_cueva()
    elif decision == "2":
        seguir_camino()
    else:
        print("Opción no válida. Por favor elige 1 o 2.")
        sendero_iluminado()

def huir_del_lobo():
    print("\nDecides huir rápidamente, pero el lobo es más rápido que tú.")
    print("El lobo te alcanza y... ¡el fin! Te devora.")
    print("¡Has perdido!")
    fin_juego()

def enfrentarse_al_lobo():
    print("\nTe enfrentas al lobo valientemente, pero resulta ser demasiado fuerte para ti.")
    print("El lobo te ataca y... ¡el fin! No logras sobrevivir.")
    print("¡Has perdido!")
    fin_juego()

def entrar_en_la_cueva():
    print("\nDecides entrar en la cueva. A medida que avanzas, encuentras una puerta dorada.")
    print("La puerta se abre y dentro encuentras un tesoro escondido. ¡Has ganado!")
    fin_juego()

def seguir_camino():
    print("\nDecides seguir el camino iluminado y, finalmente, llegas a una pequeña aldea segura.")
    print("El pueblo te ofrece refugio y comida, y vives una vida feliz. ¡Has ganado!")
    fin_juego()

def fin_juego():
    print("\nGracias por jugar. ¿Quieres jugar de nuevo? (sí/no)")
    respuesta = input().lower()
    if respuesta == "sí":
        inicio()
    else:
        print("¡Hasta la próxima aventura!")

# Comienza el juego
inicio()
