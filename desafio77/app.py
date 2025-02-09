def encantar_frase(frase):
    """
    Inverte cada palavra de uma frase, mantendo a ordem das palavras.
    
    Args:
        frase (str): A frase de entrada com várias palavras.
    
    Returns:
        str: A frase encantada com cada palavra invertida.
    """
    # Divide a frase em palavras
    palavras = frase.split(" ")
    # Inverte cada palavra
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    # Junta as palavras invertidas com espaços
    frase_encantada = " ".join(palavras_invertidas)
    return frase_encantada

# Teste com a entrada fornecida
entrada = "Hello world! Let's code Magic!"
saida = encantar_frase(entrada)

# Exibe a entrada e a saída
print(f"Entrada: '{entrada}'")
print(f"Saída: '{saida}'")
