mi_hash_table = {}

# Agregar elementos a la tabla hash
mi_hash_table['clave1'] = 'valor1'
mi_hash_table['clave2'] = 'valor2'
mi_hash_table['clave3'] = 'valor3'

# Acceder a elementos
print("Valor asociado a 'clave2':", mi_hash_table['clave2'])

# Actualizar un valor
mi_hash_table['clave2'] = 'nuevo_valor'

# Eliminar un elemento
del mi_hash_table['clave1']

# Imprimir la tabla hash
print("Tabla Hash actualizada:", mi_hash_table)
