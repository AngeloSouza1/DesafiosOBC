def maior_palindromo_produto(n):
    maior = 0
    inicio = 10**(n-1)
    fim = 10**n

    for i in range(fim - 1, inicio - 1, -1):
        for j in range(i, inicio - 1, -1):
            produto = i * j
            if produto <= maior:
                break  
            if str(produto) == str(produto)[::-1]:
                maior = produto
                print(f"🔎 Novo palíndromo encontrado: {produto} = {i} x {j}")

    return maior


n = 2
resultado = maior_palindromo_produto(n)
print(f"\n🔥 Maior palíndromo formado pelo produto de dois números de {n} dígitos: {resultado}")
