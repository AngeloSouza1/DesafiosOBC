import tkinter as tk
from tkinter import Toplevel, Text
from heroi_tesouro import encontre_caminho

# Variável global para armazenar o mapa inicial
mapa_inicial = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', 'H', '.', '.', 'T', '#'],
    ['#', '#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '#', '#'],
    ['#', '#', '#', '#', '#', '#']
]

# Variável para o mapa atual, que será modificado pelo usuário
mapa_atual = [linha[:] for linha in mapa_inicial]

labels = []  # Variável global para os rótulos do mapa na interface

# Função para criar pop-ups personalizados
def criar_popup(titulo, mensagem):
    popup = Toplevel(janela)
    popup.title(titulo)
    popup.geometry("300x150")
    popup.configure(bg="#000000")  # Fundo preto
    popup.resizable(False, False)

    label_mensagem = tk.Label(
        popup,
        text=mensagem,
        bg="#000000",  # Fundo preto
        fg="#FFEB3B",  # Texto amarelo
        font=("Arial", 12, "bold"),
        wraplength=280
    )
    label_mensagem.pack(pady=20)

    botao_fechar = tk.Button(
        popup,
        text="OK",
        command=popup.destroy,
        bg="#FFEB3B",  # Amarelo
        fg="black",    # Texto preto
        font=("Arial", 12, "bold"),
        relief="raised",
        borderwidth=2
    )
    botao_fechar.pack(pady=10)

    popup.transient(janela)
    popup.grab_set()
    janela.wait_window(popup)

# Função para redefinir o mapa para o estado inicial
def reiniciar_mapa():
    global mapa_atual
    mapa_atual = [linha[:] for linha in mapa_inicial]  # Restaura o mapa inicial
    atualizar_interface()
    criar_popup("Reiniciar", "O mapa foi reiniciado para o estado inicial!")

# Função para atualizar os rótulos do mapa na interface
def atualizar_interface():
    for widget in grade_frame.winfo_children():
        widget.destroy()  # Remove todos os rótulos existentes

    global labels
    labels = []
    for i, linha in enumerate(mapa_atual):
        row = []
        for j, celula in enumerate(linha):
            cor = "#424242" if celula == '#' else "#FFFFFF"
            texto = " " if celula == '.' else celula
            label = tk.Label(
                grade_frame,
                text=texto,
                width=4,
                height=2,
                bg=cor,
                fg="black",
                font=("Arial", 12),
                borderwidth=2,
                relief="raised"
            )
            label.grid(row=i, column=j, padx=2, pady=2)
            row.append(label)
        labels.append(row)

# Função para encontrar o caminho e atualizar a interface
def mostrar_caminho():
    try:
        caminho = encontre_caminho(mapa_atual)
        
        if not caminho:
            criar_popup("Resultado", "Nenhum caminho encontrado!")
            return
        
        # Atualiza a interface para destacar o caminho
        for i, linha in enumerate(mapa_atual):
            for j, celula in enumerate(linha):
                if (i, j) in caminho:
                    labels[i][j].config(bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))  # Verde para o caminho
                elif celula == "H":
                    labels[i][j].config(bg="#FFEB3B", fg="black", font=("Arial", 14, "bold"))  # Amarelo para o herói
                elif celula == "T":
                    labels[i][j].config(bg="#F44336", fg="white", font=("Arial", 14, "bold"))  # Vermelho para o tesouro

        criar_popup("Resultado", f"Caminho encontrado: {caminho}")
    except ValueError as e:
        criar_popup("Erro", str(e))

# Função para abrir a janela de inserção de mapa
def abrir_janela_personalizacao():
    popup = Toplevel(janela)
    popup.title("Inserir Mapa Personalizado")
    popup.geometry("400x500")
    popup.configure(bg="#212121")
    popup.resizable(False, False)

    label_instrucoes = tk.Label(
        popup,
        text="Insira o mapa no formato esperado (linhas de '#', '.', 'H', 'T'):\nExemplo:\n#####\n#H..T#\n###.#\n#.###\n#####",
        bg="#212121",
        fg="#FFEB3B",
        font=("Arial", 10),
        wraplength=380
    )
    label_instrucoes.pack(pady=10)

    text_area = Text(popup, width=40, height=10, font=("Arial", 12))
    text_area.pack(pady=10)
    text_area.insert("1.0", "#####\n#H..T#\n###.#\n#.###\n#####")  # Placeholder de exemplo

    botao_confirmar = tk.Button(
        popup,
        text="Confirmar Mapa",
        command=lambda: definir_mapa_personalizado(text_area.get("1.0", tk.END), popup),
        bg="#03A9F4",
        fg="white",
        font=("Arial", 12, "bold"),
        relief="raised",
        borderwidth=2
    )
    botao_confirmar.pack(pady=10)

# Função para atualizar o mapa personalizado
def definir_mapa_personalizado(novo_mapa, janela_personalizacao):
    global mapa_atual
    try:
        # Converter string para matriz
        linhas = novo_mapa.strip().split("\n")
        mapa = [list(linha) for linha in linhas]
        
        # Validar se há um herói e um tesouro
        tem_heroi = any('H' in linha for linha in mapa)
        tem_tesouro = any('T' in linha for linha in mapa)
        if not tem_heroi or not tem_tesouro:
            raise ValueError("O mapa deve conter um herói ('H') e um tesouro ('T').")
        
        # Atualizar o mapa atual
        mapa_atual = mapa
        atualizar_interface()  # Atualiza a interface gráfica
        criar_popup("Sucesso", "Novo mapa carregado com sucesso!")
        janela_personalizacao.destroy()  # Fecha o pop-up de personalização
    except Exception as e:
        criar_popup("Erro", f"Mapa inválido: {e}")

# Criação da janela principal
janela = tk.Tk()
janela.title("🗺️ A Jornada do Herói")
janela.geometry("600x900")
janela.config(bg="#212121")  # Fundo escuro

# Título estilizado
titulo = tk.Label(
    janela,
    text="A Jornada do Herói",
    font=("Helvetica", 18, "bold"),
    bg="#212121",
    fg="#FFEB3B"
)
titulo.pack(pady=10)

# Configuração da matriz visual
grade_frame = tk.Frame(janela, bg="#212121")
grade_frame.pack(pady=20)
atualizar_interface()

# Botões principais
botao_caminho = tk.Button(
    janela,
    text="🔍 Encontrar Caminho",
    command=mostrar_caminho,
    bg="#03A9F4",
    fg="white",
    font=("Arial", 14, "bold"),
    relief="raised",
    borderwidth=3
)
botao_caminho.pack(pady=10)

botao_personalizar = tk.Button(
    janela,
    text="✏️ Inserir Mapa Personalizado",
    command=abrir_janela_personalizacao,
    bg="#FFEB3B",
    fg="black",
    font=("Arial", 14, "bold"),
    relief="raised",
    borderwidth=3
)
botao_personalizar.pack(pady=10)

botao_reiniciar = tk.Button(
    janela,
    text="🔄 Reiniciar Mapa",
    command=reiniciar_mapa,
    bg="#F44336",
    fg="white",
    font=("Arial", 14, "bold"),
    relief="raised",
    borderwidth=3
)
botao_reiniciar.pack(pady=10)

# Rodapé com crédito
rodape = tk.Label(
    janela,
    text="Desenvolvido por Angelo Souza",
    font=("Arial", 10),
    bg="#212121",
    fg="#BDBDBD"
)
rodape.pack(side="bottom", pady=10)

# Inicializa a interface gráfica
janela.mainloop()
