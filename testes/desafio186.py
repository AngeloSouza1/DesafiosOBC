def altura_da_torre(n):
    if n == 1:
        return 1
    a, b = 1, 1
    soma = a + b
    for _ in range(3, n + 1):
        c = a + b
        soma += c
        a, b = b, c
    return soma


print(altura_da_torre(5))   
print(altura_da_torre(10))  
print(altura_da_torre(1))   
