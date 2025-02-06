def ordenar_fragrancias(fragrancias):
    """
    Ordena uma lista de fragrâncias com base na soma dos valores ASCII de seus caracteres,
    em ordem decrescente. Em caso de empate, mantém a ordem original.

    Args:
        fragrancias (list): Lista de strings representando os nomes das fragrâncias.

    Returns:
        list: Lista ordenada conforme descrito no desafio.
    """

    # Função auxiliar para calcular a soma dos valores ASCII dos caracteres de uma fragrância
    def soma_ascii(fragrancia):
        return sum(ord(char) for char in fragrancia)

    # Ordenar em ordem decrescente pela soma dos valores ASCII, mantendo a ordem original em empates
    fragrancias_ordenadas = sorted(fragrancias, key=soma_ascii, reverse=True)

    return fragrancias_ordenadas

# Teste com a entrada fornecida
entrada = ["Jasmim", "Lavanda", "Rosa"]
saida = ordenar_fragrancias(entrada)

# Exibir resultados detalhados
print(f"Entrada: {entrada}")
for fragrancia in entrada:
    print(f"{fragrancia} tem uma soma ASCII de {sum(ord(c) for c in fragrancia)}")
print(f"Saída Esperada: {saida}")
