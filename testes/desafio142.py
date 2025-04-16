def traduzir_emocao(vilarejo, frase):
    mapa_emocoes = {
        'alegria': {
            'Bom dia!': '🌞🎉',
            'Como vai você?': '🤗🎈',
            'Até logo!': '👋💖'
        },
        'tristeza': {
            'Bom dia!': '🌧️☔',
            'Como vai você?': '😔🥀',
            'Até logo!': '👋🖤'
        }
    }

    vila = mapa_emocoes.get(vilarejo.lower())
    if not vila:
        return "❌ Vilarejo desconhecido."

    traducao = vila.get(frase)
    if not traducao:
        return "❓ Frase não encontrada na vila."

    return traducao

# Exemplos de uso:
print(traduzir_emocao('alegria', 'Bom dia!'))        # 🌞🎉
print(traduzir_emocao('tristeza', 'Até logo!'))      # 👋🖤
print(traduzir_emocao('alegria', 'Como vai você?'))  # 🤗🎈
