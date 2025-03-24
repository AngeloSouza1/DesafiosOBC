# 🔍 Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 🔢 Soma os dígitos de um número
def soma_dos_digitos(n):
    return sum(int(d) for d in str(n))

# ✨ Função principal com os novos critérios (primos < 20)
def encontrar_numero_magico_atualizado():
    primos = [i for i in range(2, 20) if eh_primo(i)]
    soma_primos = sum(primos)
    soma_digitos = soma_dos_digitos(soma_primos)

    print("🚀 Missão: Encontrar o número mágico com base nos novos critérios!")
    print(f"🔢 Primos < 20 encontrados: {primos}")
    print(f"📊 Soma dos primos: {soma_primos}")
    print(f"🧮 Soma dos dígitos de {soma_primos}: {soma_digitos}")
    print(f"➗ Resto da divisão por 10: {soma_primos % 10}")

    # Verificações finais
    if soma_digitos <= 25 and soma_primos % 10 == 7:
        print("\n✅ Número mágico encontrado!")
        print(f"✨ Número mágico: {soma_primos}")
        print("   ✔ Soma dos dígitos ≤ 25")
        print("   ✔ Resto da divisão por 10 = 7")
    else:
        print("\n❌ Este número não atende todos os critérios mágicos.")

# Executar
encontrar_numero_magico_atualizado()
