import random

class Animal:
    def __init__(self, nombre, tipo, energia=100, posicion_x=0, posicion_y=0):
        """
        Constructor para inicializar el animal.
        :param nombre: Nombre del animal.
        :param tipo: Tipo del animal (herbívoro, carnívoro).
        :param energia: Energía inicial del animal (default: 100).
        :param posicion_x: Posición inicial en el eje X (default: 0).
        :param posicion_y: Posición inicial en el eje Y (default: 0).
        """
        self.nombre = nombre
        self.tipo = tipo  # "herbívoro", "carnívoro"
        self.energia = energia
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.vivo = True

    def mover(self):
        """Mueve el animal aleatoriamente"""
        if self.vivo:
            # El movimiento es aleatorio en las direcciones X y Y
            self.posicion_x += random.randint(-1, 1)
            self.posicion_y += random.randint(-1, 1)
            self.energia -= 5  # Moverse cuesta energía

            # Si la energía es 0 o menos, el animal muere
            if self.energia <= 0:
                self.vivo = False
                print(f"{self.nombre} ha muerto por falta de energía.")
            else:
                print(f"{self.nombre} se ha movido a ({self.posicion_x}, {self.posicion_y}). Energía restante: {self.energia}")
        else:
            print(f"{self.nombre} ya está muerto.")

    def comer(self, cantidad_energia):
        """El animal come y recupera energía"""
        if self.vivo:
            self.energia += cantidad_energia
            print(f"{self.nombre} ha comido. Energía actual: {self.energia}")
        else:
            print(f"{self.nombre} no puede comer porque está muerto.")

    def estado(self):
        """Muestra el estado actual del animal"""
        if self.vivo:
            print(f"{self.nombre} está vivo. Energía: {self.energia}. Posición: ({self.posicion_x}, {self.posicion_y}).")
        else:
            print(f"{self.nombre} está muerto.")

# Creando instancias de Animal
leon = Animal("León", "carnívoro")
conejo = Animal("Conejo", "herbívoro", energia=50)

# Mover los animales
leon.mover()
conejo.mover()

# Hacer que coman
leon.comer(30)
conejo.comer(20)

# Ver el estado de los animales
leon.estado()
conejo.estado()
