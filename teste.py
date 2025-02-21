
x = int(input("Código do produto comprado: "))
y = int(input("Quantidade comprada: "))

precos = {
    1: 5.00,
    2: 3.50,
    3: 4.80,
    4: 8.90,
    5: 7.32
}

if x in precos:
    total = precos[x] * y
    print(f"Valor a pagar R${total:.2f}")
else:
    print("Código do produto inválido.")
