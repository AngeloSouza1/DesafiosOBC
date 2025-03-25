def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def soma_dos_digitos(numero):
    return sum(int(digito) for digito in str(numero))

def encontrar_numero_magico():
    primos = [n for n in range(2, 20) if eh_primo(n)]
    soma_primos = sum(primos)
    
    if soma_dos_digitos(soma_primos) <= 25 and soma_primos % 10 == 7:
        print(f"✨ Número mágico encontrado: {soma_primos}")
        print(f"🔢 Primos somados: {primos}")
        print(f"🔎 Soma dos dígitos: {soma_dos_digitos(soma_primos)}")
        print(f"🧮 Resto da divisão por 10: {soma_primos % 10}")
    else:
        print("❌ Nenhum número mágico encontrado com os critérios dados.")

# Executar
encontrar_numero_magico()
