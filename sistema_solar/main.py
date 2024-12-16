import tkinter as tk
from tkinter import messagebox
from orbita import calcular_voltas

# Função para calcular as voltas
def calcular():
    try:
        entrada = entry_angulos.get()
        angulos = [int(valor.strip()) for valor in entrada.split(",")]
        
        if not angulos:
            raise ValueError("Nenhum ângulo fornecido.")

        voltas = calcular_voltas(angulos)
        resultado_label.config(
            text=f"🔄 {voltas} volta(s) completa(s) necessária(s) para percorrer todos os pontos.",
            fg="#00ff00"
        )
    except ValueError:
        resultado_label.config(
            text="❌ Entrada inválida! Insira números inteiros separados por vírgulas.",
            fg="#ff4444"
        )

# Função para sair da aplicação
def sair():
    if messagebox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Simulador de Órbitas Intergalácticas 🌌")
root.geometry("700x400")
root.config(bg="#1a1a1a")
root.resizable(False, False)

# Título
titulo = tk.Label(
    root,
    text="Simulador de Voltas em Órbitas Intergalácticas 🚀",
    font=("Helvetica", 20, "bold"),
    bg="#1a1a1a",
    fg="#00ffcc"
)
titulo.pack(pady=20)

# Frame para entrada
entrada_frame = tk.Frame(root, bg="#1a1a1a")
entrada_frame.pack(pady=20)

entry_label = tk.Label(
    entrada_frame,
    text="Digite os ângulos separados por vírgulas:",
    font=("Helvetica", 14),
    bg="#1a1a1a",
    fg="#ffffff"
)
entry_label.pack(side=tk.LEFT, padx=10)

entry_angulos = tk.Entry(
    entrada_frame,
    font=("Helvetica", 14),
    width=30,
    bg="#262626",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief=tk.FLAT
)
entry_angulos.pack(side=tk.LEFT, padx=10)

# Botão para calcular voltas
btn_calcular = tk.Button(
    root,
    text="Calcular Voltas",
    font=("Helvetica", 14, "bold"),
    bg="#00ffcc",
    fg="#1a1a1a",
    activebackground="#00ddaa",
    activeforeground="#000000",
    relief=tk.RAISED,
    bd=3,
    command=calcular
)
btn_calcular.pack(pady=15)

# Área de resultado
resultado_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16),
    bg="#1a1a1a",
    fg="#ffffff",
    wraplength=600,
    justify="center"
)
resultado_label.pack(pady=20)

# Botão para sair
btn_sair = tk.Button(
    root,
    text="Sair",
    font=("Helvetica", 14, "bold"),
    bg="#ff4444",
    fg="#ffffff",
    activebackground="#ff6666",
    activeforeground="#ffffff",
    relief=tk.RAISED,
    bd=3,
    command=sair
)
btn_sair.pack(pady=10)

# Inicia o loop principal da interface
root.mainloop()
