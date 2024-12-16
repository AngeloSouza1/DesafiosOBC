# orbita.py

def calcular_voltas(angulos):
    """
    Calcula o número mínimo de voltas completas necessárias para passar por todos os pontos ao menos uma vez.

    Parâmetros:
    - angulos (list): Lista de ângulos inteiros representando os pontos de curva.

    Retorna:
    - int: Número mínimo de voltas completas.
    """
    # Normaliza os ângulos para o intervalo [0, 360) e ordena
    angulos = sorted([angulo % 360 for angulo in angulos])

    # Caso especial: Se há apenas um ângulo ou nenhum ângulo, apenas 1 volta é necessária
    if len(angulos) <= 1:
        return 1

    # Inicializa a contagem de voltas
    voltas = 1
    # Define o padrão como a primeira diferença
    pattern = angulos[1] - angulos[0]

    # Itera pelos ângulos e compara as diferenças
    for i in range(2, len(angulos)):
        diferenca = angulos[i] - angulos[i - 1]
        if diferenca != pattern:
            voltas += 1
            pattern = diferenca

    return voltas
