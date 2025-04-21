from collections import Counter

def calcular_poder_frutas(frutas):
    total = len(frutas)
    contagem = Counter(frutas)

    poderes = []
    for fruta, qtd in contagem.items():
        poder = (qtd / total) * 100
        poderes.append(f"{fruta}: {round(poder, 1)}%")

    # Ordenar do maior para o menor percentual
    poderes.sort(key=lambda x: float(x.split(": ")[1].replace("%", "")), reverse=True)
    return poderes

# Exemplo de uso:
entrada = ['maçã', 'banana', 'cereja', 'maçã', 'pera', 'banana', 'cereja', 'maçã']
resultado = calcular_poder_frutas(entrada)

# Exibindo o resultado mágico 🧚
print("🍓 Poder mágico das frutas:")
for r in resultado:
    print(f"  ✨ {r}")
