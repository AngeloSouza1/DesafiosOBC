import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from busca_tesouro import encontrar_menor_caminho

def mostrar_ilha_graficamente(ilha, caminho, total_passos):
    # Mapear os símbolos para números (para criar uma matriz numérica)
    simbolo_para_numero = {
        'P': 1,  # Ponto de partida
        'T': 2,  # Tesouro
        '~': 3,  # Terra comum
        'X': 4,  # Mar
    }

    # Criar a matriz numérica da ilha
    matriz = np.array([[simbolo_para_numero[celula] for celula in linha] for linha in ilha])

    # Aplicar os passos no caminho
    for (x, y) in caminho:
        if ilha[x][y] == '~':
            matriz[x][y] = 5  # Representação numérica dos passos percorridos

    # Garantir que o ponto de partida 'P' e o tesouro 'T' sejam mantidos
    inicio_x, inicio_y = caminho[0]
    fim_x, fim_y = caminho[-1]
    matriz[inicio_x][inicio_y] = 1
    matriz[fim_x][fim_y] = 2

    # Definir o mapa de cores para os elementos
    colors = ['#6a0dad', '#006400', '#ffffff', '#00008b', '#ffd700']  # Cores para P, T, ~, X, passos
# ff8c00
    # Criar o colormap usando ListedColormap
    cmap = ListedColormap(colors)

    # Plotar a matriz usando imshow
    plt.figure(figsize=(10, 10))
    plt.imshow(matriz, cmap=cmap, interpolation='nearest')

    # Adicionar os símbolos no centro das células
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if (i, j) == (inicio_x, inicio_y):
                plt.text(j, i, 'P', ha='center', va='center', fontsize=14, color='white', weight='bold')
            elif (i, j) == (fim_x, fim_y):
                plt.text(j, i, 'T', ha='center', va='center', fontsize=14, color='white', weight='bold')
            elif ilha[i][j] == 'X':
                plt.text(j, i, 'X', ha='center', va='center', fontsize=13, color='white')
            elif ilha[i][j] == '~':
                plt.text(j, i, '~', ha='center', va='center', fontsize=12, color='black')

    # Adicionar título e legenda
    plt.title(f'Total de Passos: {total_passos}', fontsize=16, weight='bold')
    plt.axis('off')
    plt.show()

def main():
    # Matriz com caminho garantido do ponto de partida até o tesouro
    ilha = [
        ['P', '~', '~', '~', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', '~', '~', '~', 'X', 'X', 'X', 'X'],
        ['X', '~', '~', '~', 'X', '~', '~', '~', '~', 'X'],
        ['X', '~', 'X', '~', 'X', 'X', 'X', '~', 'X', 'X'],
        ['X', '~', 'X', '~', '~', '~', 'X', '~', '~', 'X'],
        ['X', '~', 'X', 'X', 'X', '~', 'X', 'X', '~', 'X'],
        ['X', '~', '~', '~', 'X', '~', '~', '~', '~', 'X'],
        ['X', 'X', 'X', '~', 'X', 'X', 'X', 'X', '~', 'X'],
        ['X', '~', '~', '~', '~', '~', '~', '~', '~', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'T', 'X']
    ]

    # Encontrar o número mínimo de passos e o caminho
    resultado, caminho = encontrar_menor_caminho(ilha)

    # Mostrar a ilha graficamente com os passos
    mostrar_ilha_graficamente(ilha, caminho, resultado)

    if resultado != -1:
        print(f"Número mínimo de passos: {resultado}")
    else:
        print("O tesouro não pode ser alcançado.")

if __name__ == "__main__":
    main()
