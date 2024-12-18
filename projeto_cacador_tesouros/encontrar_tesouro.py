# encontrar_tesouro.py

def encontrar_caminho_ate_tesouro(mapa):
    """
    Encontra o caminho mais curto até o tesouro em um mapa de coordenadas.

    Parâmetros:
    - mapa (list): Lista de tuplas representando as coordenadas (x, y).

    Retorna:
    - list: Lista de tuplas com o caminho até o tesouro.
    """
    # Lista para armazenar o caminho percorrido
    caminho = []

    # Ponto de partida é a primeira coordenada
    x_atual, y_atual = mapa[0]
    x_destino, y_destino = mapa[-1]

    # Enquanto não chegarmos ao destino, vamos nos mover passo a passo
    while (x_atual, y_atual) != (x_destino, y_destino):
        caminho.append((x_atual, y_atual))
        
        # Decidir o próximo passo em direção ao destino
        if x_atual < x_destino:
            x_atual += 1
        elif x_atual > x_destino:
            x_atual -= 1
        
        if y_atual < y_destino:
            y_atual += 1
        elif y_atual > y_destino:
            y_atual -= 1

    # Adiciona a coordenada final (o destino)
    caminho.append((x_destino, y_destino))

    return caminho
