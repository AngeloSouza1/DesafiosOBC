import tkinter as tk
from collections import deque
import time

# Labirinto padrão
labirinto_default = [
    ['#', 'S', '.', '.'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', '#'],
    ['.', '#', 'E', '#']
]

# Tamanho de cada célula do labirinto
TAMANHO_CELULA = 50

# Emojis para representar os elementos do labirinto
EMOJIS = {
    '#': '🧱',  # Parede
    '.': '👣',  # Caminho livre
    'S': '🏳️',  # Início
    'E': '🌌',  # Saída
    'C': '🔵'   # Caminho percorrido (destacado)
}

class LabirintoGUI:
    def __init__(self, root, labirinto):
        self.root = root
        self.labirinto = labirinto
        self.rows = len(labirinto)
        self.cols = len(labirinto[0])
        
        # Criar canvas para desenhar o labirinto
        self.canvas = tk.Canvas(root, width=self.cols * TAMANHO_CELULA, height=self.rows * TAMANHO_CELULA)
        self.canvas.pack()

        # Campo de texto para entrada do labirinto
        self.text_input = tk.Text(root, height=5, width=40)
        self.text_input.pack(pady=10)
        labirinto_str = "\n".join(["".join(row) for row in self.labirinto])
        self.text_input.insert("1.0", labirinto_str)

        # Botão para carregar o labirinto
        self.botao_carregar = tk.Button(root, text="Carregar Labirinto", command=self.carregar_labirinto)
        self.botao_carregar.pack(pady=5)

        # Label para exibir o caminho encontrado
        self.label_resultado = tk.Label(root, text="", font=("Arial", 14))
        self.label_resultado.pack(pady=10)

        # Botão para resolver o labirinto
        self.botao_resolver = tk.Button(root, text="Resolver", command=self.resolver_labirinto)
        self.botao_resolver.pack(pady=5)

        self.desenhar_labirinto()

    def carregar_labirinto(self):
        """Lê o input de texto e atualiza o labirinto."""
        text = self.text_input.get("1.0", "end").strip()
        linhas = text.split("\n")
        novo_labirinto = []
        for linha in linhas:
            # Remove espaços e converte cada linha em uma lista de caracteres
            row = list(linha.replace(" ", ""))
            if row:
                novo_labirinto.append(row)
        if novo_labirinto:
            self.labirinto = novo_labirinto
            self.rows = len(novo_labirinto)
            self.cols = len(novo_labirinto[0])
            self.canvas.config(width=self.cols * TAMANHO_CELULA, height=self.rows * TAMANHO_CELULA)
            self.desenhar_labirinto()
            self.label_resultado.config(text="Labirinto carregado!")
        else:
            self.label_resultado.config(text="Erro: Labirinto inválido!")

    def desenhar_labirinto(self):
        """Desenha o labirinto no canvas com emojis."""
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                emoji = EMOJIS.get(self.labirinto[i][j], '?')
                self.canvas.create_text(
                    j * TAMANHO_CELULA + TAMANHO_CELULA // 2,
                    i * TAMANHO_CELULA + TAMANHO_CELULA // 2,
                    text=emoji, font=("Arial", 24)
                )

    def encontrar_caminho(self):
        """Utiliza BFS para encontrar o caminho mais curto de 'S' a 'E'."""
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        inicio, fim = None, None

        for i in range(self.rows):
            for j in range(self.cols):
                if self.labirinto[i][j] == 'S':
                    inicio = (i, j)
                elif self.labirinto[i][j] == 'E':
                    fim = (i, j)

        if not inicio or not fim:
            self.label_resultado.config(text="Erro: Labirinto precisa ter 'S' e 'E'.")
            return []

        print(f"\n🛡️ [INICIANDO] Buscando o caminho mais curto de {inicio} até {fim}")
        fila = deque([(inicio, [inicio])])
        visitados = set([inicio])

        while fila:
            (x, y), caminho = fila.popleft()
            print(f"🔍 [ANALISANDO] Posição atual: ({x}, {y}) | Caminho: {caminho}")

            if (x, y) == fim:
                print("────────────────────────────")
                print(f"🏆 [SUCESSO] Caminho encontrado: {caminho}")
                print("────────────────────────────\n")
                return caminho

            for dx, dy in direcoes:
                novo_x, novo_y = x + dx, y + dy
                if (0 <= novo_x < self.rows and 0 <= novo_y < self.cols and
                        self.labirinto[novo_x][novo_y] in ('.', 'E') and (novo_x, novo_y) not in visitados):
                    fila.append(((novo_x, novo_y), caminho + [(novo_x, novo_y)]))
                    visitados.add((novo_x, novo_y))
        print("🚨 [FALHA] Nenhum caminho encontrado!")
        return []

    def desenhar_caminho(self, caminho):
        """Destaca o caminho encontrado no canvas com o emoji 'C' (caminho percorrido)."""
        for (x, y) in caminho[1:-1]:
            self.canvas.create_text(
                y * TAMANHO_CELULA + TAMANHO_CELULA // 2,
                x * TAMANHO_CELULA + TAMANHO_CELULA // 2,
                text=EMOJIS['C'], font=("Arial", 24)
            )
            self.root.update()
            time.sleep(0.3)

    def resolver_labirinto(self):
        """Encontra e desenha o caminho, e exibe uma mensagem com o caminho encontrado."""
        caminho = self.encontrar_caminho()
        if caminho:
            self.desenhar_caminho(caminho)
            self.label_resultado.config(text=f"Caminho: {caminho}")
        else:
            self.label_resultado.config(text="Nenhum caminho encontrado!")

# Criar a interface gráfica
root = tk.Tk()
root.title("Labirinto Místico do Feiticeiro")
labirinto_gui = LabirintoGUI(root, labirinto_default)
root.mainloop()
