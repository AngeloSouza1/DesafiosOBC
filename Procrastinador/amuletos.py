def soma_dos_digitos(numero):
    """
    Calcula a soma dos dígitos de um número.
    """
    return sum(int(digito) for digito in str(numero))

def eh_primo(numero):
    """
    Verifica se um número é primo.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_amuletos_com_processamento(amuletos):
    """
    Filtra os amuletos cuja soma dos dígitos é um número primo e retorna os passos do processamento.
    """
    processamento = []
    amuletos_dignos = []

    for amuleto in amuletos:
        soma = soma_dos_digitos(amuleto)
        primo = eh_primo(soma)
        status = "✅" if primo else "❌"
        processamento.append(f"{amuleto}: {' + '.join(str(digito) for digito in str(amuleto))} = {soma} ({'primo' if primo else 'não primo'}) {status}")
        if primo:
            amuletos_dignos.append(amuleto)

    return amuletos_dignos, "\n".join(processamento)
