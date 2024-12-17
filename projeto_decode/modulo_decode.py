def codificar_mensagem(mensagem):
    mensagem_codificada = ""

    for char in mensagem:
        if 'a' <= char <= 'z':
            mensagem_codificada += chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            mensagem_codificada += chr(((ord(char) - ord('A') + 1) % 26) + ord('A'))
        else:
            mensagem_codificada += char

    return mensagem_codificada


def decodificar_mensagem(mensagem_codificada):
     mensagem_decodificada = ""

    for char in mensagem_codificada:
        if 'a' <= char <= 'z':
            mensagem_decodificada += 'z' if char == 'a' else chr(ord(char) - 1)
        elif 'A' <= char <= 'Z':
            mensagem_decodificada += 'Z' if char == 'A' else chr(ord(char) - 1)
        else:
            mensagem_decodificada += char

    return mensagem_decodificada
