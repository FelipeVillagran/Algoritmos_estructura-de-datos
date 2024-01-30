def busqueda_exponencial(lista, objetivo):
    '''
    La búsqueda exponencial es una variante de la búsqueda binaria que funciona en listas ordenadas y reduce el rango de búsqueda exponencialmente.
    '''
    n = len(lista)
    
    if lista[0] == objetivo:
        return 0
    
    i = 1
    while i < n and lista[i] <= objetivo:
        i = i * 2

    return busqueda_binaria(lista, objetivo, i // 2, min(i, n))

# Utilizando la búsqueda binaria previamente definida
def busqueda_binaria(lista, objetivo, inicio, fin):
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  # Devuelve el índice del elemento si se encuentra
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1  # Retorna -1 si el elemento no está en la lista

# Ejemplo de uso
mi_lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = busqueda_exponencial(mi_lista_ordenada, 8)
print(f"El elemento 8 se encuentra en la posición: {resultado}")