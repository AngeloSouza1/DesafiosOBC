def organizar_criaturas(lista):
    print("\n🌳✨ Bem-vindo à Floresta Encantada! Criaturas mágicas aguardam sua ajuda! 🧙‍♂️🔮\n")
    
    print(f"🔀 Criaturas embaralhadas: {lista}")
    
    lista_ordenada = sorted(lista)  # Ordenação crescente

    print("📜✨ Usando um feitiço de ordenação...")
    print("\n🔮💫 Criaturas organizadas com sucesso! Aqui está a nova ordem:\n")
    print(f"✅ {lista_ordenada}\n")
    
    print("🌟 O equilíbrio da Floresta Encantada foi restaurado! Obrigado, mago dos dados! 🪄🎉\n")
    return lista_ordenada

# 🔹 **Exemplo de entrada e teste**
forca_criaturas = [3, 1, 4, 1, 5, 9, 2]
organizar_criaturas(forca_criaturas)
