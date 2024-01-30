'''
Un montículo binario es una estructura de datos de árbol binario completa en la que el valor de cada nodo es menor (o mayor, dependiendo del tipo de montículo) que los valores de sus nodos hijos.
'''
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insertar(self, elemento):
        heapq.heappush(self.heap, elemento)

    def extraer_min(self):
        return heapq.heappop(self.heap)

# Ejemplo de uso
mi_min_heap = MinHeap()
mi_min_heap.insertar(4)
mi_min_heap.insertar(2)
mi_min_heap.insertar(8)
mi_min_heap.insertar(1)

print("Elementos extraídos del Min Heap:")
while mi_min_heap.heap:
    print(mi_min_heap.extraer_min())
