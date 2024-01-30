def busqueda_lineal(lista,objetivo):
    '''
    La busqueda lineal es un metodo simple que recorre la lista de elementos uno por uno hasta encontrar el elemento buscado.
    '''
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i # Devuelve el indice del elemento si se encuentra
    return -1   # Si no se encuentra devuelve -1

#Ejemplo de uso
mi_lista = [1, 3, 5, 7, 9, 11]
resultado = busqueda_lineal(mi_lista, 7)
print(f'El elemento 7 se encuentra en la posición {resultado}')
