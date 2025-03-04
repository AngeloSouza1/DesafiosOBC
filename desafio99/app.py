import tkinter as tk

# Labirinto do desafio
maze = [
    ['#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '#'],
    ['#', '#', '.', '#', '#'],
    ['#', '.', '.', 'E', '#'],
    ['#', '#', '#', '#', '#']
]

def find_path(maze):
    """
    Encontra o caminho mais curto no labirinto usando DFS.
    O labirinto é uma matriz de caracteres onde:
      - 'S' é o ponto de partida,
      - 'E' é o ponto de saída,
      - '#' são paredes intransponíveis,
      - '.' são caminhos válidos.
    Retorna uma lista de coordenadas (tuplas) do caminho encontrado ou None se não houver solução.
    """
    rows = len(maze)
    cols = len(maze[0])
    start, end = None, None

    # Procura as posições de 'S' e 'E'
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    
    if start is None or end is None:
        return None

    def dfs(i, j, path, visited):
        if (i, j) == end:
            return path
        visited.add((i, j))
        # Movimentos permitidos: cima, baixo, esquerda, direita
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] != '#' and (ni, nj) not in visited:
                res = dfs(ni, nj, path + [(ni, nj)], visited)
                if res is not None:
                    return res
        visited.remove((i, j))
        return None

    return dfs(start[0], start[1], [start], set())

class LabyrinthSolverGUI:
    def __init__(self, root, maze):
        self.root = root
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        
        self.root.title("O Labirinto do Encantador de Códigos")
        self.root.geometry("600x600")
        self.root.configure(bg="#1e1e2f")
        
        # Área para exibir o labirinto usando emojis
        # Usaremos emojis para dar um visual mais legal:
        # '#' -> 🧱, 'S' -> 🏴‍☠️, 'E' -> 🚪, '.' -> 👣
        self.EMOJIS = {
            '#': '🧱',
            'S': '🏴‍☠️',
            'E': '🚪',
            '.': '👣'
        }
        self.canvas = tk.Canvas(root, width=self.cols * 80, height=self.rows * 80, bg="#2e2e3e")
        self.canvas.pack(pady=20)
        self.draw_maze()
        
        # Botão para resolver o labirinto
        self.button_resolver = tk.Button(root, text="Resolver Labirinto", command=self.resolver_labirinto, font=("Arial", 14), bg="#4CAF50", fg="white")
        self.button_resolver.pack(pady=10)
        
        # Label para exibir o resultado (mensagem e caminho)
        self.label_result = tk.Label(root, text="", font=("Arial", 16), bg="#1e1e2f", fg="#ffeb3b")
        self.label_result.pack(pady=10)
    
    def draw_maze(self):
        """Desenha o labirinto no canvas utilizando emojis."""
        self.canvas.delete("all")
        cell_size = 80
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * cell_size
                y = i * cell_size
                self.canvas.create_rectangle(x, y, x+cell_size, y+cell_size, outline="black", width=2)
                char = self.maze[i][j]
                emoji = self.EMOJIS.get(char, char)
                self.canvas.create_text(x + cell_size/2, y + cell_size/2, text=emoji, font=("Arial", 40))
    
    def draw_path(self, path):
        """Desenha o caminho encontrado sobre o labirinto."""
        cell_size = 80
        # Desenha círculos sobre as células do caminho
        for (i, j) in path:
            x = j * cell_size + cell_size/2
            y = i * cell_size + cell_size/2
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="yellow", outline="orange", width=3)
    
    def resolver_labirinto(self):
        """Encontra o caminho mais curto e atualiza a interface com o resultado."""
        path = find_path(self.maze)
        if path:
            self.draw_maze()  # Redesenha o labirinto para limpar caminhos anteriores
            self.draw_path(path)
            self.label_result.config(text=f"Você chegou ao tesouro!\nCaminho: {path}")
        else:
            self.label_result.config(text="Nenhum caminho encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = LabyrinthSolverGUI(root, maze)
    root.mainloop()
