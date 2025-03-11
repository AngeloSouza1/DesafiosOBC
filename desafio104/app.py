def identificar_portas(portas):
    if len(portas) != 3:
        return "Erro: A entrada deve conter exatamente 3 números!"

    porta_1, porta_2, porta_3 = portas

    # Validando a lógica do enigma
    if porta_1 % 3 == 0:  # Porta 1 deve ser múltiplo de 3
        soma_digitos = sum(int(d) for d in str(porta_1))  # Soma dos dígitos de porta_1
        produto = porta_1 * soma_digitos  # Produto de porta_1 e soma_digitos

        if porta_2 == soma_digitos and porta_3 == produto:
            resultado = {
                porta_1: "🏆 Tesouro encontrado!",
                porta_2: "⚫ Poço sem fim... 💀",
                porta_3: "🔄 Volta ao início!"
            }
            return resultado
        else:
            return "Erro: Os números não seguem o padrão do enigma!"
    else:
        return "Erro: O primeiro número deve ser um múltiplo de 3!"

# 🔥 Testando o código com a entrada fornecida
portas = [15, 6, 90]
resultado = identificar_portas(portas)

# 🎭 Exibindo a saída formatada
for numero, destino in resultado.items():
    print(f"Porta {numero}: {destino}")
