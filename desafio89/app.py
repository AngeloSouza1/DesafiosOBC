from itertools import combinations

def descobrir_combinacao(energias, chave_portal):
    resultados = []

    print(f"\n🚀 [INICIANDO BUSCA] Energias disponíveis: {energias}")
    print(f"🔑 [OBJETIVO] Encontrar combinações que somam {chave_portal}\n")

    # Gerar todas as combinações possíveis de 2 até o tamanho da lista
    for i in range(2, len(energias) + 1):
        for combinacao in combinations(energias, i):
            soma_atual = sum(combinacao)
            print(f"🔍 [TESTANDO] Combinação: {combinacao} -> Soma: {soma_atual}")

            if soma_atual == chave_portal:
                print(f"✅ [VÁLIDA] Adicionando combinação: {combinacao}")
                resultados.append(sorted(combinacao))  # Ordenar os elementos dentro da combinação

    # Ordenar as combinações primeiro pelo tamanho e depois pelo valor
    print("\n📌 [ORDENANDO] Organizando combinações pelo tamanho e soma dos valores")
    resultados = sorted(resultados, key=lambda x: (len(x), x))

    print(f"🔄 [ORDENADO] Lista de combinações antes da filtragem: {resultados}")

    # Filtrar para manter apenas as menores combinações possíveis
    combinacoes_filtradas = []
    valores_usados = set()

    print("\n🔍 [FILTRAGEM] Eliminando combinações maiores que já possuem subconjuntos válidos")

    for combinacao in resultados:
        if not any(set(combinacao).issubset(set(c)) for c in combinacoes_filtradas):
            print(f"✅ [APROVADO] Mantendo: {combinacao}")
            combinacoes_filtradas.append(combinacao)
            valores_usados.update(combinacao)
        else:
            print(f"❌ [DESCARTADO] {combinacao} já está contido em {combinacoes_filtradas}")

    print("\n🚀 [FINALIZADO] Lista final de combinações possíveis:")
    for combinacao in combinacoes_filtradas:
        print(f"✨ {combinacao}")

    return combinacoes_filtradas

# 🔥 **Teste**
energias = [2, 4, 6, 10, 8]
chave_portal = 16
resultado = descobrir_combinacao(energias, chave_portal)
print("\n🔑 Combinacoes encontradas:", resultado)
