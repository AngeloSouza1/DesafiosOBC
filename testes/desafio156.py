def monstro_mais_forte(monstros):
    
    danos = {}
    
    for monstro in monstros:
        total = sum(monstro['ataques'])
        danos[monstro['nome']] = total
    
    maior_dano = max(danos.values())
    

    vencedores = [nome for nome, dano in danos.items() if dano == maior_dano]
    
    return vencedores[0] if len(vencedores) == 1 else vencedores


monstros1 = [
    {'nome': 'Goblin', 'ataques': [10, 12, 8]},
    {'nome': 'Orc', 'ataques': [15, 20]},
    {'nome': 'Dragão', 'ataques': [20, 15, 25]}
]
print(monstro_mais_forte(monstros1))  # Saída: 'Dragão'

monstros2 = [
    {'nome': 'Goblin', 'ataques': [10, 20]},
    {'nome': 'Orc', 'ataques': [15, 15]},
    {'nome': 'Troll', 'ataques': [10, 20]}
]
print(monstro_mais_forte(monstros2))  # Saída: ['Goblin', 'Troll']
