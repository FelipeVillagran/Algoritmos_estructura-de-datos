def quick_sort(lista):
    '''
    El ordenamiento rapido elige un elemento como pivote y particiona ña ñista en dos, colocando los elementos menores a la izquierda y los mayores a la derecha
    '''
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista.pop()
        menores = [elemento for elemento in lista if elemento <= pivote]
        mayores = [elemento for elemento in lista if elemento > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
mi_lista_ordenada = quick_sort(mi_lista)
print("Lista ordenada usando ordenamiento rápido:", mi_lista_ordenada)