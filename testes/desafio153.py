from itertools import combinations

def encontrar_elixir_ouro(ingredientes, valor_desejado):
    # Ordena a lista para tentar menores combinações primeiro
    ingredientes.sort()
    
    for r in range(1, len(ingredientes) + 1):
        for combinacao in combinations(ingredientes, r):
            if sum(combinacao) == valor_desejado:
                return list(combinacao)
    return []

# Exemplo de uso
ingredientes = [3, 5, 7, 8, 9]
valor_desejado = 17

resultado = encontrar_elixir_ouro(ingredientes, valor_desejado)
print("🧪 Ingredientes usados:", resultado)
