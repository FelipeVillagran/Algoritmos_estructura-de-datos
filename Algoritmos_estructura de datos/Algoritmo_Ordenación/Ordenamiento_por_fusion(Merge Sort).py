def merge_sort(lista):
    '''
    El ordenamiento por fusión divide la lista en mitades, ordena cada mitad y luego combina las mitades ordenadas.
    '''
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
merge_sort(mi_lista)
print("Lista ordenada usando ordenamiento por fusión:", mi_lista)
