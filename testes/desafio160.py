def capitulo_encantado(n):
    resultado = ""
    for digito in str(n):
        d = int(digito)
        if d % 2 == 1:  # ímpar
            resultado += str(d * 2)
        else:           # par
            resultado += digito
    return int(resultado)


print(capitulo_encantado(94713))  
print(capitulo_encantado(20468))  
