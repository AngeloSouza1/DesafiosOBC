import tkinter as tk

def calcular_coordenada(direcoes_list):
    """
    Recebe uma lista de strings, cada uma representando uma sequência de direções,
    e retorna a coordenada final (x, y) a partir do ponto inicial (0, 0) usando a seguinte chave:
      N: (0, -1)
      S: (0, +1)
      L: (-1, 0)
      O: (0, 0)
    """
    # Coordenada inicial
    x, y = 0, 0
    # Para cada string na lista
    for seq in direcoes_list:
        seq = seq.strip().upper()
        for ch in seq:
            if ch == 'N':
                y -= 1
            elif ch == 'S':
                y += 1
            elif ch == 'L':
                x -= 1
            elif ch == 'O':
                x += 0  # O não gera movimento
            else:
                # Ignora caracteres não esperados
                continue
    return x, y

def calcular():
    try:
        # Lê o input do usuário (ex.: "NNSSLO, NL, OSS")
        entrada = entry.get().strip()
        if not entrada:
            result_label.config(text="❌ Insira as sequências de direções!")
            return
        # Separa a entrada por vírgula e remove espaços extras
        sequencias = [s.strip() for s in entrada.split(",") if s.strip()]
        # Calcula a coordenada final
        x, y = calcular_coordenada(sequencias)
        # Exibe a mensagem
        result_label.config(text=f"Você chegou ao tesouro!\nCoordenada final: ({x}, {y})")
    except Exception as e:
        result_label.config(text=f"❌ Erro: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("A Aventura do Tesouro Perdido 🔍💰")
root.geometry("500x300")
root.configure(bg="#1e1e2f")

# Instrução
instruction = tk.Label(root, 
                       text="Digite as sequências de direções (ex.: NNSSLO, NL, OSS):",
                       font=("Arial", 12),
                       bg="#1e1e2f",
                       fg="#ffffff")
instruction.pack(pady=10)

# Campo de entrada
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)
entry.insert(0, "NNSSLO, NL, OSS")

# Botão para calcular
button = tk.Button(root, 
                   text="Calcular Tesouro", 
                   command=calcular,
                   font=("Arial", 12, "bold"),
                   bg="#4CAF50",
                   fg="#ffffff")
button.pack(pady=10)

# Label para exibir o resultado
result_label = tk.Label(root, 
                        text="", 
                        font=("Arial", 14, "bold"),
                        bg="#1e1e2f",
                        fg="#ffeb3b")
result_label.pack(pady=10)

root.mainloop()
