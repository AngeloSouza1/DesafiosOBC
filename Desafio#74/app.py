import tkinter as tk
from tkinter import messagebox
from typing import List, Dict

# Função para verificar se um número é primo
def eh_primo(numero: int) -> bool:
    """Verifica se um número é primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Função para calcular a soma ASCII do nome do planeta
def soma_ascii(nome: str) -> int:
    """Calcula a soma dos valores ASCII das letras de um nome."""
    return sum(ord(letra) for letra in nome)

# Função para encontrar o planeta do tesouro
def encontrar_planeta_tesouro(planetas: List[Dict[str, int]]) -> str:
    """Retorna o nome do planeta com maior soma ASCII e energia prima."""
    planeta_tesouro = None
    maior_soma_ascii = 0

    for planeta in planetas:
        nome = planeta["nome"]
        energia = planeta["energia"]

        if eh_primo(energia):
            soma_nome = soma_ascii(nome)
            if soma_nome > maior_soma_ascii:
                maior_soma_ascii = soma_nome
                planeta_tesouro = nome

    return planeta_tesouro if planeta_tesouro else "Nenhum planeta encontrado"

# Lista de planetas
planetas = []

# Função para adicionar planeta à lista
def adicionar_planeta():
    nome = entry_nome.get().strip()
    energia = entry_energia.get().strip()

    if not nome or not energia.isdigit():
        messagebox.showerror("Erro", "Por favor, insira um nome válido e um número inteiro para a energia.")
        return
    
    planetas.append({"nome": nome, "energia": int(energia)})
    lista_planetas.insert(tk.END, f"{nome} - Energia: {energia}")
    
    # Limpar campos
    entry_nome.delete(0, tk.END)
    entry_energia.delete(0, tk.END)

# Função para encontrar o tesouro e exibir o resultado
def encontrar_tesouro():
    if not planetas:
        messagebox.showwarning("Aviso", "Nenhum planeta foi adicionado!")
        return

    resultado = encontrar_planeta_tesouro(planetas)
    
    # Exibir o resultado na interface
    label_resultado.config(text=f"🌌 Planeta do Tesouro: {resultado}", fg="yellow")

# Função para reiniciar a aplicação
def reiniciar_aplicacao():
    global planetas
    planetas = []  # Zera a lista de planetas
    lista_planetas.delete(0, tk.END)  # Limpa a lista exibida na interface
    label_resultado.config(text="🌌 Planeta do Tesouro: ???", fg="white")  # Reseta o resultado

# Criando a interface gráfica
root = tk.Tk()
root.title("Caça ao Tesouro Espacial 🚀")
root.geometry("500x550")
root.configure(bg="#282c34")

# Título
label_titulo = tk.Label(root, text="Caça ao Tesouro Espacial 🌌", font=("Arial", 16, "bold"), fg="white", bg="#282c34")
label_titulo.pack(pady=10)

# Entrada do nome do planeta
label_nome = tk.Label(root, text="Nome do Planeta:", font=("Arial", 12), fg="white", bg="#282c34")
label_nome.pack()
entry_nome = tk.Entry(root, font=("Arial", 12), width=30)
entry_nome.pack(pady=5)

# Entrada da energia do planeta
label_energia = tk.Label(root, text="Energia do Planeta:", font=("Arial", 12), fg="white", bg="#282c34")
label_energia.pack()
entry_energia = tk.Entry(root, font=("Arial", 12), width=30)
entry_energia.pack(pady=5)

# Botão para adicionar planeta
btn_adicionar = tk.Button(root, text="Adicionar Planeta", font=("Arial", 12, "bold"), bg="#61afef", fg="white", command=adicionar_planeta)
btn_adicionar.pack(pady=10)

# Lista de planetas adicionados
label_lista = tk.Label(root, text="Planetas Adicionados:", font=("Arial", 12, "bold"), fg="white", bg="#282c34")
label_lista.pack()
lista_planetas = tk.Listbox(root, font=("Arial", 12), width=40, height=6)
lista_planetas.pack(pady=5)

# Botão para encontrar o planeta do tesouro
btn_encontrar = tk.Button(root, text="Encontrar Tesouro 🏆", font=("Arial", 12, "bold"), bg="#98c379", fg="black", command=encontrar_tesouro)
btn_encontrar.pack(pady=10)

# Resultado do planeta do tesouro
label_resultado = tk.Label(root, text="🌌 Planeta do Tesouro: ???", font=("Arial", 14, "bold"), fg="white", bg="#282c34")
label_resultado.pack(pady=20)

# Botão para reiniciar a aplicação (sempre visível)
btn_reiniciar = tk.Button(root, text="Reiniciar Aplicação", font=("Arial", 12, "bold"), bg="#e06c75", fg="white", command=reiniciar_aplicacao)
btn_reiniciar.pack(pady=15)

# Rodapé
label_footer = tk.Label(root, text="Desenvolvido por AAFS 🪐", font=("Arial", 10, "italic"), fg="gray", bg="#282c34")
label_footer.pack(side="bottom", pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
