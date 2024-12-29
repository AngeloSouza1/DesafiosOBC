import tkinter as tk
from tkinter import PhotoImage
from solver import escape_room_solution  # Importa a função da solução


def custom_messagebox(title, message, msg_type="info"):
    """
    Exibe uma mensagem popup personalizada centralizada na janela principal.
    """
    def clear_input_and_close():
        """Limpa o campo de entrada e fecha o popup."""
        input_text.delete("1.0", tk.END)
        popup.destroy()

    bg_color = "#2b2b2b"
    fg_color = "#ffffff"
    highlight_color = "#FF0000"  # Cor de destaque para o resultado

    popup = tk.Toplevel(root)
    popup.title(title)
    popup.config(bg=bg_color)
    popup.geometry("400x250")
    popup.resizable(False, False)

    # Centraliza o popup em relação à janela principal
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    popup_x = root_x + (root_width // 2) - (400 // 2)
    popup_y = root_y + (root_height // 2) - (250 // 2)
    popup.geometry(f"400x250+{popup_x}+{popup_y}")

    # Ícone no topo
    label_icon = tk.Label(popup, text="🎉", font=("Roboto", 30), bg=bg_color, fg=fg_color)
    label_icon.pack(pady=10)

    # Mensagem principal
    label_message = tk.Label(popup, text=title, font=("Roboto", 18, "bold"), bg=bg_color, fg=fg_color)
    label_message.pack(pady=5)

    # Resultado com destaque
    label_highlight = tk.Label(
        popup, 
        text=message, 
        font=("Roboto", 15, "bold"), 
        bg=bg_color, 
        fg=highlight_color, 
        wraplength=350
    )
    label_highlight.pack(pady=10)

    # Botão de fechar
    close_button = tk.Button(
        popup,
        text="OK",
        font=("Roboto", 14, "bold"),
        bg="#007BFF",
        fg="#FFFFFF",
        activebackground="#0056b3",
        activeforeground="#FFFFFF",
        command=clear_input_and_close  # Chama a função de limpar e fechar
    )
    close_button.pack(pady=10)


def process_input():
    """
    Processa o texto inserido pelo usuário e exibe a frase mágica no popup.
    """
    user_input = input_text.get("1.0", tk.END).strip()  # Obtém o texto do campo de entrada
    if not user_input:
        custom_messagebox("Entrada Vazia", "Por favor, insira suas frases para decifrar!", "warning")
        return

    # Converte o texto em uma lista de frases
    input_list = user_input.split("\n")
    try:
        # Processa a solução usando a função importada
        magic_phrase = escape_room_solution(input_list)
        custom_messagebox("Sucesso!", f"{magic_phrase}", "info")  # Mostra a frase mágica no popup
    except Exception as e:
        custom_messagebox("Erro", f"Ocorreu um erro ao processar as frases:\n{str(e)}", "error")


# Criação da janela principal
root = tk.Tk()
root.title("Escape Room - Decifrador de Memes")
root.geometry("515x950")
root.config(bg="#1e1e1e")  # Fundo escuro

# Carregar a imagem central
uploaded_image_path = "image.png"  # Nova imagem escura, insira o caminho correto
main_image = PhotoImage(file=uploaded_image_path)

# Adiciona a imagem na parte superior
image_label = tk.Label(root, image=main_image, bg="#1e1e1e")
image_label.pack(pady=10)

# Instruções
instructions = tk.Label(
    root,
    text="Insira suas frases de memes (uma por linha):",
    font=("Roboto", 14),
    bg="#1e1e1e",
    fg="#c0c0c0"
)
instructions.pack(pady=10)

# Campo de entrada
input_text = tk.Text(
    root, 
    height=10, 
    width=60, 
    font=("Roboto", 12), 
    wrap="word", 
    borderwidth=0, 
    relief="solid", 
    bg="#333333", 
    fg="#ffffff", 
    insertbackground="#00FF7F",  # Cursor verde
)
input_text.pack(pady=10, padx=20)

# Função para alterar o estilo do botão ao passar o mouse
def on_enter(e):
    decode_button.config(bg="#0056b3", fg="#ffffff")

def on_leave(e):
    decode_button.config(bg="#007BFF", fg="#FFFFFF")

# Botão para decifrar com estilo aprimorado
decode_button = tk.Button(
    root,
    text="Decifrar",
    font=("Roboto", 16, "bold"),
    bg="#007BFF",
    fg="#FFFFFF",
    activebackground="#0056b3",
    activeforeground="#FFFFFF",
    relief="flat",  # Botão plano
    borderwidth=0,  # Sem bordas
    highlightthickness=0,
    padx=20,  # Margem horizontal interna
    pady=10,  # Margem vertical interna
    command=process_input
)
decode_button.pack(pady=20)

# Bind para aplicar animação ao passar o mouse
decode_button.bind("<Enter>", on_enter)
decode_button.bind("<Leave>", on_leave)


# Loop principal
root.mainloop()
