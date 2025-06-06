import tkinter as tk
from tkinter import messagebox
from copy import deepcopy
import time
import threading

labirinto = [
    ['E', '.', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '#'],
    ['#', '#', '.', '#', '.', 'S'],
    ['#', '.', '#', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#'],
]

CELL_SIZE = 50
VELOCIDADE = 0.25  

class LabirintoApp:
    def __init__(self, root, lab):
        self.root = root
        self.lab = lab
        self.n = len(lab)
        self.m = len(lab[0])
        self.canvas = tk.Canvas(root, width=self.m * CELL_SIZE, height=self.n * CELL_SIZE)
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Iniciar Jornada 🧙‍♂️", command=self.iniciar_resolucao)
        self.start_button.pack(pady=10)

        self.resultado_label = tk.Label(root, text="", font=("Courier", 12), justify="center")
        self.resultado_label.pack(pady=10)

        self.desenhar_labirinto()

    def desenhar_labirinto(self):
        self.canvas.delete("all")
        self.rects = [[None]*self.m for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                x0, y0 = j * CELL_SIZE, i * CELL_SIZE
                x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
                cor = self.get_cor(self.lab[i][j])
                self.rects[i][j] = self.canvas.create_rectangle(x0, y0, x1, y1, fill=cor, outline='gray')
                if self.lab[i][j] in ('E', 'S'):
                    self.canvas.create_text((x0 + x1)//2, (y0 + y1)//2, text=self.lab[i][j], font=('Arial', 16, 'bold'))

    def get_cor(self, val):
        return {
            'E': 'green',
            'S': 'red',
            '.': 'white',
            '#': 'black',
            '◉': 'blue',
            '*': 'yellow'  
        }.get(val, 'white')

    def iniciar_resolucao(self):
        thread = threading.Thread(target=self.resolver_com_animacao)
        thread.start()

    def resolver_com_animacao(self):
        n, m = self.n, self.m
        visitado = [[False]*m for _ in range(n)]
        caminho = []

        for i in range(n):
            for j in range(m):
                if self.lab[i][j] == 'E':
                    entrada = (i, j)

        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m): return False
            if self.lab[x][y] == '#' or visitado[x][y]: return False

            visitado[x][y] = True
            caminho.append((x, y))

            if self.lab[x][y] not in ('E', 'S'):
                self.lab[x][y] = '*'
                self.atualizar_visual()
                time.sleep(VELOCIDADE)

            if self.lab[x][y] == 'S':
                return True

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                if dfs(x + dx, y + dy):
                    return True

            if self.lab[x][y] == '*':
                self.lab[x][y] = '.'
                self.atualizar_visual()
                time.sleep(VELOCIDADE / 2)

            caminho.pop()
            return False

        if dfs(*entrada):
            for x, y in caminho:
                if self.lab[x][y] not in ('E', 'S'):
                    self.lab[x][y] = '◉'
            self.atualizar_visual()

            caminho_str = "🧭 Caminho mágico encontrado:\n" + str(caminho)
            self.resultado_label.config(text=caminho_str)
        else:
            messagebox.showinfo("Falha!", "Nenhum caminho encontrado!")
            self.resultado_label.config(text="🛑 Nenhum caminho foi encontrado.")

    def atualizar_visual(self):
        for i in range(self.n):
            for j in range(self.m):
                cor = self.get_cor(self.lab[i][j])
                self.canvas.itemconfig(self.rects[i][j], fill=cor)
        self.root.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Labirinto Encantado 🧱🔮 - Visual + Resultado")
    app = LabirintoApp(root, deepcopy(labirinto))
    root.mainloop()
