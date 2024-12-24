import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from modulo import calcular_forca_final

# Configuração principal
root = tk.Tk()
root.title("🕹️ Jornada do Herói Pixelado 🏰")
root.geometry("500x600")
root.configure(bg="#121212")  # Cor de fundo escura

# Verificação e uso da fonte personalizada
try:
    regular_font = Font(family="Poppins", size=12)
    bold_font = Font(family="Poppins", size=12, weight="bold")
    title_font = Font(family="Poppins", size=20, weight="bold")
    small_font = Font(family="Poppins", size=10)
except Exception as e:
    print("Fonte Poppins não encontrada, usando Arial.")
    regular_font = Font(family="Arial", size=12)
    bold_font = Font(family="Arial", size=12, weight="bold")
    title_font = Font(family="Arial", size=20, weight="bold")
    small_font = Font(family="Arial", size=10)

# Função para resetar os campos da aplicação
def resetar_campos():
    entry_forca_inicial.delete(0, tk.END)
    entry_pocao_vermelha.delete(0, tk.END)
    entry_pocao_azul.delete(0, tk.END)
    entry_pocao_verde.delete(0, tk.END)
    entry_fases.delete(0, tk.END)

# Função para personalizar pop-ups
def show_popup(title, message, error=False):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("400x200")
    popup.configure(bg="#121212")
    popup.transient(root)  # Mantém o pop-up acima da janela principal
    popup.grab_set()  # Bloqueia interação com a janela principal

    # Estilos do título e mensagem
    title_label = tk.Label(
        popup,
        text=f"{'❌' if error else '✅'} {title}",
        font=bold_font,
        bg="#121212",
        fg="#FF6584" if not error else "#E94E77",
    )
    title_label.pack(pady=10)

    message_label = tk.Label(
        popup,
        text=message,
        font=regular_font,
        bg="#121212",
        fg="#E1E1E1",
        wraplength=350,
        justify="center",
    )
    message_label.pack(pady=10)

    # Função para fechar o popup e resetar os campos
    def fechar_popup():
        resetar_campos()  # Reseta os campos ao fechar o popup
        popup.destroy()

    # Botão de fechar
    btn_close = ttk.Button(popup, text="Fechar", command=fechar_popup)
    btn_close.pack(pady=10)

# Função para calcular a força
def calcular():
    try:
        # Obtém os valores inseridos pelo usuário
        forca_inicial = int(entry_forca_inicial.get())
        pocao_vermelha = int(entry_pocao_vermelha.get())
        pocao_azul = int(entry_pocao_azul.get())
        pocao_verde = int(entry_pocao_verde.get())
        fases = int(entry_fases.get())

        # Calcula a força final usando a função do módulo
        forca_final = calcular_forca_final(forca_inicial, pocao_vermelha, pocao_azul, pocao_verde, fases)

        # Exibe o resultado em um pop-up customizado
        show_popup("Resultado", f"🎉 Força total do Pixel: {forca_final}!\nPrepare-se para enfrentar o Dragão! 🐉🔥")
    except ValueError:
        show_popup("Erro", "⚠️ Por favor, insira valores válidos em todos os campos.", error=True)

# Estilo do ttk
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TLabel",
    font=regular_font,
    background="#121212",
    foreground="#E1E1E1",
)
style.configure(
    "TEntry",
    font=regular_font,
    fieldbackground="#1E1E1E",
    foreground="#E1E1E1",
    borderwidth=1,
    relief="flat",
)
style.configure(
    "TButton",
    font=bold_font,
    background="#FF6584",
    foreground="#FFFFFF",
    borderwidth=0,
    focuscolor="#FF6584",
    padding=5,
)
style.map("TButton", background=[("active", "#E94E77")])

# Título principal
title_label = tk.Label(
    root,
    text="🕹️ Jornada do Herói Pixelado 🏰",
    font=title_font,
    bg="#121212",
    fg="#FF6584",
)
title_label.pack(pady=20)

# Subtítulo
subtitle_label = tk.Label(
    root,
    text="💪 Ajude o Pixel a alcançar sua força máxima!",
    font=regular_font,
    bg="#121212",
    fg="#E1E1E1",
)
subtitle_label.pack(pady=10)

# Frame para os campos de entrada
frame = tk.Frame(root, bg="#121212")
frame.pack(pady=20)

# Campos de entrada
fields = [
    ("⚡ Força Inicial do Pixel:", "entry_forca_inicial"),
    ("🧪 Poções Vermelhas:", "entry_pocao_vermelha"),
    ("🧪 Poções Azuis:", "entry_pocao_azul"),
    ("🧪 Poções Verdes:", "entry_pocao_verde"),
    ("🎯 Número de Fases:", "entry_fases"),
]

# Criação dos campos
for i, (label_text, var_name) in enumerate(fields):
    label = ttk.Label(frame, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
    entry = ttk.Entry(frame, width=25)
    entry.grid(row=i, column=1, padx=10, pady=10)
    globals()[var_name] = entry

# Botão principal
btn_calcular = ttk.Button(root, text="🎮 Calcular Força", command=calcular)
btn_calcular.pack(pady=20)

# Rodapé
footer_label = tk.Label(
    root,
    text="🌟 Desenvolvido por AAFS 🌟",
    font=small_font,
    bg="#121212",
    fg="#3E3E3E",
)
footer_label.pack(side="bottom", pady=10)

# Loop principal
root.mainloop()
