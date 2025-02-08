def dragon_magic(x, d):
    return (x * x) % d

def resolver_enigma():
    x = 1
    while True:
        if (dragon_magic(x, 5)  == 4 and
            dragon_magic(x, 7)  == 4 and
            dragon_magic(x, 9)  == 7 and
            dragon_magic(x, 11) == 1 and
            dragon_magic(x, 13) == 9):
            return x
        x += 1

# Resultado final
codigo_secreto = resolver_enigma()

print("\n✨🐉 ENIGMA DOS DRAGÕES RESOLVIDO 🐉✨")
print("--------------------------------------------------")
print(f"🔍 O menor número mágico que satisfaz todas as magias é: {codigo_secreto}")
print("--------------------------------------------------")
