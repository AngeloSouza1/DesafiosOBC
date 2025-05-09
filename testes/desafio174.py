def ordenar_feiticos(feiticos):
    feiticos_ordenados = [''.join(sorted(f)) for f in feiticos]
    return sorted(feiticos_ordenados)

entrada = ['wxus', 'soacb']
saida = ordenar_feiticos(entrada)
print(saida)  
