import re

def eh_palindromo(frase):
 
    frase_limpa = re.sub(r'[^a-z0-9]', '', frase.lower())
    return frase_limpa == frase_limpa[::-1]


print(eh_palindromo("Socorram-me, subi no ônibus em Marrocos"))  
print(eh_palindromo("Anotaram a data da maratona"))             
print(eh_palindromo("Esta frase não é um palíndromo"))          
