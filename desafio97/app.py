import tkinter as tk
from collections import deque

# Labirinto fixo conforme o enunciado
maze = [
    ['#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '#'],
    ['#', '#', '.', '#', '#'],
    ['#', '.', '.', 'E', '#'],
    ['#', '#', '#', '#', '#']
]

# Emojis para representar cada elemento do labirinto
EMOJIS = {
    '#': '🧱',  # Paredes
    '.': '👣',  # Caminho
    'S': '🏁',  # Início
    'E': '🚪'   # Saída
}

# Tamanho da célula em pixels
CELL_SIZE = 70

def find_shortest_path(maze):
    """
    Encontra o caminho mais curto no labirinto usando BFS.
    Retorna uma lista de coordenadas do caminho (tuplas).
    """
    rows = len(maze)
    cols = len(maze[0])
    start, end = None, None

    # Encontrar a posição de 'S' (start) e 'E' (exit)
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if start is None or end is None:
        return []

    queue = deque([(start, [start])])
    visited = {start}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and 
                maze[nx][ny] in ('.', 'E') and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return []

class LabyrinthGUI:
    def __init__(self, root, maze):
        self.root = root
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        
        self.root.title("O Labirinto do Encantador de Códigos")
        self.root.geometry("600x600")
        
        # Canvas para desenhar o labirinto
        self.canvas = tk.Canvas(root, width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE, bg="white")
        self.canvas.pack(pady=20)
        
        # Botão para resolver o labirinto
        self.button_resolver = tk.Button(root, text="Resolver Labirinto", command=self.resolver_labirinto, font=("Arial", 14))
        self.button_resolver.pack(pady=10)
        
        # Label para exibir o caminho encontrado
        self.label_result = tk.Label(root, text="", font=("Arial", 16))
        self.label_result.pack(pady=10)
        
        self.draw_maze()
    
    def draw_maze(self):
        """Desenha o labirinto no canvas utilizando emojis."""
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * CELL_SIZE
                y = i * CELL_SIZE
                # Desenha um retângulo para delimitar a célula
                self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, outline="black")
                emoji = EMOJIS.get(self.maze[i][j], '?')
                self.canvas.create_text(x + CELL_SIZE / 2, y + CELL_SIZE / 2, text=emoji, font=("Arial", 32))
    
    def draw_path(self, path):
        """Destaca o caminho encontrado, sobrepondo um fundo amarelo sem sobrescrever os emojis."""
        for (i, j) in path:
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            # Desenha um retângulo sem borda para destacar a célula
            self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="yellow", stipple="gray50")
            # Redesenha o emoji para manter a representação do labirinto
            emoji = EMOJIS.get(self.maze[i][j], '?')
            self.canvas.create_text(x + CELL_SIZE / 2, y + CELL_SIZE / 2, text=emoji, font=("Arial", 32))
    
    def resolver_labirinto(self):
        """Encontra o caminho mais curto e atualiza a interface com o caminho e uma mensagem."""
        path = find_shortest_path(self.maze)
        if path:
            self.draw_path(path)
            self.label_result.config(text=f"Caminho encontrado:\n{path}")
        else:
            self.label_result.config(text="Nenhum caminho encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = LabyrinthGUI(root, maze)
    root.mainloop()
