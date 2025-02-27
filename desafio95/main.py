def calcular_tempo_jornada(jornada):
    """
    Calcula o tempo total da jornada de Pyro, somando os tempos de cada região.
    
    Args:
        jornada (list): Lista de dicionários com 'regiao', 'clima' e 'distancia'.
        
    Returns:
        float: Tempo total da jornada (em horas).
    """
    # Mapeamento das condições meteorológicas para velocidades (km/h)
    velocidades = {
        "ensolarado": 10,
        "chuva": 7,
        "neblina": 5,
        "tempestade": 2
    }
    
    tempo_total = 0.0

    print("\n🔍 [DEBUG] Iniciando o cálculo da jornada:")
    for regiao in jornada:
        clima = regiao["clima"]
        distancia = regiao["distancia"]
        velocidade = velocidades.get(clima, 0)
        if velocidade == 0:
            print(f"⚠️ [ALERTA] Clima desconhecido: {clima}. Região ignorada.")
            continue

        tempo_regiao = distancia / velocidade
        print(f"🔍 [DEBUG] Região: {regiao['regiao']:<25} | Clima: {clima:<10} | Distância: {distancia:>3} km | "
              f"Velocidade: {velocidade:>2} km/h | Tempo: {tempo_regiao:>5.2f} h")
        tempo_total += tempo_regiao

    return tempo_total


# Exemplo de entrada
jornada = [
    {"regiao": "Floresta Encantada", "clima": "neblina", "distancia": 20},
    {"regiao": "Deserto Ardente", "clima": "ensolarado", "distancia": 30},
    {"regiao": "Planície Tempestuosa", "clima": "tempestade", "distancia": 15},
    {"regiao": "Pântano das Sombras", "clima": "chuva", "distancia": 12}
]

tempo_total = calcular_tempo_jornada(jornada)
print(f"\nPyro completou sua jornada em {tempo_total:.2f} horas!")
