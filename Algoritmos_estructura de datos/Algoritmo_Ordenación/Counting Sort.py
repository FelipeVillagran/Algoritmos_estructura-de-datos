def counting_sort(lista):
    '''
    Counting Sort es un algoritmo de ordenación que funciona bien para números enteros no negativos con un rango conocido.
    '''
    max_valor = max(lista)
    min_valor = min(lista)
    rango = max_valor - min_valor + 1

    # Inicializar el arreglo de conteo
    conteo = [0] * rango

    # Contar las ocurrencias de cada elemento
    for num in lista:
        conteo[num - min_valor] += 1

    # Reconstruir la lista ordenada
    idx = 0
    for i in range(rango):
        while conteo[i] > 0:
            lista[idx] = i + min_valor
            idx += 1
            conteo[i] -= 1

# Ejemplo de uso
mi_lista_counting_sort = [4, 2, 2, 8, 3, 3, 1]
counting_sort(mi_lista_counting_sort)
print("Counting Sort:", mi_lista_counting_sort)