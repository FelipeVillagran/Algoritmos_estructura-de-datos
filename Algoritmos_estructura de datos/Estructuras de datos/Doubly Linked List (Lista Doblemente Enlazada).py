class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_elemento(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
mi_lista_doblemente_enlazada = ListaDoblementeEnlazada()
mi_lista_doblemente_enlazada.agregar_elemento(1)
mi_lista_doblemente_enlazada.agregar_elemento(2)
mi_lista_doblemente_enlazada.agregar_elemento(3)
mi_lista_doblemente_enlazada.imprimir_lista()
