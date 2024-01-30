def busqueda_interpolada(lista, objetivo):
    '''
    La búsqueda interpolada es un algoritmo de búsqueda en listas ordenadas que calcula una estimación de la posición del objetivo.
    '''
    inicio, fin = 0, len(lista) - 1

    while inicio <= fin and lista[inicio] <= objetivo <= lista[fin]:
        posicion = inicio + int(((float(fin - inicio) / (lista[fin] - lista[inicio])) * (objetivo - lista[inicio])))
        
        if lista[posicion] == objetivo:
            return posicion
        elif lista[posicion] < objetivo:
            inicio = posicion + 1
        else:
            fin = posicion - 1

    return -1  # Retorna -1 si el elemento no está en la lista

# Ejemplo de uso
mi_lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = busqueda_interpolada(mi_lista_ordenada, 8)
print(f"El elemento 8 se encuentra en la posición: {resultado}")