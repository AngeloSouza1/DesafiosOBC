def calcular_pontos(tarefas):
    """
    Calcula a pontuação total de acordo com as regras:
    - Primeiro lugar ganha todos os pontos disponíveis.
    - Segundo lugar ganha metade dos pontos disponíveis, arredondados para baixo.
    - Terceiro lugar não ganha pontos.
    
    :param tarefas: Lista de pontos disponíveis para cada tarefa.
    :return: Tupla com pontuações (primeiro lugar, segundo lugar, terceiro lugar).
    """
    primeiro_lugar = 0
    segundo_lugar = 0
    terceiro_lugar = 0

    for pontos in tarefas:
        primeiro_lugar += pontos
        segundo_lugar += pontos // 2
        terceiro_lugar += 0

    return primeiro_lugar, segundo_lugar, terceiro_lugar
