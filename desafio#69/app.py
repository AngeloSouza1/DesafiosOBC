from itertools import product

def gerar_traducoes(mensagem_original, traducoes):
    """
    Gera todas as combinações possíveis de traduções para uma mensagem.

    Args:
        mensagem_original (str): A string original da mensagem.
        traducoes (dict): Dicionário com as possíveis traduções para cada caractere.

    Returns:
        list: Lista com todas as combinações possíveis.
    """

    print(f"\n🔍 [DEBUG] Mensagem original: {mensagem_original}")
    print(f"🔍 [DEBUG] Traduções disponíveis: {traducoes}")

    # Criar a lista de opções de tradução respeitando a ordem dos caracteres na mensagem
    lista_traducao = [traducoes[char] for char in mensagem_original]

    print(f"🔍 [DEBUG] Lista de opções de tradução: {lista_traducao}")

    # Gerar todas as combinações possíveis usando product()
    todas_combinacoes = [''.join(comb) for comb in product(*lista_traducao)]
    
    print(f"\n✅ Todas as combinações geradas: {todas_combinacoes}")

    return todas_combinacoes

# Teste direto no script
if __name__ == "__main__":
    mensagem_original = "SOS"
    traducoes = {
        'S': ['5', '2'],
        'O': ['9', '6']
    }
    resultado = gerar_traducoes(mensagem_original, traducoes)
