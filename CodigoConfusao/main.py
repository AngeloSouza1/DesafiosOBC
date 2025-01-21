def decifrar_mensagem(codificada):
    """
    Decifra uma mensagem onde cada par de caracteres consecutivos foi invertido.
    """
    mensagem_decifrada = []
    print("Iniciando a decodificação...")

    for i in range(0, len(codificada) - 1, 2):
        # Inverte o par de caracteres
        mensagem_decifrada.append(codificada[i + 1])  # Segundo caractere do par
        mensagem_decifrada.append(codificada[i])      # Primeiro caractere do par
        print(f"Par processado: '{codificada[i]}{codificada[i + 1]}' -> '{codificada[i + 1]}{codificada[i]}'")

    mensagem_decifrada = ''.join(mensagem_decifrada)
    print("Decodificação finalizada!")
    return mensagem_decifrada


# Teste com a entrada do desafio
mensagem_codificada = "ehll o"  # Entrada embaralhada corretamente
mensagem_original = decifrar_mensagem(mensagem_codificada)
print(f"Mensagem Original: {mensagem_original}")
