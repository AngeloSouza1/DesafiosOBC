
def batalha_dos_dragoes(energia_inicial_a, energia_inicial_b, itens_a, itens_b):
 
    energia_total_a = energia_inicial_a + sum(itens_a)
    energia_total_b = energia_inicial_b + sum(itens_b)

    if energia_total_a > energia_total_b:
        return "Dragão A"
    elif energia_total_b > energia_total_a:
        return "Dragão B"
    else:
        return "Empate"
