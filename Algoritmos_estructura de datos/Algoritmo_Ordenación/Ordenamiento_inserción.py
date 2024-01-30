def ordenamiento_insercion(lista):
    '''
    El ordenamiento por inserción construye una secuencia ordenada tomando un elemento de la lista y colocandolo en la posicion correcta
    '''
    for i in range(1, len(lista)):
        clave =lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1]  = lista[j]
            j -=1
        lista[j + 1] = clave
        
# Ejemplo de uso
mi_lista= [64, 34, 25, 12, 22, 11, 90]
ordenamiento_insercion(mi_lista)
print(f'Lista ordenada usando ordenamiento por inserción:', mi_lista)