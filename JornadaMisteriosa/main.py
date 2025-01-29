from itertools import combinations

def sublistas_com_soma_zero(arr):
    """
    Retorna todas as sublistas contínuas de um array que têm soma igual a zero,
    com logs detalhados para depuração.

    Args:
    arr (list): Lista de inteiros.

    Returns:
    list: Lista de sublistas contínuas cuja soma é zero.
    """
    sublistas_resultado = []  # Lista para armazenar as sublistas contínuas com soma zero
    print("Início da execução")
    print(f"Entrada: {arr}\n")
    
    # Gerar todas as combinações possíveis de índices para sublistas contínuas
    for i, j in combinations(range(len(arr) + 1), 2):
        sublista = arr[i:j]
        soma_sublista = sum(sublista)
        print(f"  Índice inicial: {i}, Índice final: {j-1}, Sublista: {sublista}, Soma: {soma_sublista}")

        if soma_sublista == 0:
            print(f"    -> Sublista encontrada com soma zero: {sublista}")
            sublistas_resultado.append(sublista)

    print("\nSublistas Resultantes:", sublistas_resultado)
    return sublistas_resultado


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
