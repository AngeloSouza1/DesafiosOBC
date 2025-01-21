def calcular_posicao(movimentos):
    # Coordenadas iniciais (x, y)
    x, y = 0, 0

    # Processa cada movimento
    for movimento in movimentos:
        if movimento == "norte":
            y += 1
        elif movimento == "sul":
            y -= 1
        elif movimento == "leste":
            x += 1
        elif movimento == "oeste":
            x -= 1

    # Retorna a posição final otimizada
    return x, y

# Teste com o exemplo fornecido
if __name__ == "__main__":
    movimentos = ["norte", "leste", "sul", "oeste", "norte", "leste"]
    resultado = calcular_posicao(movimentos)
    print(f"\nMovimentos fornecidos: {movimentos}")
    print(f"Posição final otimizada: {resultado}")
    print(f"Coordenadas finais: x = {resultado[0]}, y = {resultado[1]}\n")
