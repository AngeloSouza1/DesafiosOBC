import tkinter as tk
from collections import deque

def find_shortest_path(maze):
    """
    Encontra o caminho mais curto em um labirinto de caracteres usando BFS.
    
    O labirinto é uma matriz onde:
      - 'S' é o ponto de partida,
      - 'E' é o ponto de saída,
      - '#' são paredes intransponíveis,
      - '.' são caminhos válidos.
    
    Retorna uma lista de coordenadas (tuplas) do caminho encontrado ou uma lista vazia se não houver solução.
    """
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    start, end = None, None

    # Encontrar as posições de 'S' e 'E'
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if start is None or end is None:
        return []

    # BFS para encontrar o caminho mais curto
    queue = deque([(start, [start])])
    visited = {start}

    # Movimentos permitidos: cima, baixo, esquerda, direita
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] in ('.', 'E') and (nx, ny) not in visited:
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
        
        # Área de exibição do labirinto (texto simples)
        self.text_maze = tk.Text(root, width=30, height=self.rows, font=("Courier", 14))
        self.text_maze.pack(pady=10)
        self.display_maze()
        
        # Botão para resolver o labirinto
        self.button_resolver = tk.Button(root, text="Resolver", command=self.resolver_labirinto, font=("Arial", 12))
        self.button_resolver.pack(pady=5)
        
        # Área para exibir o resultado (caminho encontrado)
        self.label_result = tk.Label(root, text="", font=("Arial", 14))
        self.label_result.pack(pady=10)
    
    def display_maze(self):
        """Exibe o labirinto no widget Text."""
        self.text_maze.delete("1.0", tk.END)
        for row in self.maze:
            self.text_maze.insert(tk.END, " ".join(row) + "\n")
    
    def resolver_labirinto(self):
        """Encontra e exibe o caminho mais curto para sair do labirinto."""
        path = find_shortest_path(self.maze)
        if path:
            self.label_result.config(text=f"Caminho encontrado:\n{path}")
        else:
            self.label_result.config(text="Nenhum caminho encontrado.")

if __name__ == "__main__":
    # Labirinto do desafio
    maze = [
        ['#', '#', '#', '#', '#'],
        ['#', 'S', '.', '.', '#'],
        ['#', '#', '.', '#', '#'],
        ['#', '.', '.', 'E', '#'],
        ['#', '#', '#', '#', '#']
    ]
    
    root = tk.Tk()
    gui = LabyrinthGUI(root, maze)
    root.mainloop()
