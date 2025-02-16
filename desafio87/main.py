def organiza_inventario(inventario):
    """
    Organiza a lista de poções em ordem decrescente de poder.

    Args:
        inventario (list): Lista de dicionários contendo 'nome' e 'poder' de cada poção.

    Returns:
        list: Lista ordenada das poções da mais forte para a mais fraca.
    """
    if not inventario:
        return "Erro: O inventário está vazio!"

    inventario_ordenado = sorted(inventario, key=lambda poção: poção['poder'], reverse=True)
    
    return inventario_ordenado

# 🔥 **Teste com a entrada do desafio**
inventario = [
    {'nome': 'Poção de Cura', 'poder': 50},
    {'nome': 'Poção de Invisibilidade', 'poder': 75},
    {'nome': 'Poção de Força', 'poder': 60}
]

resultado = organiza_inventario(inventario)
print(f"\n🧪 **Inventário Organizado:**\n{resultado}\n")
