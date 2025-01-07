# monstros.py

def crie_monstros(dados):
    """
    Filtra os monstros com poder total acima da média.

    Args:
        dados (list): Lista de dicionários contendo os atributos dos monstros.

    Returns:
        list: Lista de dicionários com os monstros acima da média de poder total.
    """
    # Calcula o poder total de cada monstro
    poderes_totais = [monstro["ataque"] + monstro["defesa"] + monstro["magia"] for monstro in dados]

    # Calcula a média do poder total
    media_poder = sum(poderes_totais) / len(poderes_totais) if poderes_totais else 0

    # Filtra os monstros com poder total maior que a média
    monstros_acima_da_media = [
        monstro for monstro in dados
        if (monstro["ataque"] + monstro["defesa"] + monstro["magia"]) > media_poder
    ]

    return monstros_acima_da_media
