class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
mi_lista_enlazada = ListaEnlazada()
mi_lista_enlazada.agregar_elemento(1)
mi_lista_enlazada.agregar_elemento(2)
mi_lista_enlazada.agregar_elemento(3)
mi_lista_enlazada.imprimir_lista()
