def encontrar_numero_magico(lista):
    crescente = sorted(lista)
    decrescente = sorted(lista, reverse=True)

    return [crescente[i] for i in range(len(lista)) if crescente[i] == decrescente[i]]


print(encontrar_numero_magico([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))
print(encontrar_numero_magico([7, 6, 5, 4, 3, 2, 1]))
print(encontrar_numero_magico([1, 2, 3, 4, 5]))
print(encontrar_numero_magico([10, 20, 30, 40, 50, 60]))

