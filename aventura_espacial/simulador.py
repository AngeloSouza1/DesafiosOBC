# simulador.py

def simular_viagem_espacial(repeticoes=3):
    """
    Simula uma viagem espacial através de uma sequência de planetas,
    emitindo sons característicos para cada planeta.

    Parâmetros:
    - repeticoes (int): Número de vezes que a sequência completa deve ser repetida.
    """
    planetas_e_sons = [
        ('Terra', 'Beep!'),
        ('Marte', 'Boop!'),
        ('Júpiter', 'Buzz!'),
        ('Saturno', 'Bing!'),
        ('Nébula', 'Wooosh!')
    ]

    for _ in range(repeticoes):
        for planeta, som in planetas_e_sons:
            print(som, end=' ')
