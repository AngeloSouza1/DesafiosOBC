def calcular_mana(mago):
    mana = mago['mana_inicial']
    regeneracao = mago['regeneracao_por_minuto']
    tempo_entre = mago['tempo_entre_lançamentos']
    
    for feitiço in mago['feitiços']:
        if mana < feitiço['custo']:
            return 'Não'
        mana -= feitiço['custo']
        mana += regeneracao * tempo_entre
    
    return 'Sim'

# Exemplos de uso
testes = [
    {
        'mana_inicial': 50,
        'regeneracao_por_minuto': 10,
        'feitiços': [
            {'nome': 'bola_de_fogo', 'custo': 20},
            {'nome': 'escudo_magico', 'custo': 15},
            {'nome': 'cura', 'custo': 25}
        ],
        'tempo_entre_lançamentos': 1,
        'esperado': 'Sim'
    },
    {
        'mana_inicial': 30,
        'regeneracao_por_minuto': 5,
        'feitiços': [
            {'nome': 'raio', 'custo': 15},
            {'nome': 'explosao', 'custo': 20}
        ],
        'tempo_entre_lançamentos': 2,
        'esperado': 'Não'
    },
    {
        'mana_inicial': 100,
        'regeneracao_por_minuto': 20,
        'feitiços': [
            {'nome': 'escudo', 'custo': 40},
            {'nome': 'cura', 'custo': 50},
            {'nome': 'espada_arcana', 'custo': 30}
        ],
        'tempo_entre_lançamentos': 1,
        'esperado': 'Sim'
    }
]

print("\U0001F9D9✨ A Jornada do Mago: Calculando a Mana ✨\U0001F9D9\n")
print("==============================================")

for i, teste in enumerate(testes, 1):
    resultado = calcular_mana(teste)
    print(f"🔮 Teste {i}:")
    print(f"   🔢 Mana Inicial: {teste['mana_inicial']}")
    print(f"   ⚡ Regeneração por Minuto: {teste['regeneracao_por_minuto']}")
    print(f"   ⏳ Tempo entre Lançamentos: {teste['tempo_entre_lançamentos']} min")
    print(f"   🧙 Feitiços: {[f['nome'] + ' (' + str(f['custo']) + ' mana)' for f in teste['feitiços']]}")
    print(f"   ✅ Pode lançar todos os feitiços? {resultado}")
    print(f"   🎯 Resultado esperado: {teste['esperado']}")
    print("----------------------------------------------")

print("==============================================\n")
print("📖 Prepare seu grimoire e boa sorte, nobre mago! 🧙‍♂️")
