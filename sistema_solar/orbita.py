def calcular_voltas(angulos):
 
    angulos = sorted([angulo % 360 for angulo in angulos])

    if len(angulos) <= 1:
        return 1

    voltas = 1
    pattern = angulos[1] - angulos[0]

    for i in range(2, len(angulos)):
        diferenca = angulos[i] - angulos[i - 1]
        if diferenca != pattern:
            voltas += 1
            pattern = diferenca

    return voltas
