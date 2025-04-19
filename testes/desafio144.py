def verificar_saida_masmorra(palavra):
    soma_ascii = sum(ord(c) for c in palavra)
    print(f"🔍 Soma dos valores ASCII: {soma_ascii}")
    
    if soma_ascii % 2 == 0:
        return "✅ Porta aberta! Você escapou da masmorra! 🗝️🚪"
    else:
        return "❌ Tente novamente! A soma é ímpar... ⚙️🔒"

entrada = "escape"
resultado = verificar_saida_masmorra(entrada)
print(resultado)
