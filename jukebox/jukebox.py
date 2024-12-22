from collections import deque

def min_operations_with_steps(initial, target):
    """
    Calcula o menor número de operações para transformar 'initial' em 'target'.
    Retorna uma lista detalhada de passos para visualização.
    """
    if initial == target:
        return 0, [(initial, "Início")]
    
    # Fila para BFS: armazena pares (valor_atual, passos, histórico)
    queue = deque([(initial, 0, [(initial, "Início")])])
    visited = set()  # Para evitar ciclos
    
    while queue:
        current, steps, path = queue.popleft()
        
        # Se já visitamos este valor, pule
        if current in visited:
            continue
        visited.add(current)
        
        # Verifica se atingimos o alvo
        if current == target:
            return steps, path
        
        # Gerar próximas operações válidas
        next_values = [
            (current * 2, "Multiplicação por 2"),  # Multiplicação
            (current + 1, "Adição de 1"),          # Soma
            (current - 1, "Subtração de 1"),      # Subtração
        ]
        
        # Divisão inteira só é válida se for exata
        if current % 2 == 0:
            next_values.append((current // 2, "Divisão por 2"))
        
        # Adicionar próximas operações à fila
        for next_val, operation in next_values:
            # Ignorar valores inválidos (somente números positivos)
            if next_val > 0 and next_val not in visited:
                queue.append((next_val, steps + 1, path + [(next_val, operation)]))
    
    # Caso o alvo não seja atingido, retorne infinito (teoricamente impossível aqui)
    return float('inf'), []
