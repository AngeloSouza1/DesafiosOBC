import re

def encontrar_codigo_secreto(palavras):
    codigo = []
    for palavra in palavras:
        matches = re.findall(r'[^aeiouAEIOU\W\d_]{3}', palavra)
        codigo.extend(matches)
    return codigo


palavras = ["dragons", "knights", "quest", "bravery"]
print(encontrar_codigo_secreto(palavras))  # ["ght"]
print(encontrar_codigo_secreto(["bcdfg", "zzzab", "trstn"]))  
