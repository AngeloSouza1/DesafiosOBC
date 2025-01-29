from typing import List

def redistribuir_combustivel(compartimentos: List[int]) -> List[int]:
    """
    Redistribui o combustível entre os compartimentos de forma equilibrada.
    
    :param compartimentos: Lista de inteiros representando a quantidade de combustível em cada compartimento.
    :return: Nova lista com o combustível redistribuído de forma justa.
    """
    total_combustivel = sum(compartimentos)  # Soma total do combustível disponível
    num_compartimentos = len(compartimentos)  # Número de compartimentos
    
    if num_compartimentos == 0:  # Caso não existam compartimentos
        return []

    # Calcular a quantidade média de combustível por compartimento
    media = total_combustivel // num_compartimentos
    extra = total_combustivel % num_compartimentos  # Quantidade restante que não pode ser dividida igualmente

    # Criar a nova lista com combustível distribuído de forma justa
    nova_distribuicao = [media] * num_compartimentos

    # Distribuir o extra para os primeiros compartimentos
    for i in range(extra):
        nova_distribuicao[i] += 1

    return nova_distribuicao

# Testes e saída formatada
def testar_combustivel():
    testes = [
        {"entrada": [12, 5, 8, 0, 6], "descricao": "Caso base"},
        {"entrada": [10, 10, 10, 10], "descricao": "Todos compartimentos iguais"},
        {"entrada": [1, 2, 3, 4, 5], "descricao": "Combustível crescente"},
        {"entrada": [0, 0, 0, 20], "descricao": "Um compartimento com todo o combustível"},
        {"entrada": [], "descricao": "Lista vazia"},
        {"entrada": [100], "descricao": "Apenas um compartimento"},
        {"entrada": [3, 3, 3, 3, 3, 3, 30], "descricao": "Um compartimento desbalanceado"}
    ]

    for i, teste in enumerate(testes):
        entrada = teste["entrada"]
        descricao = teste["descricao"]
        resultado = redistribuir_combustivel(entrada)

        print(f"\n🚀 **Teste {i+1}: {descricao}**")
        print(f"📥 **Entrada:** {entrada}")
        print(f"⚖️ **Distribuição Equilibrada:** {resultado}\n")

# Executar os testes
if __name__ == "__main__":
    testar_combustivel()
