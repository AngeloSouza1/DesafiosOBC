def distribuir_suprimentos(suprimentos, numero_astronautas):
    """
    Distribui os suprimentos de forma equitativa entre os astronautas.

    Args:
        suprimentos (dict): Dicionário contendo a quantidade total de cada suprimento.
        numero_astronautas (int): Número total de astronautas.

    Returns:
        dict: Dicionário com a quantidade de suprimentos que cada astronauta receberá.
    """
    if numero_astronautas <= 0:
        return "Erro: O número de astronautas deve ser maior que zero."

    distribuicao = {item: quantidade // numero_astronautas for item, quantidade in suprimentos.items()}

    return distribuicao

# 🔥 **Teste com a entrada do desafio**
suprimentos = {'comida': 50, 'agua': 80, 'kits': 60}
numero_astronautas = 5

resultado = distribuir_suprimentos(suprimentos, numero_astronautas)
print(f"\n🚀 **Distribuição Equitativa dos Suprimentos:**\n{resultado}\n")

