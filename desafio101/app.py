import re

def contar_chaves(salas):
    total_chaves = 0
    print("\n🏰 Bem-vindo à Jornada do Herói no Mundo de Python! 🛡️🐍\n")
    
    for idx, sala in enumerate(salas, start=1):
        numeros = re.findall(r'\d', sala)  # Encontrar todos os números individuais
        soma = sum(int(n) for n in numeros)  # Somar os números
        
        print(f"📍 Sala {idx}: {sala}")
        print(f"   🔢 Números encontrados: {' + '.join(numeros)} = {soma}")
        
        if soma % 2 == 0:
            print(f"   ✅ A soma é **par**! O herói conquista uma chave! 🔑🎉")
            total_chaves += 1
        else:
            print(f"   ❌ A soma é **ímpar**. O herói **não** recebe uma chave. 😞")
        
        print("-" * 50)  # Separador para melhor visualização

    print(f"\n🏆 **Missão Concluída!** O herói coletou **{total_chaves}** chaves! 🔑💪")
    return total_chaves

# 🔹 **Exemplo de entrada e teste**
salas_exemplo = ['sala-1: 🗝️12ab&*3', 'sala-2: %%1xx34', 'sala-3: 9*&^']
resultado = contar_chaves(salas_exemplo)
: 12
🔑 Total de chaves conquistadas: 2