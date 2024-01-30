def radix_sort(lista):
    '''
    Radix Sort ordena los elementos procesando los dígitos de menos a más significativos o viceversa.
    '''
    max_valor = max(lista)
    exp = 1

    while max_valor // exp > 0:
        counting_sort_radix(lista, exp)
        exp *= 10

def counting_sort_radix(lista, exp):
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        indice = lista[i] // exp
        conteo[indice % 10] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    i = n - 1
    while i >= 0:
        indice = lista[i] // exp
        salida[conteo[indice % 10] - 1] = lista[i]
        conteo[indice % 10] -= 1
        i -= 1

    for i in range(n):
        lista[i] = salida[i]

# Ejemplo de uso
mi_lista_radix_sort = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(mi_lista_radix_sort)
print("Radix Sort:", mi_lista_radix_sort)