import tkinter as tk
from tkinter import messagebox
from modulo_missoes import gerar_missao

# Função para exibir a missão
def exibir_missao():
    missao = gerar_missao()
    resultado_label.config(
        text=f"🎯 Objetivo: {missao['objetivo']}\n\n🗺️ Local: {missao['local']}\n\n⚔️ Vilão: {missao['vilao']}",
        fg="#ffffff"
    )

# Função para sair da aplicação
def sair():
    if messagebox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Missões de RPG 🌟")
root.geometry("600x500")
root.config(bg="#1e1e2e")
root.resizable(False, False)

# Título
titulo_label = tk.Label(
    root,
    text="Gerador de Missões de RPG 🌌",
    font=("Helvetica", 24, "bold"),
    bg="#1e1e2e",
    fg="#ffcc00"
)
titulo_label.pack(pady=20)

# Botão para gerar missão
btn_gerar = tk.Button(
    root,
    text="Gerar Missão 🎲",
    font=("Helvetica", 16, "bold"),
    bg="#00bfff",
    fg="#ffffff",
    activebackground="#009acd",
    activeforeground="#ffffff",
    relief=tk.RAISED,
    bd=5,
    command=exibir_missao
)
btn_gerar.pack(pady=20)

# Área para exibir a missão
resultado_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16),
    bg="#1e1e2e",
    fg="#ffffff",
    wraplength=500,
    justify="center"
)
resultado_label.pack(pady=40)

# Botão para sair
btn_sair = tk.Button(
    root,
    text="Sair ❌",
    font=("Helvetica", 16, "bold"),
    bg="#ff4444",
    fg="#ffffff",
    activebackground="#cc0000",
    activeforeground="#ffffff",
    relief=tk.RAISED,
    bd=5,
    command=sair
)
btn_sair.pack(pady=20)

# Inicia o loop principal da interface
root.mainloop()
