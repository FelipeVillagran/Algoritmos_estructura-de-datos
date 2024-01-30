def ordenamiento_burbuja(lista):
    '''
    El ordenamiento de burbuja compara elementos adyacentes y los intercambia si están en el orden  incorrecto.
    '''
    n = len(lista)
    for i in range (n-1):
        for j in range (0, n - i - 1):
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_burbuja(mi_lista)
print(f'Lista ordenada usando ordenamiento de burbuja:',  mi_lista)