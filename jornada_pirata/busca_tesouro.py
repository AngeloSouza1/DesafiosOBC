from collections import deque

def encontrar_menor_caminho(ilha):
    linhas, colunas = len(ilha), len(ilha[0])
    inicio = None

    # Encontrar a posição inicial 'P'
    for i in range(linhas):
        for j in range(colunas):
            if ilha[i][j] == 'P':
                inicio = (i, j)
                break
        if inicio:
            break

    if not inicio:
        return -1, []

    # Movimentos possíveis (direita, baixo, esquerda, cima)
    movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    fila = deque([(inicio[0], inicio[1], 0, [inicio])])
    visitados = set([inicio])

    while fila:
        x, y, passos, caminho = fila.popleft()

        # Se encontramos o tesouro 'T', retornamos o número de passos e o caminho
        if ilha[x][y] == 'T':
            return passos, caminho

        # Explorar os movimentos possíveis
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy

            if 0 <= nx < linhas and 0 <= ny < colunas and (nx, ny) not in visitados:
                if ilha[nx][ny] != 'X':
                    visitados.add((nx, ny))
                    fila.append((nx, ny, passos + 1, caminho + [(nx, ny)]))

    return -1, []
