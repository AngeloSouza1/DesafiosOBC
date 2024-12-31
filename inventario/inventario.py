def calcular_peso_total(items):

    peso_total = sum(item["peso"] for item in items)
    return peso_total

def avaliar_capacidade(peso_total, capacidade_maxima):

    if peso_total > capacidade_maxima:
        return "Cuidado! O peso ultrapassa a capacidade máxima."
    else:
        return "Tudo certo! O peso está dentro do limite."
