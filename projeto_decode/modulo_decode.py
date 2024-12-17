def decodificar_mensagem(mensagem_codificada):
    """
    Decodifica uma mensagem onde cada letra foi trocada pela próxima letra no alfabeto.

    Parâmetros:
    - mensagem_codificada (str): A mensagem codificada.

    Retorna:
    - str: A mensagem decodificada.
    """
    mensagem_decodificada = ""

    for char in mensagem_codificada:
        if char.islower():  # Se for uma letra minúscula
            mensagem_decodificada += chr(((ord(char) - ord('a') - 1) % 26) + ord('a'))
        elif char.isupper():  # Se for uma letra maiúscula
            mensagem_decodificada += chr(((ord(char) - ord('A') - 1) % 26) + ord('A'))
        else:
            # Se não for uma letra, mantém o caractere original
            mensagem_decodificada += char

    return mensagem_decodificada
