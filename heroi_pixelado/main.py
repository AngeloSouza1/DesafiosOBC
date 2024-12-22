import os
from collections import deque

def limpar_tela():
    """Limpa a tela no terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_mapa(mapa):
    """Função para imprimir o mapa de forma mais apresentável."""
    print("+" + "-" * (len(mapa[0]) * 2 - 1) + "+")
    for linha in mapa:
        print("|" + " ".join(str(celula) for celula in linha) + "|")
    print("+" + "-" * (len(mapa[0]) * 2 - 1) + "+")

def pode_alcancar_espada(mapa):
    # Encontrar a posição inicial do herói e a espada
    heroi_pos = None
    espada_pos = None
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == 'H':
                heroi_pos = (i, j)
            elif mapa[i][j] == 'S':
                espada_pos = (i, j)
    
    if not heroi_pos or not espada_pos:
        return "Mapa inválido: O herói ou a espada não foram encontrados."

    rows, cols = len(mapa), len(mapa[0])
    visited = set()
    queue = deque([heroi_pos])
    visited.add(heroi_pos)
    
    def move_until_wall(x, y, dx, dy):
        """Move o herói em linha reta até encontrar uma parede."""
        while True:
            nx, ny = (x + dx) % rows, (y + dy) % cols
            if mapa[nx][ny] == 1 or (nx, ny) in visited:  # Parar antes de uma parede ou local já visitado
                break
            x, y = nx, ny
        return x, y
    
    # BFS para explorar o mapa
    while queue:
        x, y = queue.popleft()
        
        # Checar se chegou à espada
        if (x, y) == espada_pos:
            return "Herói alcançou a espada!"
        
        # Tentar todas as 4 direções
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = move_until_wall(x, y, dx, dy)
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return "Herói não conseguiu alcançar a espada."

# Limpar a tela antes de executar
limpar_tela()

# Teste do exemplo fornecido
mapa = [
    [0, 1, 0, 0, 0],
    ['H', 1, 'S', 1, 0],
    [0, 1, 0, 0, 0]
]

# Exibir o mapa inicial
print("Mapa Inicial:")
imprimir_mapa(mapa)

# Testar a função
resultado = pode_alcancar_espada(mapa)
print("\nResultado:")
print(resultado)

# Pausar o programa até que o usuário pressione Enter
input("\nPressione Enter para sair...")
