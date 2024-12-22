def classificar_elemento(elementos, novo_elemento, categorias):
    """
    Função para inserir e classificar elementos químicos em categorias.

    Args:
        elementos (list): Lista ordenada de elementos.
        novo_elemento (str): Novo elemento a ser inserido.
        categorias (dict): Dicionário com categorias e seus elementos.

    Returns:
        list: Lista atualizada com o elemento inserido.
        dict: Categorias atualizadas com o novo elemento.
        str: Mensagem com a categoria do novo elemento.
    """
    # Verificar se o elemento já está incluído
    if novo_elemento in elementos:
        raise ValueError(f"O elemento '{novo_elemento}' já foi incluído.")

    # Identificar a categoria do novo elemento
    categoria = "Outros"
    for cat, elems in categorias.items():
        if novo_elemento in elems:
            categoria = cat
            break

    # Se o elemento não estiver em nenhuma categoria, adicioná-lo à categoria "Outros"
    if categoria == "Outros":
        categorias["Outros"].append(novo_elemento)

    # Atualizar a lista de elementos
    elementos.append(novo_elemento)
    elementos.sort()

    # Atualizar as categorias (garantindo a ordem)
    categorias[categoria] = sorted(categorias[categoria])

    return elementos, categorias, f"O elemento '{novo_elemento}' foi classificado na categoria '{categoria}'."
