import heapq

def encontrar_rota_mais_rapida(rotas, origem, destino):
    # Criar um grafo a partir das rotas fornecidas
    grafo = {}
    for rota in rotas:
        if rota["origem"] not in grafo:
            grafo[rota["origem"]] = []
        if rota["destino"] not in grafo:
            grafo[rota["destino"]] = []
        grafo[rota["origem"]].append((rota["tempo"], rota["destino"]))
        grafo[rota["destino"]].append((rota["tempo"], rota["origem"]))  # Supondo que as viagens sejam bidirecionais

    # Implementação do algoritmo de Dijkstra usando uma fila de prioridade (heap)
    fila_prioridade = [(0, origem, [origem])]  # (tempo_acumulado, planeta, caminho_percorrido)
    tempos_minimos = {planeta: float('inf') for planeta in grafo}
    tempos_minimos[origem] = 0

    while fila_prioridade:
        tempo_atual, planeta_atual, caminho_atual = heapq.heappop(fila_prioridade)

        if planeta_atual == destino:
            return tempo_atual, caminho_atual  # Retorna tempo e rota percorrida

        for tempo_viagem, vizinho in grafo[planeta_atual]:
            novo_tempo = tempo_atual + tempo_viagem
            if novo_tempo < tempos_minimos[vizinho]:
                tempos_minimos[vizinho] = novo_tempo
                heapq.heappush(fila_prioridade, (novo_tempo, vizinho, caminho_atual + [vizinho]))

    return -1, []  # Se não houver rota possível

# 🚀 Teste com os dados fornecidos
rotas = [
    {"origem": "Terra", "destino": "Marte", "tempo": 5},
    {"origem": "Marte", "destino": "Júpiter", "tempo": 4},
    {"origem": "Terra", "destino": "Júpiter", "tempo": 15},
    {"origem": "Júpiter", "destino": "Saturno", "tempo": 3},
    {"origem": "Marte", "destino": "Saturno", "tempo": 8}
]

origem = "Terra"
destino = "Saturno"

tempo_minimo, caminho = encontrar_rota_mais_rapida(rotas, origem, destino)

# 🌌 Exibição formatada do resultado
print("\n🚀 Missão Espacial: Encontrando a Rota Mais Rápida! 🌌")
print(f"🪐 Planeta de Origem: {origem}")
print(f"🌍 Planeta de Destino: {destino}\n")

if tempo_minimo != -1:
    caminho_formatado = " -> ".join(caminho)
    print(f"⏳ Tempo mínimo necessário: {tempo_minimo} unidades de tempo 💫")
    print(f"🗺️ Rota percorrida: {caminho_formatado}\n")
    print(f"🔹 Saída: {tempo_minimo} (Viagem de {caminho_formatado})")
else:
    print("⚠️ Nenhuma rota disponível entre os planetas! 🛑")
