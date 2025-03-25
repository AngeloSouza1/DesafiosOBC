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

# ✨ Função principal para encontrar o número mágico
def encontrar_numero_magico_dinamico():
    primos = [i for i in range(2, 100) if eh_primo(i)]
    primos.sort(reverse=True)

    soma_total = sum(primos)
    print(f"🔎 Soma total dos primos menores que 100: {soma_total}")

    for i in range(len(primos)):
        parcial = soma_total - sum(primos[:i])
        soma_digitos = soma_dos_digitos(parcial)

        print(f"🧮 Testando número: {parcial} | Soma dos dígitos: {soma_digitos} | Resto por 10: {parcial % 10}")

        if soma_digitos <= 25 and parcial % 10 == 7:
            print("\n🚀 Número Mágico Encontrado!")
            print(f"🔐 Número: {parcial}")
            print("✅ Regras atendidas:")
            print("   ✔ Soma de primos menores que 100")
            print("   ✔ Soma dos dígitos <= 25")
            print("   ✔ Resto por 10 igual a 7")
            return parcial

    print("\n❌ Nenhum número mágico atende a todas as condições.")
    return None

# 🚀 Executa a função
encontrar_numero_magico_dinamico()
