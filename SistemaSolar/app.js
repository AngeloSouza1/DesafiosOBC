// Função para calcular o valor do quinto planeta
function calcularQuintoPlaneta(valorInicial) {
    const valores = [valorInicial, valorInicial ** 2]; // Inicia com os valores dos dois primeiros planetas

    console.log("\uD83D\uDF0C Valores iniciais dos planetas:", valores);

    for (let i = 2; i < 5; i++) {
        const novoValor = (valores[i - 1] ** 2) + (valores[i - 2] ** 2); // Fórmula correta
        valores.push(novoValor);
        console.log(`🪐 Planeta ${i + 1} calculado: ${novoValor}`); // Log intermediário
    }

    console.log("\uD83D\uDF0C Todos os valores calculados:", valores);

    return valores[4]; // Retorna o valor do quinto planeta
}

// Entrada do usuário (substitua este valor para testar)
const valorDoPrimeiroPlaneta = 2; // Exemplo: Entrada = 2

// Calcula o valor do quinto planeta
const valorQuintoPlaneta = calcularQuintoPlaneta(valorDoPrimeiroPlaneta);

// Exibe o resultado
console.log("\uD83D\uDE80✨ Jornada do Programador pelo Sistema Solar Reticulado ✨\uD83D\uDE80\n");
console.log("==============================================");
console.log(`🌌 Valor do primeiro planeta: ${valorDoPrimeiroPlaneta}`);
console.log(`🪐 Valor do quinto planeta: ${valorQuintoPlaneta}`);
console.log("==============================================\n");
console.log("🌟 Continue explorando o universo da programação! 🌟");
