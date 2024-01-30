from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()

    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]

# Ejemplo de uso
mi_cola = Cola()
mi_cola.encolar(1)
mi_cola.encolar(2)
mi_cola.encolar(3)
print("Frente de la cola:", mi_cola.ver_frente())
print("Desencolando elementos:")
while not mi_cola.esta_vacia():
    print(mi_cola.desencolar())
