def normalize(s):
    """
    Normaliza a string para verificação de palíndromo:
    converte para minúsculas e substitui 't' por 'u'.
    """
    return s.lower().replace('t', 'u')

def is_palindrome(s):
    """Retorna True se a string normalizada for igual à sua inversa."""
    s_norm = normalize(s)
    return s_norm == s_norm[::-1]

# Variável global para armazenar o melhor palíndromo encontrado
best_palindrome = ""

def buscar_palindromo(words, current="", depth=0, max_depth=2):
    """
    Busca recursivamente por uma concatenação de palavras que forme um palíndromo.
    
    Args:
        words (list): Lista de palavras disponíveis.
        current (str): String formada até o momento.
        depth (int): Número de palavras concatenadas.
        max_depth (int): Número máximo de palavras a serem concatenadas.
    """
    global best_palindrome

    if current:
        current_norm = normalize(current)
        reverso = current_norm[::-1]
        print(f"   [DEBUG] Verificando: '{current}' (normalizado: '{current_norm}') | Inverso: '{reverso}'")
    
    if current and is_palindrome(current):
        print("────────────────────────────")
        print(f"✅ [PALÍNDROMO ENCONTRADO] '{current}'")
        if len(current) > len(best_palindrome):
            best_palindrome = current
            print(f"🚀 [ATUALIZAÇÃO] Novo melhor palíndromo: '{best_palindrome}'")
    
    if depth == max_depth:
        print(f"*** [LIMITE ALCANÇADO] Profundidade {depth} atingida com '{current}'")
        return

    for word in words:
        new_str = current + word
        print(f"🔍 [BUSCANDO] Depth: {depth+1} | Tentando: '{new_str}'")
        buscar_palindromo(words, new_str, depth + 1, max_depth)

if __name__ == "__main__":
    # Exemplo do exercício
    words = ['mago', 'gnom', 'ombagog', 'amagtug', 'tugama']
    max_depth = 2  # Concatenação de 2 palavras
    print("🚀 Iniciando a busca pelo palíndromo mais longo...\n")
    buscar_palindromo(words, current="", depth=0, max_depth=max_depth)
    print("\n🔑 Palíndromo mais longo encontrado:", best_palindrome)
