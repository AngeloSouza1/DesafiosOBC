from typing import List

def derrotar_dragao(tesouro: List[int]) -> List[int]:
    """
    Encontra a subsequência contínua com a maior soma em uma lista de inteiros.
    
    :param tesouro: Lista de números inteiros representando o tesouro do dragão.
    :return: A subsequência contínua com a maior soma.
    """
    if not tesouro:  # Se a lista estiver vazia, retorna uma lista vazia
        return []

    max_soma = float('-inf')  # Menor valor inicial possível
    soma_atual = 0
    inicio, fim = 0, 0
    temp_inicio = 0
    
    for i, num in enumerate(tesouro):
        if soma_atual <= 0:  # Reinicia a soma se for negativa
            temp_inicio = i
            soma_atual = num
        else:
            soma_atual += num
        
        if soma_atual > max_soma:  # Atualiza se encontrar uma soma maior
            max_soma = soma_atual
            inicio, fim = temp_inicio, i

    return tesouro[inicio:fim+1]

# Testes e saída formatada
def testar_dragao():
    testes = [
        {"entrada": [3, -2, 5, -1, 4, -3, 2, 3, -5], "descricao": "Caso base"},
        {"entrada": [-5, -2, -8, -1, -7], "descricao": "Todos os números negativos"},
        {"entrada": [-4, -2, 5, -9], "descricao": "Apenas um número positivo"},
        {"entrada": [1, 2, 3, 4, 5], "descricao": "Todos números positivos"},
        {"entrada": [], "descricao": "Lista vazia"},
        {"entrada": [10], "descricao": "Lista com um único número"},
        {"entrada": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "descricao": "Sequência com valores mistos"}
    ]

    for i, teste in enumerate(testes):
        entrada = teste["entrada"]
        descricao = teste["descricao"]
        resultado = derrotar_dragao(entrada)

        print(f"\n🔥 **Teste {i+1}: {descricao}** 🔥")
        print(f"📥 **Entrada:** {entrada}")
        print(f"🏆 **Subsequência Máxima:** {resultado}\n")


# Executar os testes
if __name__ == "__main__":
    testar_dragao()
