import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from jukebox import min_operations_with_steps

def calculate_operations():
    try:
        # Obter os valores das entradas
        initial = int(entry_initial.get())
        target = int(entry_target.get())

        # Calcular os passos
        steps, path = min_operations_with_steps(initial, target)

        # Exibir o resultado
        result_text.set(f"Menor número de operações: {steps}")

        # Limpar a tabela anterior
        for item in table.get_children():
            table.delete(item)

        # Inserir os passos na tabela
        for idx, (value, operation) in enumerate(path):
            table.insert("", "end", values=(idx, operation, value))

        # Tornar o botão "Iniciar Novamente" visível ao lado do botão de cálculo
        restart_button.grid(row=0, column=2, padx=10, pady=5)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos!")

def restart_program():
    # Limpar entradas, resultados e tabela
    entry_initial.delete(0, tk.END)
    entry_target.delete(0, tk.END)
    result_text.set("")
    for item in table.get_children():
        table.delete(item)

    # Esconder o botão "Iniciar Novamente"
    restart_button.grid_forget()

# Criar a janela principal
root = tk.Tk()
root.title("Jukebox do Multiverso 🎶")
root.geometry("700x780")
root.configure(bg="black")
root.resizable(False, False)

# Variáveis para exibição dinâmica
result_text = tk.StringVar()

# Criar os widgets
title_label = tk.Label(
    root, text="Jukebox do Multiverso 🎶", font=("Helvetica", 20, "bold"), fg="cyan", bg="black"
)
title_label.pack(pady=10)

instructions_label = tk.Label(
    root, text="Insira os números inicial e alvo:", font=("Helvetica", 14), fg="white", bg="black"
)
instructions_label.pack(pady=5)

frame_inputs = tk.Frame(root, bg="black")
frame_inputs.pack(pady=10)

label_initial = tk.Label(
    frame_inputs, text="Número Inicial:", font=("Helvetica", 12), fg="white", bg="black"
)
label_initial.grid(row=0, column=0, padx=10, pady=5)
entry_initial = ttk.Entry(frame_inputs, width=10, font=("Helvetica", 12))
entry_initial.grid(row=0, column=1, pady=5)

label_target = tk.Label(
    frame_inputs, text="Número Alvo:", font=("Helvetica", 12), fg="white", bg="black"
)
label_target.grid(row=1, column=0, padx=10, pady=5)
entry_target = ttk.Entry(frame_inputs, width=10, font=("Helvetica", 12))
entry_target.grid(row=1, column=1, pady=5)

# Frame para os botões
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=15)

button_calculate = tk.Button(
    button_frame,
    text="🎯 Calcular",
    font=("Helvetica", 14, "bold"),
    bg="#003366",  # Azul escuro
    fg="white",
    command=calculate_operations,
)
button_calculate.grid(row=0, column=0, padx=10, pady=5)

# Botão "Iniciar Novamente" (escondido inicialmente)
restart_button = tk.Button(
    button_frame,
    text="🔄 Reiniciar",
    font=("Helvetica", 14, "bold"),
    bg="#4CAF50",  # Verde escuro
    fg="white",
    command=restart_program,
)
restart_button.grid_forget()  # Esconde o botão inicialmente

result_label = tk.Label(
    root, textvariable=result_text, font=("Helvetica", 14, "bold"), fg="yellow", bg="black"
)
result_label.pack(pady=10)

steps_label = tk.Label(
    root, text="Passos para Transformação:", font=("Helvetica", 14, "bold"), fg="magenta", bg="black"
)
steps_label.pack(pady=5)

# Tabela para exibir os passos
table_frame = tk.Frame(root, bg="black")
table_frame.pack(pady=10)

table = ttk.Treeview(
    table_frame,
    columns=("Passo", "Operação", "Valor"),
    show="headings",
    height=15,
    style="Custom.Treeview",
)
table.heading("Passo", text="Passo")
table.heading("Operação", text="Operação")
table.heading("Valor", text="Valor")
table.column("Passo", width=50, anchor="center")
table.column("Operação", width=300, anchor="center")
table.column("Valor", width=100, anchor="center")
table.pack()

# Estilizar a tabela
style = ttk.Style()
style.theme_use("default")
style.configure(
    "Custom.Treeview",
    background="black",
    foreground="white",
    rowheight=25,
    fieldbackground="black",
    font=("Helvetica", 12),
)
style.map("Custom.Treeview", background=[("selected", "#003366")], foreground=[("selected", "white")])

# Rodar o loop principal
root.mainloop()
