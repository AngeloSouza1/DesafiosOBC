import tkinter as tk
from tkinter import messagebox
from encontrar_tesouro import encontrar_caminho_ate_tesouro

def calcular_caminho():
    try:
        entrada = entry_coordenadas.get()
        if not entrada:
            raise ValueError("Por favor, insira as coordenadas.")
        
        # Converter a entrada em uma lista de tuplas
        coordenadas = [tuple(map(int, coord.strip().split(','))) for coord in entrada.split()]
        
        # Calcular o caminho até o tesouro
        caminho = encontrar_caminho_ate_tesouro(coordenadas)
        
        # Mostrar o resultado
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "🗺️ Caminho até o tesouro:\n\n")
        for passo, coord in enumerate(caminho, start=1):
            result_text.insert(tk.END, f"Passo {passo}: {coord}\n")
    
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Use o formato correto: x,y x,y ...")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro inesperado: {e}")

def limpar():
    entry_coordenadas.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Caçador de Tesouros Pirata 🏴‍☠️")
root.geometry("600x400")
root.config(bg="#1a1a1a")

# Título
titulo = tk.Label(root, text="🏴‍☠️ Caçador de Tesouros Pirata 🏝️", font=("Helvetica", 20, "bold"), bg="#1a1a1a", fg="#00ffcc")
titulo.pack(pady=10)

# Entrada de coordenadas
frame_entrada = tk.Frame(root, bg="#1a1a1a")
frame_entrada.pack(pady=10)

label_coordenadas = tk.Label(frame_entrada, text="Digite as coordenadas (ex: 0,0 1,2 3,4):", font=("Helvetica", 12), bg="#1a1a1a", fg="#ffffff")
label_coordenadas.pack(side=tk.LEFT, padx=10)

entry_coordenadas = tk.Entry(frame_entrada, font=("Helvetica", 14), width=30, bg="#262626", fg="#ffffff", insertbackground="#ffffff")
entry_coordenadas.pack(side=tk.LEFT, padx=10)

# Botões
frame_botoes = tk.Frame(root, bg="#1a1a1a")
frame_botoes.pack(pady=10)

btn_calcular = tk.Button(frame_botoes, text="Calcular Caminho", font=("Helvetica", 14, "bold"), bg="#00cc66", fg="#ffffff", command=calcular_caminho)
btn_calcular.pack(side=tk.LEFT, padx=10)

btn_limpar = tk.Button(frame_botoes, text="Limpar", font=("Helvetica", 14, "bold"), bg="#ff4444", fg="#ffffff", command=limpar)
btn_limpar.pack(side=tk.LEFT, padx=10)

# Área de resultados
result_text = tk.Text(root, font=("Helvetica", 12), height=10, bg="#262626", fg="#ffffff")
result_text.pack(pady=20, padx=20)

# Inicia o loop principal da interface
root.mainloop()
