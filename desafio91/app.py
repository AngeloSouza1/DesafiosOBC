def soma_multiplos(n):
    """
    Retorna a soma de todos os múltiplos de 3 ou 5 abaixo de n.

    Args:
        n (int): Número limite superior (exclusivo).

    Returns:
        int: Soma dos múltiplos de 3 ou 5 abaixo de n.
    """
    soma = 0
    multiplos = []

    print(f"\n⚔️ [INICIANDO] Calculando soma de múltiplos de 3 ou 5 abaixo de {n}")

    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            multiplos.append(i)
            soma += i
            print(f"✅ [MULTIPLO ENCONTRADO] {i} → Soma parcial: {soma}")

    print(f"\n📜 [RESULTADO] Múltiplos encontrados: {multiplos}")
    print(f"🔮 [SOMA FINAL] {soma}")

    return soma

# Teste
n = 10
resultado = soma_multiplos(n)
print(f"\n🔰 [RESPOSTA FINAL] Soma dos múltiplos abaixo de {n}: {resultado}")
