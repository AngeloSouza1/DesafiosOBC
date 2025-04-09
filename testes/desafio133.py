def gerar_nome_super_heroi(nome, poder):
    # Garante que nome e poder tenham pelo menos 3 caracteres
    parte_nome = nome[:3] if len(nome) >= 3 else nome
    parte_poder = poder[-3:] if len(poder) >= 3 else poder

    nome_heroi = parte_nome + parte_poder
    return nome_heroi

# Exemplos:
print(gerar_nome_super_heroi("Miguel", "Invisibilidade"))  # 'Migade'
print(gerar_nome_super_heroi("Ana", "Fogo"))               # 'Anago'
print(gerar_nome_super_heroi("Lu", "Ar"))                  # 'Luar'
