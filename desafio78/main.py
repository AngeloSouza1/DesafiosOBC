def contar_caminhos(x, y, atual_x=0, atual_y=0, visitados=set()):
    """
    Conta o número de caminhos possíveis do ponto inicial (0, 0) ao destino (x, y),
    garantindo que caminhos duplicados não sejam contados.

    Args:
        x (int): Coordenada x do destino.
        y (int): Coordenada y do destino.
        atual_x (int): Coordenada x atual (inicia em 0).
        atual_y (int): Coordenada y atual (inicia em 0).
        visitados (set): Conjunto de coordenadas visitadas.

    Returns:
        int: Número total de caminhos possíveis sem cair em portais.
    """
    # Debug para rastrear a posição atual
    print(f"🔍 [DEBUG] Atual: ({atual_x}, {atual_y})")

    # Se atingir o destino
    if atual_x == x and atual_y == y:
        print(f"✅ [DESTINO ALCANÇADO] Coordenadas finais: ({atual_x}, {atual_y})")
        return 1

    # Portal de procrastinação
    if (atual_x + atual_y) % 3 == 0 and (atual_x, atual_y) != (0, 0):
        print(f"🚨 [PORTAL ATIVADO] Coordenadas somadas ({atual_x} + {atual_y}) são múltiplas de 3. Caminho inválido.")
        return 0

    # Conjunto de caminhos visitados
    if (atual_x, atual_y) in visitados:
        print(f"🔄 [CAMINHO DUPLICADO] Já visitado: ({atual_x}, {atual_y}). Ignorando.")
        return 0

    # Adiciona a posição atual ao conjunto de visitados
    visitados.add((atual_x, atual_y))

    # Inicializar contador de caminhos
    total_caminhos = 0

    # Movimento: Direita
    if atual_x + 1 <= x:
        total_caminhos += contar_caminhos(x, y, atual_x + 1, atual_y, visitados.copy())

    # Movimento: Cima
    if atual_y + 1 <= y:
        total_caminhos += contar_caminhos(x, y, atual_x, atual_y + 1, visitados.copy())

    # Movimento: Diagonal
    if atual_x + 1 <= x and atual_y + 1 <= y:
        total_caminhos += contar_caminhos(x, y, atual_x + 1, atual_y + 1, visitados.copy())

    # Debug para rastrear caminhos parciais
    print(f"🔢 [RESULTADO PARCIAL] Total de caminhos possíveis a partir de ({atual_x}, {atual_y}): {total_caminhos}")
    return total_caminhos


# Teste no script
if __name__ == "__main__":
    # Configuração do desafio
    x, y = 2, 2  # Coordenadas finais do destino
    print(f"Entrada: x = {x}, y = {y}")
    resultado = contar_caminhos(x, y)
    print(f"\n✅ Saída Final: {resultado}")
