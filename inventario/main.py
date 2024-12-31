import tkinter as tk
from tkinter import ttk
from inventario import calcular_peso_total, avaliar_capacidade

def atualizar_tabela():
    """Atualiza a tabela com os itens inseridos."""
    for row in tabela.get_children():
        tabela.delete(row)  # Limpa a tabela
    for item in items:
        tabela.insert("", "end", values=(item["nome"], item["peso"]))

def carregar_itens():
    """Carrega os itens inseridos no campo de entrada e atualiza a tabela."""
    entrada_itens = entry_items.get().strip()

    try:
        # Converte a entrada JSON para uma lista de dicionários
        carregados = eval(entrada_itens)

        # Valida a estrutura dos itens
        if not all(isinstance(item, dict) and "nome" in item and "peso" in item for item in carregados):
            raise ValueError("A lista de itens deve conter dicionários com as chaves 'nome' e 'peso'.")

        # Atualiza os itens e a tabela
        global items
        items = carregados
        atualizar_tabela()
        entry_items.delete(0, tk.END)
        verificar_inputs()  # Verifica os campos após carregar itens
    except Exception as e:
        exibir_popup(f"Erro ao carregar itens: {e}", tipo="erro")

def processar_inventario():
    """Processa o inventário e avalia o peso total."""
    entrada_capacidade = entry_capacidade.get().strip()

    try:
        capacidade_maxima = int(entrada_capacidade)

        # Calcula o peso total
        peso_total = calcular_peso_total(items)

        # Avalia a capacidade
        mensagem_capacidade = avaliar_capacidade(peso_total, capacidade_maxima)

        # Exibe o resultado
        exibir_popup(f"Peso total do inventário: {peso_total}\n{mensagem_capacidade}", tipo="info")
    except ValueError as e:
        exibir_popup(f"Erro: {e}", tipo="erro")

def reiniciar():
    """Reinicia o formulário."""
    global items
    items = []  # Limpa os itens
    atualizar_tabela()
    entry_items.delete(0, tk.END)
    entry_capacidade.delete(0, tk.END)
    btn_reiniciar.pack_forget()  # Esconde o botão de reiniciar
    verificar_inputs()  # Desabilita os botões após reiniciar

def exibir_popup(mensagem, tipo="info"):
    """Cria um popup personalizado."""
    popup = tk.Toplevel(root)
    popup.title("Mensagem")

    # Configurações do estilo do popup
    popup.geometry("350x180")
    popup.configure(bg="#1e1e2f")
    popup.transient(root)
    popup.grab_set()

    # Emoji para o tipo de mensagem
    emoji = "✅" if tipo == "info" else "❌"

    # Mensagem com emoji
    label_mensagem = tk.Label(
        popup,
        text=f"{emoji} {mensagem}",
        font=("Arial", 12),
        bg="#1e1e2f",
        fg="#ffffff",
        wraplength=300,
        justify="center"
    )
    label_mensagem.pack(pady=20)

    # Botão para fechar o popup
    def fechar_popup():
        popup.destroy()
        if tipo == "info":  # Apenas se for um resultado bem-sucedido
            reiniciar()  # Limpa os campos e a tabela

    botao_fechar = tk.Button(
        popup,
        text="Fechar",
        font=("Arial", 12, "bold"),
        bg="#4CAF50" if tipo == "info" else "#FF5555",
        fg="#ffffff",
        width=10,
        command=fechar_popup
    )
    botao_fechar.pack(pady=10)

def verificar_inputs():
    """Habilita ou desabilita os botões dependendo dos campos preenchidos."""
    itens_preenchidos = bool(entry_items.get().strip())
    capacidade_preenchida = bool(entry_capacidade.get().strip())

    # Habilita ou desabilita os botões
    btn_carregar["state"] = "normal" if itens_preenchidos else "disabled"
    btn_calcular["state"] = "normal" if capacidade_preenchida and items else "disabled"

# Configuração inicial do Tkinter
root = tk.Tk()
root.title("Inventário do Aventureiro")
root.geometry("600x520")
root.configure(bg="#1e1e2f")

# Dados do inventário
items = []

# Título
label_titulo = tk.Label(
    root,
    text="⚔️ Cálculo do Inventário do Aventureiro 🛡️",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
)
label_titulo.pack(pady=10)

# Entrada para os itens
label_items = tk.Label(
    root,
    text="Digite os itens do inventário em formato JSON:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="#cccccc",
    wraplength=480,
    justify="left"
)
label_items.pack(pady=5)

label_exemplo = tk.Label(
    root,
    text="(ex.: [{'nome': 'Espada', 'peso': 10}]):",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="#FFD700",  # Cor amarela
    wraplength=480,
    justify="left"
)
label_exemplo.pack(pady=5)

entry_items = tk.Entry(root, font=("Arial", 12), width=60)
entry_items.pack(pady=10)
entry_items.bind("<KeyRelease>", lambda event: verificar_inputs())  # Verifica ao digitar

btn_carregar = tk.Button(
    root,
    text="Carregar Itens",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="#ffffff",
    command=carregar_itens,
    state="disabled"  # Inicialmente desabilitado
)
btn_carregar.pack(pady=10)

# Tabela para exibir itens
tabela_frame = tk.Frame(root)
tabela_frame.pack(pady=10)

tabela = ttk.Treeview(tabela_frame, columns=("Nome", "Peso"), show="headings", height=5)
tabela.heading("Nome", text="Nome")
tabela.heading("Peso", text="Peso")
tabela.pack()

# Entrada para capacidade máxima
label_capacidade = tk.Label(
    root,
    text="Capacidade Máxima (ex.: 20):",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="#cccccc"
)
label_capacidade.pack(pady=10)

entry_capacidade = tk.Entry(root, font=("Arial", 12), width=40)
entry_capacidade.pack(pady=5)
entry_capacidade.bind("<KeyRelease>", lambda event: verificar_inputs())  # Verifica ao digitar

# Botões de calcular e reiniciar
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

btn_calcular = tk.Button(
    btn_frame,
    text="📊 Calcular Peso Total",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="#ffffff",
    command=processar_inventario,
    state="disabled"  # Inicialmente desabilitado
)
btn_calcular.grid(row=0, column=0, padx=5)

btn_reiniciar = tk.Button(
    btn_frame,
    text="🔄 Reiniciar",
    font=("Arial", 12, "bold"),
    bg="#FF5555",
    fg="#ffffff",
    command=reiniciar
)
btn_reiniciar.grid(row=0, column=1, padx=5)
btn_reiniciar.pack_forget()  # Inicialmente escondido

# Rodapé
footer_label = tk.Label(
    root,
    text="Criado por AAFS 🧑‍💻",
    font=("Arial", 10),
    bg="#1e1e2f",
    fg="#555555"
)
footer_label.pack(side="bottom", pady=10)

# Loop principal
root.mainloop()
