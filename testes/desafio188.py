def decifrar_painel(mensagem):
    total = 0
    for char in mensagem:
        if char.isdigit():
            total += int(char)
        elif char.islower():
            total += ord(char) - 96
    return total


print(decifrar_painel("a1b*9c!"))     
print(decifrar_painel("z9x#2!"))      
print(decifrar_painel("@#$%"))        
print(decifrar_painel("abc123"))      
