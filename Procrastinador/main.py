import tkinter as tk
from tkinter import ttk, messagebox
from amuletos import filtrar_amuletos_com_processamento

def verificar_amuletos():
    try:
        # Obter os valores do campo de entrada
        entrada = entrada_amuletos.get().strip()
        if not entrada:
            raise ValueError("Por favor, insira ao menos um número.")

        # Converter entrada em uma lista de inteiros
        inventario = list(map(int, entrada.split(",")))

        # Filtrar os amuletos dignos e obter os passos do processamento
        dignos, passos = filtrar_amuletos_com_processamento(inventario)

        # Atualizar a exibição do resultado
        resultado.set(f"Amuletos dignos: {', '.join(map(str, dignos))}" if dignos else "Nenhum amuleto digno encontrado.")
        processamento.set(f"Processamento Detalhado:\n\n{passos}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def reiniciar():
    """
    Limpa todos os campos de entrada e saída.
    """
    entrada_amuletos.delete(0, tk.END)
    resultado.set("")
    processamento.set("")

# Criar a janela principal
root = tk.Tk()
root.title("Jornada do Herói Procrastinador 🚀")
root.geometry("700x500")
root.configure(bg="black")

# Variáveis para exibição do resultado e processamento
resultado = tk.StringVar()
processamento = tk.StringVar()

# Título
titulo_label = tk.Label(
    root,
    text="Jornada do Herói Procrastinador 🚀",
    font=("Helvetica", 16, "bold"),
    fg="cyan",
    bg="black",
)
titulo_label.pack(pady=10)

# Instruções
instrucoes_label = tk.Label(
    root,
    text="Digite os amuletos separados por vírgulas:\nExemplo: 23,58,145,97,1024",
    font=("Helvetica", 12),
    fg="white",
    bg="black",
)
instrucoes_label.pack(pady=5)

# Entrada de texto
entrada_amuletos = ttk.Entry(root, font=("Helvetica", 12), width=50)
entrada_amuletos.pack(pady=10)

# Frame para os botões
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

# Botão para verificar os amuletos
verificar_button = tk.Button(
    button_frame,
    text="Verificar Amuletos",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=verificar_amuletos,
)
verificar_button.grid(row=0, column=0, padx=5)

# Botão para reiniciar
reiniciar_button = tk.Button(
    button_frame,
    text="Reiniciar",
    font=("Helvetica", 12, "bold"),
    bg="#FF5722",
    fg="white",
    command=reiniciar,
)
reiniciar_button.grid(row=0, column=1, padx=5)

# Exibição do resultado
resultado_label = tk.Label(
    root,
    textvariable=resultado,
    font=("Helvetica", 12),
    fg="yellow",
    bg="black",
    wraplength=600,
)
resultado_label.pack(pady=10)

# Exibição do processamento
processamento_label = tk.Label(
    root,
    textvariable=processamento,
    font=("Courier New", 11),
    fg="white",
    bg="black",
    justify="left",
    anchor="w",
    wraplength=600,
)
processamento_label.pack(pady=10)

# Rodar o loop principal
root.mainloop()
