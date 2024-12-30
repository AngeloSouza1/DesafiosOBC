import tkinter as tk
from tesouro import encontrar_tesouro

def exibir_popup(mensagem, tipo="info"):
    """Cria um popup personalizado."""
    print(f"[LOG] Exibindo popup ({'Sucesso' if tipo == 'info' else 'Erro'}): {mensagem}")
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
        if tipo == "info":
            print("[LOG] Limpando o campo de entrada.")  # Log da limpeza
            entry_sequencia.delete(0, tk.END)  # Limpa o campo de entrada

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

def processar_sequencia():
    """Processa a sequência inserida pelo usuário."""
    entrada = entry_sequencia.get().strip()
    print(f"[LOG] Entrada recebida: {entrada}")

    try:
        # Converte a entrada em uma lista de números inteiros
        sequencia = list(map(int, entrada.split(',')))
        print(f"[LOG] Sequência convertida: {sequencia}")

        # Calcula a combinação secreta
        resultado = encontrar_tesouro(sequencia)
        print(f"[LOG] Combinação Secreta calculada: {resultado}")

        # Exibe o resultado no popup
        exibir_popup(f"Combinação Secreta: {resultado} 🗝️", tipo="info")
    except ValueError as e:
        print(f"[LOG] Erro ao processar entrada: {e}")
        exibir_popup("Por favor, insira uma sequência válida de números separados por vírgula. 🚨", tipo="erro")

# Configuração principal do Tkinter
root = tk.Tk()
root.title("Encontrar Tesouro")
root.geometry("400x350")
root.configure(bg="#1e1e2f")

# Estilo
label_titulo = tk.Label(
    root,
    text="🗺️ Descubra a Combinação Secreta 🗝️",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
)
label_titulo.pack(pady=10)

label_instrucao = tk.Label(
    root,
    text="Digite uma sequência de números separados por vírgula:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="#cccccc"
)
label_instrucao.pack(pady=5)

entry_sequencia = tk.Entry(root, font=("Arial", 12), width=40)
entry_sequencia.pack(pady=10)

btn_processar = tk.Button(
    root,
    text="🔍 Processar",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="#ffffff",
    command=processar_sequencia
)
btn_processar.pack(pady=20)

footer_label = tk.Label(
    root,
    text="Criado por AAFS 🧑‍💻",
    font=("Arial", 10),
    bg="#1e1e2f",
    fg="#555555"
)
footer_label.pack(side="bottom", pady=10)

# Loop principal do Tkinter
print("[LOG] Aplicação iniciada.")
root.mainloop()
