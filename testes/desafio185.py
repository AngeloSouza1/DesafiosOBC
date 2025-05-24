def decodificar_mensagem(codigos):
    return ''.join(chr(n + 64) for n in codigos if n != 0)


print(decodificar_mensagem([8, 1, 18, 4, 0, 9, 16, 0, 18, 9, 4]))


print(decodificar_mensagem([8, 5, 12, 12, 15, 0, 23, 15, 18, 12, 4]))

