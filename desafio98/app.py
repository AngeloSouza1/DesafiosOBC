import tkinter as tk

def encontrar_numeros_magicos(numeros):
    """
    Retorna uma lista com os números mágicos:
    números ímpares que são menores que a média inteira de todos os números.
    
    Args:
        numeros (list): Lista de inteiros.
    
    Returns:
        list: Números mágicos.
    """
    if not numeros:
        return []
    # Calcula a média usando divisão inteira
    media = sum(numeros) // len(numeros)
    # Apenas números ímpares e estritamente menores que a média
    return [n for n in numeros if n % 2 != 0 and n < media]

def calcular():
    try:
        # Recupera o texto do campo de entrada, removendo espaços
        texto = entry.get().strip().replace(" ", "")
        # Converte o texto em uma lista de inteiros
        numeros = [int(x) for x in texto.split(",") if x]
        # Calcula os números mágicos
        magicos = encontrar_numeros_magicos(numeros)
        # Atualiza o label com o resultado
        result_label.config(text=f"🧙‍♂️ Números Mágicos: {magicos}\n(Média inteira: {sum(numeros) // len(numeros)})")
    except Exception as e:
        result_label.config(text=f"❌ Erro: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Aventuras na Caverna dos Dragões 🐉")
root.geometry("500x300")
root.configure(bg="#1e1e2f")

# Label de instrução
instruction = tk.Label(root, 
                       text="Digite os poderes dos dragões (ex.: 3,7,10,15,6,2,9):",
                       font=("Arial", 12),
                       bg="#1e1e2f",
                       fg="#ffffff")
instruction.pack(pady=10)

# Campo de entrada
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)
entry.insert(0, "3,7,10,15,6,2,9")

# Botão para calcular
button = tk.Button(root, 
                   text="Calcular Números Mágicos", 
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
