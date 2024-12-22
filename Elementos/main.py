import tkinter as tk
from tkinter import ttk, messagebox
from classificar_elementos import classificar_elemento

# Emojis para as categorias
CATEGORY_EMOJIS = {
    "Metais": "🔩",
    "Gases Nobres": "✨",
    "Halogênios": "🧪",
    "Outros": "🌌"
}

def adicionar_elemento():
    # Obter os valores da entrada
    elemento = novo_elemento_entry.get().strip().capitalize()
    if not elemento:
        messagebox.showerror("Erro", "Por favor, insira um elemento válido!")
        novo_elemento_entry.delete(0, tk.END)  # Limpar campo de entrada mesmo no erro
        return

    try:
        # Processar o elemento e atualizar a lista e categorias
        global elementos, categorias
        elementos, categorias, mensagem = classificar_elemento(elementos, elemento, categorias)

        # Atualizar a exibição do Treeview
        atualizar_lista()

        # Exibir mensagem da categoria
        categoria_label.config(text=mensagem, fg="green")
    except ValueError as ve:
        messagebox.showerror("Erro", str(ve))
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    finally:
        # Limpar o campo de entrada sempre, independente de erro ou sucesso
        novo_elemento_entry.delete(0, tk.END)

def atualizar_lista():
    """
    Atualiza o Treeview com os elementos e suas categorias.
    """
    # Limpar a lista existente no Treeview
    for item in lista_elementos_tree.get_children():
        lista_elementos_tree.delete(item)

    # Inserir os elementos e categorias no Treeview
    for elemento in elementos:
        # Determinar a categoria do elemento
        categoria = "Outros"
        for cat, elems in categorias.items():
            if elemento in elems:
                categoria = cat
                break

        # Adicionar o emoji correspondente à categoria
        categoria_com_emoji = f"{CATEGORY_EMOJIS.get(categoria, '')} {categoria}"
        lista_elementos_tree.insert("", "end", values=(elemento, categoria_com_emoji))

def mostrar_categorias():
    # Construir um dicionário filtrado apenas com os elementos presentes na lista de elementos
    categorias_filtradas = {cat: [] for cat in categorias}
    for elemento in elementos:
        for categoria, elems in categorias.items():
            if elemento in elems:
                categorias_filtradas[categoria].append(elemento)
                break

    # Construir a string para exibir as categorias filtradas
    categorias_texto = "Categorias e Elementos:\n\n"
    for categoria, elementos_filtrados in categorias_filtradas.items():
        if elementos_filtrados:  # Exibir apenas categorias com elementos
            categorias_texto += f"{CATEGORY_EMOJIS.get(categoria, '')} {categoria}:\n  - " + ", ".join(elementos_filtrados) + "\n\n"

    # Exibir as categorias em uma nova janela
    categorias_janela = tk.Toplevel(root)
    categorias_janela.title("Categorias e Elementos")
    categorias_janela.geometry("400x400")
    categorias_janela.configure(bg="black")

    categorias_label = tk.Label(
        categorias_janela,
        text=categorias_texto,
        font=("Helvetica", 12),
        fg="white",
        bg="black",
        justify="left",
    )
    categorias_label.pack(padx=10, pady=10)

# Lista inicial de elementos e categorias
elementos = ["H", "He", "Li", "Be", "B"]
categorias = {
    "Metais": ["Li", "Be", "Na", "Mg", "Al", "K", "Ca", "Fe", "Cu", "Zn"],
    "Gases Nobres": ["He", "Ne", "Ar", "Kr", "Xe", "Rn"],
    "Halogênios": ["F", "Cl", "Br", "I", "At"],
    "Outros": ["H", "B", "C", "O", "N", "P", "S"],
}

# Criar a janela principal
root = tk.Tk()
root.title("Classificação de Elementos Químicos")
root.geometry("500x600")
root.configure(bg="black")

# Título
titulo_label = tk.Label(
    root,
    text="Classificação de Elementos Químicos",
    font=("Helvetica", 16, "bold"),
    fg="cyan",
    bg="black",
)
titulo_label.pack(pady=10)

# Entrada de novos elementos
frame_entrada = tk.Frame(root, bg="black")
frame_entrada.pack(pady=10)

novo_elemento_label = tk.Label(
    frame_entrada,
    text="Novo Elemento:",
    font=("Helvetica", 12),
    fg="white",
    bg="black",
)
novo_elemento_label.grid(row=0, column=0, padx=10, pady=5)

novo_elemento_entry = ttk.Entry(frame_entrada, font=("Helvetica", 12))
novo_elemento_entry.grid(row=0, column=1, padx=10, pady=5)

adicionar_button = tk.Button(
    frame_entrada,
    text="Adicionar",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=adicionar_elemento,
)
adicionar_button.grid(row=0, column=2, padx=10, pady=5)

# Exibição da lista de elementos
lista_label = tk.Label(
    root,
    text="Lista de Elementos:",
    font=("Helvetica", 14, "bold"),
    fg="magenta",
    bg="black",
)
lista_label.pack(pady=10)

lista_elementos_frame = tk.Frame(root)
lista_elementos_frame.pack(pady=10)

lista_elementos_tree = ttk.Treeview(
    lista_elementos_frame,
    columns=("Elemento", "Categoria"),
    show="headings",
    height=10,
)
lista_elementos_tree.heading("Elemento", text="Elemento")
lista_elementos_tree.heading("Categoria", text="Categoria")
lista_elementos_tree.column("Elemento", width=150, anchor="center")
lista_elementos_tree.column("Categoria", width=200, anchor="center")
lista_elementos_tree.pack()

# Estilizar o Treeview
style = ttk.Style()
style.theme_use("default")
style.configure(
    "Treeview",
    background="black",
    foreground="white",
    fieldbackground="black",
    font=("Helvetica", 12),
    rowheight=25,
)
style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"), background="#007BFF", foreground="white")

# Mensagem da categoria
categoria_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 12),
    fg="yellow",
    bg="black",
)
categoria_label.pack(pady=10)

# Link para ver categorias
ver_categorias_button = tk.Button(
    root,
    text="Ver Categorias e Elementos",
    font=("Helvetica", 12, "bold"),
    bg="#007BFF",
    fg="white",
    command=mostrar_categorias,
)
ver_categorias_button.pack(pady=10)

# Inicializar a lista de elementos no Treeview
atualizar_lista()

# Rodar o loop principal
root.mainloop()
