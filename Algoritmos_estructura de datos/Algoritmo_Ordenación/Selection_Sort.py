def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Ejemplo de uso
mi_lista_selection = [64, 34, 25, 12, 22, 11, 90]
selection_sort(mi_lista_selection)
print("Selection Sort:", mi_lista_selection)
