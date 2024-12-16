# main.py

import tkinter as tk
from tkinter import messagebox
from simulador import simular_viagem_espacial

# Lista dos planetas e seus sons com emojis
planetas_e_sons = [
    ('Terra 🌍', 'Beep!'),
    ('Marte 🔴', 'Boop!'),
    ('Júpiter 🪐', 'Buzz!'),
    ('Saturno 💫', 'Bing!'),
    ('Nébula 🌌', 'Wooosh!')
]

# Dicionário para armazenar o estado dos checkboxes
selecoes = {}

def iniciar_simulacao():
    # Limpa a área de texto antes de começar
    text_area.delete('1.0', tk.END)
    
    # Filtra os planetas selecionados
    planetas_selecionados = [
        som for planeta, som in planetas_e_sons if selecoes[planeta].get()
    ]
    
    if not planetas_selecionados:
        text_area.insert(tk.END, "Nenhum planeta selecionado!\n")
        return
    
    # Executa a simulação com base nos sons dos planetas selecionados
    for _ in range(3):
        for som in planetas_selecionados:
            text_area.insert(tk.END, f"{som} ")
        text_area.insert(tk.END, "\n")

def sair():
    if messagebox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        root.destroy()

# Cria a janela principal
root = tk.Tk()
root.title("Jornada Espacial 🚀")
root.geometry("500x600")
root.config(bg="#1a1a1a")

# Título estilizado
titulo = tk.Label(root, text="Simulador de Viagem Espacial 🌌", font=("Helvetica", 18, "bold"), bg="#1a1a1a", fg="#00ffcc")
titulo.pack(pady=20)

# Frame para os checkboxes
frame_checkboxes = tk.Frame(root, bg="#1a1a1a")
frame_checkboxes.pack(pady=10)

# Adiciona checkboxes para cada planeta
for planeta, _ in planetas_e_sons:
    selecoes[planeta] = tk.BooleanVar(value=True)
    chk = tk.Checkbutton(frame_checkboxes, text=planeta, variable=selecoes[planeta], font=("Helvetica", 14), bg="#1a1a1a", fg="#ffffff", selectcolor="#262626", activebackground="#1a1a1a")
    chk.pack(anchor='w')

# Botão para iniciar a simulação
btn_iniciar = tk.Button(root, text="Iniciar Jornada", font=("Helvetica", 14), bg="#00ffcc", fg="#1a1a1a", command=iniciar_simulacao)
btn_iniciar.pack(pady=10)

# Área de texto para exibir os sons
text_area = tk.Text(root, height=12, width=50, font=("Courier", 12), bg="#262626", fg="#ffffff", wrap=tk.WORD)
text_area.pack(pady=20)

# Botão para sair do programa
btn_sair = tk.Button(root, text="Sair", font=("Helvetica", 14), bg="#ff4444", fg="#ffffff", command=sair)
btn_sair.pack(pady=10)

# Inicia o loop principal da interface
root.mainloop()
