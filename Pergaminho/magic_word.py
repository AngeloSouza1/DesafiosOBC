def encontrar_palavra_magica(pergaminho):
    """
    Encontra a palavra que aparece um número ímpar de vezes na string.

    Args:
        pergaminho (str): A string contendo palavras separadas por espaços.

    Returns:
        str: A palavra mágica que aparece um número ímpar de vezes.
    """
    # Divide o pergaminho em palavras
    palavras = pergaminho.split()

    # Dicionário para contar as ocorrências
    contador = {}

    # Conta as ocorrências de cada palavra
    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    # Encontra a palavra com número ímpar de ocorrências
    for palavra, frequencia in contador.items():
        if frequencia % 2 != 0:
            return palavra
