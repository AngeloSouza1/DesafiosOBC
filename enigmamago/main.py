from collections import Counter

def reconstruir_sequencia(viagem):
    # Verificar se a lista está vazia
    if not viagem:
        return []
    
    # Contar ocorrências de cada número na entrada
    contador = Counter(viagem)
    
    # Criar um dicionário que relaciona cada número ao seu invertido
    mapa_inverso = {num: num[::-1] for num in viagem}
    
    # Encontrar o menor número lexicograficamente para iniciar a sequência
    inicio = min(viagem)
    
    # Ordenar a sequência corretamente
    sequencia_ordenada = [inicio]
    usados = Counter([inicio])
    
    while sum(usados.values()) < len(viagem):
        ultimo = sequencia_ordenada[-1]
        proximo = mapa_inverso.get(ultimo)
        
        if proximo and usados[proximo] < contador[proximo]:
            sequencia_ordenada.append(proximo)
            usados[proximo] += 1
        else:
            # Se não encontrar mais conexões, procura outro ponto de conexão
            candidatos = [num for num in sorted(viagem) if usados[num] < contador[num]]
            if candidatos:
                sequencia_ordenada.append(candidatos[0])
                usados[candidatos[0]] += 1
            else:
                # Nenhum candidato encontrado, sair para evitar loop infinito
                break
    
    return sequencia_ordenada

# Função de Teste
def testar_reconstruir_sequencia():
    casos_de_teste = [
        # Teste básico (ordem reversa)
        (["21", "12", "31", "13"], ["12", "21", "13", "31"]),
        
        # Teste já ordenado
        (["12", "21", "13", "31"], ["12", "21", "13", "31"]),
        
        # Teste com mais números
        (["98", "89", "76", "67", "54", "45"], ["45", "54", "67", "76", "89", "98"]),
        
        # Teste com números aleatórios
        (["32", "23", "41", "14", "56", "65"], ["14", "41", "23", "32", "56", "65"]),
        
        # Teste com números desconectados (deve apenas ordenar)
        (["12", "34", "56", "78"], ["12", "34", "56", "78"]),
        
        # Teste com números repetidos
        (["21", "12", "21", "12"], ["12", "21", "12", "21"]),
        
        # Teste com todos os números sendo iguais
        (["11", "11", "11"], ["11", "11", "11"]),
        
        # Teste com um único elemento
        (["99"], ["99"]),
        
        # Teste com lista vazia
        ([], []),
        
        # Teste com múltiplos pares invertidos
        (["12", "21", "13", "31", "14", "41"], ["12", "21", "13", "31", "14", "41"]),
    ]

    for idx, (entrada, esperado) in enumerate(casos_de_teste, 1):
        resultado = reconstruir_sequencia(entrada)
        passou = resultado == esperado
        status = "✅ Passou" if passou else "❌ Falhou"
        print(f"Teste {idx}: {status}")
        print(f"Entrada: {entrada}")
        print(f"Esperado: {esperado}")
        print(f"Obtido: {resultado}\n")

# Rodar os testes
if __name__ == "__main__":
    testar_reconstruir_sequencia()
