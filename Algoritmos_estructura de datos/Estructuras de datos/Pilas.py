'''
Una pila es una estructura de datos que el principio LIFE (Last in, First Out), es decir, el ultimo elemento que se añade es el primero en ser retirado
'''
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

# Ejemplo de uso
mi_pila = Pila()
mi_pila.apilar(1)
mi_pila.apilar(2)
mi_pila.apilar(3)
print("Tope de la pila:", mi_pila.ver_tope())
print("Desapilando elementos:")
while not mi_pila.esta_vacia():
    print(mi_pila.desapilar())
