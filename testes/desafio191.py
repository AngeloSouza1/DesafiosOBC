def oraculo_do_tempo(data):
    produto = 1
    for char in data:
        if char.isdigit():
            produto *= int(char)
    if produto > 100:
        return 'Essa data é magicamente especial!'
    else:
        return 'Nada de especial na data!'


print(oraculo_do_tempo('19-12-1991'))  
print(oraculo_do_tempo('01-01-2003'))  

