from collections import deque
from typing import List, Tuple

def encontre_caminho(mapa: List[List[str]]) -> List[Tuple[int, int]]:
    linhas = len(mapa)
    colunas = len(mapa[0])
    
    heroi = None
    tesouro = None
    for i in range(linhas):
        for j in range(colunas):
            if mapa[i][j] == 'H':
                heroi = (i, j)
            elif mapa[i][j] == 'T':
                tesouro = (i, j)
    
    if not heroi or not tesouro:
        raise ValueError("A matriz deve conter um herói ('H') e um tesouro ('T').")
    
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    fila = deque([heroi])
    visitados = set()
    visitados.add(heroi)
    caminho = {heroi: None}
    
    while fila:
        atual = fila.popleft()
        if atual == tesouro:
            caminho_final = []
            while atual:
                caminho_final.append(atual)
                atual = caminho[atual]
            return caminho_final[::-1]
        
        for dx, dy in movimentos:
            nx, ny = atual[0] + dx, atual[1] + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and mapa[nx][ny] != '#' and (nx, ny) not in visitados:
                fila.append((nx, ny))
                visitados.add((nx, ny))
                caminho[(nx, ny)] = atual
    
    return []
