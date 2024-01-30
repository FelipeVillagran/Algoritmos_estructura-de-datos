from collections import deque

mi_deque = deque()

# Operaciones en ambos extremos del deque
mi_deque.append(1)   # Agregar al final
mi_deque.appendleft(2)  # Agregar al principio

mi_deque.append(3)
mi_deque.appendleft(4)

print("Deque:", mi_deque)
print("Desencolar desde la izquierda:", mi_deque.popleft())
print("Desencolar desde la derecha:", mi_deque.pop())
print("Deque actualizado:", mi_deque)
