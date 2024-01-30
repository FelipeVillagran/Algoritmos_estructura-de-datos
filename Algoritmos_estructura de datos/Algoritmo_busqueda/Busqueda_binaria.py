def busqueda_binaria(lista,objetivo):
    '''
    La busqueda binaria es eficiente pero requiere que la lista esté ordenada. Divide la lista a la mitad y compara el elemento con el valor en la posición central
    '''
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio # Devuelve el indice del elemento si se encuentra 
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Ejemplo de uso (la lista debe estar ordenada)
mi_lista_ordenada = [1, 3, 5, 7, 9, 11]
resultado = busqueda_binaria(mi_lista_ordenada, 7)
print(f"El elemento 7 se encuentra en la posición: {resultado}")