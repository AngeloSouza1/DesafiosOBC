import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from busca_tesouro import encontrar_menor_caminho
import tkinter as tk
from tkinter import messagebox

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

    # Aplicar os passos no caminho, verificando limites
    for (x, y) in caminho:
        if 0 <= x < len(ilha) and 0 <= y < len(ilha[0]) and ilha[x][y] == '~':
            matriz[x][y] = 5  # Representação numérica dos passos percorridos

    # Garantir que o ponto de partida 'P' e o tesouro 'T' sejam mantidos
    if caminho:
        inicio_x, inicio_y = caminho[0]
        fim_x, fim_y = caminho[-1]
        matriz[inicio_x][inicio_y] = 1
        matriz[fim_x][fim_y] = 2

    # Definir o mapa de cores para os elementos
    colors = ['#6a0dad', '#006400', '#ffffff', '#00008b', '#ffd700']  # Roxo, Verde Escuro, Branco, Azul Escuro, Amarelo

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
                plt.text(j, i, 'X', ha='center', va='center', fontsize=12, color='white')
            elif ilha[i][j] == '~':
                plt.text(j, i, '~', ha='center', va='center', fontsize=12, color='black')

    # Adicionar título com o número total de passos
    plt.title(f'Total de Passos: {total_passos}', fontsize=16, weight='bold')
    plt.axis('off')
    plt.show()

def processar_entrada():
    try:
        # Obter a entrada do campo de texto
        entrada = text_area.get("1.0", tk.END).strip()
        
        # Converter a entrada em uma lista de listas
        linhas = entrada.split("\n")
        max_len = max(len(linha.strip()) for linha in linhas)
        ilha = [list(linha.strip().ljust(max_len, 'X')) for linha in linhas]

        # Validação: verificar se 'P' e 'T' estão presentes
        if not any('P' in linha for linha in ilha):
            messagebox.showerror("Erro", "A matriz deve conter um ponto de partida 'P'.")
            return
        if not any('T' in linha for linha in ilha):
            messagebox.showerror("Erro", "A matriz deve conter um tesouro 'T'.")
            return

        # Encontrar o número mínimo de passos e o caminho
        resultado, caminho = encontrar_menor_caminho(ilha)

        # Verificar se o caminho está vazio
        if not caminho:
            messagebox.showerror("Erro", "Nenhum caminho encontrado para o tesouro.")
            return

        # Mostrar o resultado em uma messagebox antes de gerar o gráfico
        if resultado != -1:
            messagebox.showinfo("Resultado", f"Número mínimo de passos: {resultado}")
        else:
            messagebox.showerror("Resultado", "O tesouro não pode ser alcançado.")

        # Mostrar a ilha graficamente com os passos (sem threading)
        mostrar_ilha_graficamente(ilha, caminho, resultado)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar a entrada: {e}")

def limpar_entrada():
    """Limpa a área de texto e remove mensagens exibidas."""
    text_area.delete("1.0", tk.END)

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Entrada de Ilha para Busca de Tesouro")

# Rótulo
label = tk.Label(root, text="Insira a matriz da ilha (exemplo: P~~XX):")
label.pack(pady=10)

# Área de texto para inserir a matriz
text_area = tk.Text(root, height=15, width=50)
text_area.pack(pady=10)

# Botão para processar a entrada
button_gerar = tk.Button(root, text="Gerar Gráfico", command=processar_entrada)
button_gerar.pack(pady=5)

# Botão para limpar a entrada
button_limpar = tk.Button(root, text="Limpar", command=limpar_entrada)
button_limpar.pack(pady=5)

# Iniciar a interface Tkinter
root.mainloop()
