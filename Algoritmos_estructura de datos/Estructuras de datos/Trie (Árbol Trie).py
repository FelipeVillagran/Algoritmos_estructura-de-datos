'''
Un árbol Trie es una estructura de datos de árbol que se utiliza para almacenar una colección dinámica o eficiente de cadenas.
'''
class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.es_fin_de_palabra = False

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, palabra):
        nodo_actual = self.raiz
        for caracter in palabra:
            if caracter not in nodo_actual.hijos:
                nodo_actual.hijos[caracter] = NodoTrie()
            nodo_actual = nodo_actual.hijos[caracter]
        nodo_actual.es_fin_de_palabra = True

    def buscar(self, palabra):
        nodo_actual = self.raiz
        for caracter in palabra:
            if caracter not in nodo_actual.hijos:
                return False
            nodo_actual = nodo_actual.hijos[caracter]
        return nodo_actual.es_fin_de_palabra

# Ejemplo de uso
mi_trie = Trie()
mi_trie.insertar("hola")
mi_trie.insertar("adios")
mi_trie.insertar("hombre")

print("¿'hola' está en el Trie?", mi_trie.buscar("hola"))
print("¿'hombre' está en el Trie?", mi_trie.buscar("hombre"))
print("¿'chau' está en el Trie?", mi_trie.buscar("chau"))
