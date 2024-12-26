import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from batalha_dragoes import batalha_dos_dragoes

# Função para calcular o vencedor
def calcular_vencedor():
    try:
        energia_inicial_a = int(entry_energia_a.get())
        energia_inicial_b = int(entry_energia_b.get())
        itens_a = list(map(int, entry_itens_a.get().split(',')))
        itens_b = list(map(int, entry_itens_b.get().split(',')))

        vencedor = batalha_dos_dragoes(energia_inicial_a, energia_inicial_b, itens_a, itens_b)
        messagebox.showinfo("Resultado", f"O vencedor é: {vencedor}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("🐉🐉🐉")
root.geometry("700x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # Fundo escuro

# Estilo personalizado para a interface
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#1e1e1e")  # Fundo escuro para o frame
style.configure("TLabel", font=("Roboto", 12), background="#1e1e1e", foreground="white")
style.configure("TEntry", font=("Roboto", 12), fieldbackground="#2a2a2a", foreground="white")
style.map(
    "TEntry",
    fieldbackground=[("focus", "#3a3a3a")],  # Fundo do entry ao focar
    foreground=[("focus", "white")]
)
style.configure("TButton", font=("Roboto", 12, "bold"), background="#f39c12", foreground="#1e1e1e")
style.map(
    "TButton",
    background=[("active", "#e67e22")],
    foreground=[("active", "white")]
)

# Cabeçalho
header = ttk.Frame(root)
header.pack(fill="x", pady=10)
header_label = tk.Label(
    header,
    text="⚔️ Batalha dos Dragões 🐉",
    font=("Helvetica", 26, "bold"),
    bg="#1e1e1e",
    fg="#f39c12"
)
header_label.pack(pady=20)

# Corpo principal (frame para entradas e botões)
body_frame = ttk.Frame(root, padding="20")
body_frame.pack(pady=20)

# Energia Inicial
ttk.Label(body_frame, text="Energia Inicial do Dragão A:").grid(row=0, column=0, sticky="w", pady=10, padx=10)
entry_energia_a = ttk.Entry(body_frame, width=30)
entry_energia_a.grid(row=0, column=1, pady=10, padx=10)

ttk.Label(body_frame, text="Energia Inicial do Dragão B:").grid(row=1, column=0, sticky="w", pady=10, padx=10)
entry_energia_b = ttk.Entry(body_frame, width=30)
entry_energia_b.grid(row=1, column=1, pady=10, padx=10)

# Itens Mágicos
ttk.Label(body_frame, text="Itens Mágicos do Dragão A (separados por vírgula):").grid(row=2, column=0, sticky="w", pady=10, padx=10)
entry_itens_a = ttk.Entry(body_frame, width=30)
entry_itens_a.grid(row=2, column=1, pady=10, padx=10)

ttk.Label(body_frame, text="Itens Mágicos do Dragão B (separados por vírgula):").grid(row=3, column=0, sticky="w", pady=10, padx=10)
entry_itens_b = ttk.Entry(body_frame, width=30)
entry_itens_b.grid(row=3, column=1, pady=10, padx=10)

# Botão de Calcular
btn_calcular = ttk.Button(body_frame, text="Calcular Vencedor", command=calcular_vencedor)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=20)

# Rodapé
footer = ttk.Frame(root, padding="10")
footer.pack(side="bottom", fill="x")
footer_label = tk.Label(
    footer,
    text="Desenvolvido por Angelo Souza",
    font=("Roboto", 10, "italic"),
    bg="#1e1e1e",
    fg="#7f8c8d"
)
footer_label.pack()

# Rodar a aplicação
root.mainloop()
