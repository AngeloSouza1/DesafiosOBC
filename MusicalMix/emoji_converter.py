def converter_para_emoji(nome_banda):
    """
    Converte o nome da banda em uma sequência de emojis.

    Args:
        nome_banda (str): Nome original da banda.

    Returns:
        str: Nome da banda em formato de emoji.
    """
    # Mapeamento de vogais para emojis
    vogais_para_emojis = {
        'a': '💛',
        'e': '🎼',
        'i': '🎷',
        'o': '🥁',
        'u': '🎹'
    }

    # Mapeamento de consoantes para emojis
    consoantes_para_emojis = {
        'b': '🎺',
        'c': '🎸',
        'd': '🥁',
        'f': '🎻',
        'g': '🎷',
        'h': '🎹',
        'j': '🎵',
        'k': '🎶',
        'l': '🎤',
        'm': '🎷',
        'n': '🎼',
        'p': '🎺',
        'q': '🎻',
        'r': '🎸',
        's': '🎵',
        't': '🎶',
        'v': '🎤',
        'w': '🎺',
        'x': '🎸',
        'y': '🎵',
        'z': '🎻'
    }

    # Resultado em formato de emoji
    resultado = []

    for letra in nome_banda.lower():
        if letra in vogais_para_emojis:
            resultado.append(vogais_para_emojis[letra])
        elif letra in consoantes_para_emojis:
            resultado.append(consoantes_para_emojis[letra])

    return ''.join(resultado)
