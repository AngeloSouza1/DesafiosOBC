import tkinter as tk
from tkinter import messagebox
from magic_word import encontrar_palavra_magica

def resetar_aplicacao():
    """
    Reseta o campo de entrada e redefine o estado da aplicação.
    """
    entry_pergaminho.delete(0, tk.END)  # Limpa o campo de entrada

def processar_pergaminho():
    """
    Processa o pergaminho inserido no campo de entrada para encontrar a palavra mágica.
    """
    pergaminho = entry_pergaminho.get().strip()

    if not pergaminho:
        messagebox.showwarning("Atenção", "Por favor, insira o pergaminho!")
        return

    try:
        palavra_magica = encontrar_palavra_magica(pergaminho)
        exibir_popup(f"A palavra mágica é: {palavra_magica}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def exibir_popup(mensagem):
    """
    Exibe um popup personalizado e reseta a aplicação ao fechar.
    """
    popup = tk.Toplevel(root)
    popup.title("Resultado")
    popup.geometry("350x200")
    popup.configure(bg="#1e1e2f")
    popup.transient(root)
    popup.grab_set()

    # Mensagem no popup
    label_mensagem = tk.Label(
        popup,
        text=mensagem,
        font=("Arial", 12),
        bg="#1e1e2f",
        fg="#ffffff",
        wraplength=300,
        justify="center"
    )
    label_mensagem.pack(pady=20)

    # Botão para fechar e resetar
    botao_fechar = tk.Button(
        popup,
        text="Fechar",
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="#ffffff",
        command=lambda: [popup.destroy(), resetar_aplicacao()]
    )
    botao_fechar.pack(pady=10)

# Configuração inicial do tkinter
root = tk.Tk()
root.title("Pergaminho Secreto do Feiticeiro 🔮")
root.geometry("800x400")  # Aumentando o tamanho da janela
root.configure(bg="#1e1e2f")

# Estilização
estilo_label = {"font": ("Arial", 14), "bg": "#1e1e2f", "fg": "#ffffff"}
estilo_entry = {"font": ("Arial", 14), "width": 60}
estilo_button = {"font": ("Arial", 14, "bold"), "bg": "#4CAF50", "fg": "#ffffff"}

# Título
titulo_label = tk.Label(
    root,
    text="Pergaminho Secreto do Feiticeiro 🔮",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="#FFD700"
)
titulo_label.pack(pady=20)

# Instrução
instrucao_label = tk.Label(
    root,
    text="Digite o pergaminho contendo as palavras mágicas:",
    **estilo_label
)
instrucao_label.pack(pady=10)

# Campo de entrada
entry_pergaminho = tk.Entry(root, **estilo_entry)
entry_pergaminho.pack(pady=20)

# Botão para processar
btn_processar = tk.Button(
    root,
    text="Descobrir Palavra Mágica",
    command=processar_pergaminho,
    **estilo_button
)
btn_processar.pack(pady=20)

# Rodapé
footer_label = tk.Label(
    root,
    text="Criado por AAFS 🧙‍♂️✨",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="#555555"
)
footer_label.pack(side="bottom", pady=10)

# Loop principal
root.mainloop()
