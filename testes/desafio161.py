def contar_espirros(sequencia):
    return {
        'forte': sequencia.count('F'),
        'fraco': sequencia.count('f')
    }
print(contar_espirros("FFfFfFf"))
# Saída: {'forte': 4, 'fraco': 3}
