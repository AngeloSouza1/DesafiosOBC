from sympy import isprime  # Biblioteca para verificar números primos

def contar_pares_harmonicos(notas):
    print("\n🎹✨ Bem-vindo ao Enigma do Piano Encantado! 🎶🔮\n")
    print(f"🎼 Notas mágicas fornecidas: {notas}\n")

    pares_harmonicos = []
    
    for i in range(len(notas) - 1):
        if isprime(abs(notas[i] - notas[i + 1])): 
            pares_harmonicos.append((notas[i], notas[i + 1]))

    print("🎶🔍 Analisando os pares harmônicos...\n")

    if pares_harmonicos:
        print("🎵✨ PARES HARMÔNICOS ENCONTRADOS:")
        for par in pares_harmonicos:
            print(f"🎶 {par[0]} 🎵 {par[1]}")
    else:
        print("❌ Nenhum par harmônico encontrado! O piano permanece em silêncio... 😔")

    print(f"\n🎼 Total de pares harmônicos encontrados: {len(pares_harmonicos)}\n")
    print("🎹🎶 O segredo musical foi revelado! Obrigado, maestro dos enigmas! 🔮✨\n")

    return len(pares_harmonicos)

# 🔹 **Exemplo de entrada e teste**
notas_magicas = [1, 3, 5, 7, 9]
contar_pares_harmonicos(notas_magicas)
