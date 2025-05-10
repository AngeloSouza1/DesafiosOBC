def proximo_numero_sonho(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    
   
    for i, d in enumerate(diffs, start=1):
        if d != 2 ** i:
            return None

    proximo_dif = 2 ** (len(diffs) + 1)
    return seq[-1] + proximo_dif

quarta_noite = [3, 5, 9, 17, 33]
print(proximo_numero_sonho(quarta_noite))  
