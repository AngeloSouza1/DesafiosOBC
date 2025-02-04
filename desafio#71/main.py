def transformar_emojis_em_sentimentos(lista_emojis):
    """
    Transforma uma lista de emojis em seus respectivos sentimentos.

    Args:
        lista_emojis (list): Lista contendo emojis.

    Returns:
        list: Lista de sentimentos correspondentes aos emojis.
    """

    # Dicionário mapeando os emojis para sentimentos
    mapa_sentimentos = {
        "😀": "Feliz",
        "😢": "Triste",
        "😡": "Bravo",
        "😱": "Assustado",
        "😍": "Apaixonado"
    }

    # Converter cada emoji para seu sentimento correspondente
    lista_sentimentos = [mapa_sentimentos[emoji] for emoji in lista_emojis if emoji in mapa_sentimentos]

    return lista_sentimentos

# Teste com a entrada fornecida
entrada = ["😀", "😢", "😍"]
saida = transformar_emojis_em_sentimentos(entrada)

print(f"Entrada: {entrada}")
print(f"Saída: {saida}")
