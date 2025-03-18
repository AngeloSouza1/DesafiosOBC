def numero_magico(lista_numeros):
    # Calcula o Número Mágico multiplicando cada número pelo seu índice (iniciando de 1) e somando os valores
    numero_magico = sum(num * (i + 1) for i, num in enumerate(lista_numeros))

    # Saída formatada e imersiva
    print("\n🌲✨ **Decifrando o Código Secreto da Floresta Encantada** 🔍")
    print(f"📜 Código recebido: {lista_numeros}")
    print("🔢 Cálculo realizado:")
    calculo = " + ".join(f"({num}*{i+1})" for i, num in enumerate(lista_numeros))
    print(f"📊 {calculo} = {numero_magico}")
    print(f"🪄 **Número Mágico Revelado: {numero_magico}** ✨\n")

    return numero_magico

# 🔥 Testes
numero_magico([2, 3, 5, 7])
numero_magico([1, 4, 6, 8, 10])
numero_magico([9, 2, 7])
