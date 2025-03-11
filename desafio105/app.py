import string

def decodificar_mensagem(mensagem, deslocamento):
    alfabeto = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    mensagem_decodificada = ""
    explicacao = []

    for char in mensagem:
        if char in alfabeto:
            nova_posicao = (alfabeto.index(char) - deslocamento) % len(alfabeto)
            mensagem_decodificada += alfabeto[nova_posicao]
            explicacao.append(f"🔠 '{char}' → '{alfabeto[nova_posicao]}' (deslocado {deslocamento} posições para trás)")
        else:
            mensagem_decodificada += char  # Mantém os espaços inalterados
            explicacao.append(f"⏳ '{char}' (espaço inalterado)")

    return mensagem_decodificada, explicacao

# 🔥 Teste com exemplo fornecido
mensagem_codificada = "oz rdfn"
deslocamento = 3

resultado, detalhes = decodificar_mensagem(mensagem_codificada, deslocamento)

# 🎯 Exibição do resultado com explicação detalhada
print("\n✨ Decodificação da mensagem mágica 🔮✨")
print(f"📜 Mensagem codificada: {mensagem_codificada}")
print(f"🔢 Deslocamento: {deslocamento}\n")
print("📖 Processo de decodificação:")
for detalhe in detalhes:
    print(detalhe)
print("\n✅ Mensagem original decifrada: " + resultado)
