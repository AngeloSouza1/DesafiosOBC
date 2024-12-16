# simulador.py

def simular_viagem_espacial(repeticoes=3):
 
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
