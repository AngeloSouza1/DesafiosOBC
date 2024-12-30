def is_prime(num):
    """Verifica se um número é primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_tesouro(sequencia):
    """Retorna os números da sequência cujos índices são primos, considerando o primeiro como padrão."""
    combinacao_secreta = [sequencia[0]]  # Inclui o primeiro elemento como padrão

    # Analisando a partir do índice 2
    for i in range(2, len(sequencia)):
        if is_prime(i):
            combinacao_secreta.append(sequencia[i])

    return combinacao_secreta
