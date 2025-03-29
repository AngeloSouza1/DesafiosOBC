def decode_sinal(sinal_binario):
    mensagem_original = sinal_binario[::-1]
    print(f"🛰️ Sinal recebido: {sinal_binario}")
    print(f"📡 Sinal decodificado: {mensagem_original}")
    return mensagem_original


sinal = '1101001'
resultado = decode_sinal(sinal)

