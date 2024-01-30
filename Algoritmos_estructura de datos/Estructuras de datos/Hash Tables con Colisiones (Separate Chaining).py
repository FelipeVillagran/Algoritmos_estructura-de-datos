class NodoHash:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class HashTableConColisiones:
    def __init__(self, tamaño_tabla):
        self.tamaño_tabla = tamaño_tabla
        self.tabla = [None] * tamaño_tabla

    def hash_func(self, clave):
        return hash(clave) % self.tamaño_tabla

    def insertar(self, clave, valor):
        indice = self.hash_func(clave)
        nuevo_nodo = NodoHash(clave, valor)

        if self.tabla[indice] is None:
            self.tabla[indice] = nuevo_nodo
        else:
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar(self, clave):
        indice = self.hash_func(clave)
        actual = self.tabla[indice]

        while actual:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente

        return None

# Ejemplo de uso
mi_tabla_hash = HashTableConColisiones(10)
mi_tabla_hash.insertar('clave1', 'valor1')
mi_tabla_hash.insertar('clave2', 'valor2')
mi_tabla_hash.insertar('clave3', 'valor3')

print("Valor asociado a 'clave2':", mi_tabla_hash.buscar('clave2'))
