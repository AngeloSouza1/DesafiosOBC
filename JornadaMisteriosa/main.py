from itertools import combinations

gst


if __name__ == "__main__":
    entrada = [3, 4, -7, 1, 3, 3, 1, -4]
    saida_esperada = [[3, 4, -7], [-7, 1, 3, 3], [3, 1, -4]]

    resultado = sublistas_com_soma_zero(entrada)

    # Exibir os resultados
    print("\nSublistas Contínuas com Soma Zero Encontradas:")
    for i, sublista in enumerate(resultado):
        print(f"{i + 1}. {sublista}")

    # Validação do Resultado
    print("\nValidação:")
    if resultado == saida_esperada:
        print("✔ Resultado correto!")
    else:
        print(f"✘ Erro! Resultado esperado: {saida_esperada}, mas obteve: {resultado}")
