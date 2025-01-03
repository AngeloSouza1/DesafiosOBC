import tkinter as tk
from pontuacao import calcular_pontos  # Importa a função do módulo


# Função para criar uma janela de popup personalizada
def criar_popup(titulo, mensagem, cor_fundo="#3c3f41", cor_texto="#ffffff"):
    popup = tk.Toplevel()
    popup.title(titulo)
    popup.geometry("400x250")  # Aumentado o tamanho do popup
    popup.configure(bg=cor_fundo)
    popup.resizable(False, False)
    
    # Texto da mensagem
    label_mensagem = tk.Label(
        popup,
        text=mensagem,
        font=("Arial", 14),  # Fonte aumentada
        fg=cor_texto,
        bg=cor_fundo,
        wraplength=380,
        justify="center"
    )
    label_mensagem.pack(pady=30)  # Mais espaçamento

    # Função para fechar o popup e limpar o campo de entrada
    def fechar_popup():
        popup.destroy()
        entry_tarefas.delete(0, tk.END)  # Limpa o campo de entrada

    # Botão de fechar
    btn_fechar = tk.Button(
        popup,
        text="Fechar",
        command=fechar_popup,
        font=("Arial", 12, "bold"),  # Fonte aumentada
        bg="#008cba",
        fg="#ffffff",
        activebackground="#005f73",
        activeforeground="#ffffff",
        relief="raised",
        bd=3
    )
    btn_fechar.pack(pady=10)

    popup.transient(root)  # Para tornar o popup modal
    popup.grab_set()  # Impede interação com a janela principal enquanto o popup está aberto
    root.wait_window(popup)  # Aguarda o fechamento do popup


# Função principal de cálculo
def calcular():
    try:
        # Obter entrada do usuário
        entrada = entry_tarefas.get()

        # Converter para lista de inteiros
        tarefas = list(map(int, entrada.split(",")))

        # Calcular pontuações
        primeiro, segundo, terceiro = calcular_pontos(tarefas)

        # Mostrar resultado
        resultado = (
            f"Primeiro lugar: {primeiro} pontos\n"
            f"Segundo lugar: {segundo} pontos\n"
            f"Terceiro lugar: {terceiro} pontos"
        )
        criar_popup("Resultado", resultado)
    except ValueError:
        # Caso a entrada não seja válida
        criar_popup("Erro", "Por favor, insira números separados por vírgula.", cor_fundo="#ff4d4d", cor_texto="#ffffff")


# Configuração da janela principal
root = tk.Tk()
root.title(" ")

# Dimensão e cor de fundo
root.geometry("600x400")  # Aumentado o tamanho da janela principal
root.configure(bg="#3c3f41")

# Título principal
label_titulo = tk.Label(
    root,
    text="🧙‍♂️ Calculadora de Pontuação do Mundo dos Bruxos 🪄",
    font=("Arial", 18, "bold"),  # Fonte maior
    fg="#ffffff",
    bg="#3c3f41",
    wraplength=550,
    justify="center"
)
label_titulo.pack(pady=20)

# Instruções
label_instrucoes = tk.Label(
    root,
    text="Digite os pontos disponíveis separados por vírgula:",
    font=("Arial", 14),  # Fonte maior
    fg="#ffffff",
    bg="#3c3f41"
)
label_instrucoes.pack(pady=15)

# Campo de entrada
entry_tarefas = tk.Entry(root, width=40, font=("Arial", 14))  # Entrada maior
entry_tarefas.pack(pady=15)

# Botão calcular
btn_calcular = tk.Button(
    root,
    text="Calcular Pontuação",
    command=calcular,
    font=("Arial", 14, "bold"),  # Botão maior
    bg="#008cba",
    fg="#ffffff",
    activebackground="#005f73",
    activeforeground="#ffffff",
    relief="raised",
    bd=4  # Bordas mais grossas
)
btn_calcular.pack(pady=20)

# Rodapé
label_footer = tk.Label(
    root,
    text="Desenvolvido por AAFS 🧙‍♂️✨",
    font=("Arial", 10, "italic"),  # Fonte um pouco maior
    fg="#a9a9a9",
    bg="#3c3f41"
)
label_footer.pack(side="bottom", pady=10)

# Iniciar o loop da interface
root.mainloop()
