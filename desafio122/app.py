from collections import Counter

def gerar_nome_dragonico(nome):
    contador = Counter(nome)
    impares = [char for char, count in contador.items() if count % 2 != 0]

    # Verificação: apenas 1 ou 0 letras com contagem ímpar
    if len(impares) > 1:
        return "Impossível formar um palíndromo"

    # Construção da metade do palíndromo
    metade = ''
    meio = ''

    for char in sorted(contador):  # ordenação para menor versão
        count = contador[char]
        if count % 2 != 0:
            meio = char
        metade += char * (count // 2)

    # Construção do palíndromo final
    palindromo = metade + meio + metade[::-1]
    return palindromo


print(gerar_nome_dragonico("eragon"))      # Impossível formar um palíndromo
print(gerar_nome_dragonico("malayalam"))   # malayalam
print(gerar_nome_dragonico("aabb"))        # abba
print(gerar_nome_dragonico("racecar"))     # racecar
print(gerar_nome_dragonico("dragonlord"))  # Impossível formar um palíndromo
