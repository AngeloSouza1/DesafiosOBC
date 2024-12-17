import tkinter as tk
from tkinter import messagebox
from modulo_decode import codificar_mensagem, decodificar_mensagem

# Função para codificar a mensagem
def codificar():
    mensagem = entry_input.get().strip()
    if mensagem:
        mensagem_codificada = codificar_mensagem(mensagem)
        resultado_text.config(state='normal')
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"🔐 Mensagem Codificada:\n{mensagem_codificada}")
        resultado_text.config(state='disabled')
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira uma mensagem para codificar.")
        entry_input.focus()

# Função para decodificar a mensagem
def decodificar():
    mensagem_codificada = entry_input.get().strip()
    if mensagem_codificada:
        mensagem_decodificada = decodificar_mensagem(mensagem_codificada)
        resultado_text.config(state='normal')
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"🔓 Mensagem Decodificada:\n{mensagem_decodificada}")
        resultado_text.config(state='disabled')
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira uma mensagem para decodificar.")
        entry_input.focus()

# Função para limpar os campos
def limpar():
    entry_input.delete(0, tk.END)
    resultado_text.config(state='normal')
    resultado_text.delete("1.0", tk.END)
    resultado_text.config(state='disabled')
    entry_input.focus()

# Função para sair da aplicação
def sair():
    if messagebox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Decodificador de Mensagens Espaciais 🚀")
root.geometry("600x500")
root.config(bg="#1a1a1a")
root.resizable(False, False)

# Título
titulo = tk.Label(root, text="Decodificador de Mensagens Espaciais 🌌", font=("Helvetica", 20, "bold"), bg="#1a1a1a", fg="#00ffcc")
titulo.pack(pady=20)

# Entrada de texto
entry_label = tk.Label(root, text="Digite a mensagem:", font=("Helvetica", 14), bg="#1a1a1a", fg="#ffffff")
entry_label.pack(pady=5)

entry_input = tk.Entry(root, font=("Helvetica", 14), width=40, bg="#262626", fg="#ffffff", insertbackground="#ffffff", relief="flat")
entry_input.pack(pady=10)

# Botões de ação
btn_frame = tk.Frame(root, bg="#1a1a1a")
btn_frame.pack(pady=20)

btn_codificar = tk.Button(btn_frame, text="Codificar", font=("Helvetica", 14, "bold"), bg="#00cc66", fg="#ffffff", width=12, relief="ridge", command=codificar)
btn_codificar.grid(row=0, column=0, padx=10, pady=10)

btn_decodificar = tk.Button(btn_frame, text="Decodificar", font=("Helvetica", 14, "bold"), bg="#ffcc00", fg="#1a1a1a", width=12, relief="ridge", command=decodificar)
btn_decodificar.grid(row=0, column=1, padx=10, pady=10)

btn_limpar = tk.Button(btn_frame, text="Limpar", font=("Helvetica", 14, "bold"), bg="#3366ff", fg="#ffffff", width=12, relief="ridge", command=limpar)
btn_limpar.grid(row=1, column=0, padx=10, pady=10)

btn_sair = tk.Button(btn_frame, text="Sair", font=("Helvetica", 14, "bold"), bg="#ff4444", fg="#ffffff", width=12, relief="ridge", command=sair)
btn_sair.grid(row=1, column=1, padx=10, pady=10)

# Área de resultado com suporte para copiar texto
resultado_label = tk.Label(root, text="Resultado:", font=("Helvetica", 14), bg="#1a1a1a", fg="#ffffff")
resultado_label.pack(pady=5)

resultado_text = tk.Text(root, font=("Helvetica", 14), bg="#262626", fg="#ffffff", height=5, wrap="word", state='disabled', relief="flat")
resultado_text.pack(pady=10, padx=20, fill="x")

# Foco inicial na entrada
entry_input.focus()

# Inicia o loop principal da interface
root.mainloop()
