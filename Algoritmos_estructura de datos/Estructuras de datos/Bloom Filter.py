'''
Un filtro Bloom es una estructura de datos probabilística diseñada para verificar si un elemento pertenece a un conjunto.
'''
import hashlib

class BloomFilter:
    def __init__(self, tamaño, num_funciones_hash):
        self.tamaño = tamaño
        self.bit_array = [0] * tamaño
        self.num_funciones_hash = num_funciones_hash

    def agregar(self, elemento):
        for i in range(self.num_funciones_hash):
            indice = self._hash(elemento, i) % self.tamaño
            self.bit_array[indice] = 1

    def verificar(self, elemento):
        for i in range(self.num_funciones_hash):
            indice = self._hash(elemento, i) % self.tamaño
            if self.bit_array[indice] == 0:
                return False
        return True

    def _hash(self, elemento, indice):
        # Utilizamos funciones hash diferentes para cada iteración
        hash_func = hashlib.sha256(f"{elemento}{indice}".encode())
        return int(hash_func.hexdigest(), 16)

# Ejemplo de uso
mi_bloom_filter = BloomFilter(10, 3)
mi_bloom_filter.agregar("hola")
mi_bloom_filter.agregar("adios")

print("¿'hola' está en el Bloom Filter?", mi_bloom_filter.verificar("hola"))
print("¿'chau' está en el Bloom Filter?", mi_bloom_filter.verificar("chau"))
