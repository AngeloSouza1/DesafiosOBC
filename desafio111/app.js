// Função para calcular a sequência dos elementos mágicos
function elementalPowerSum(arr) {
    return arr.map(num => {
        let simbolo = "";
        if (num % 3 === 0) simbolo += "🔥"; // Fogo
        if (num % 5 === 0) simbolo += "💧"; // Água
        if (num % 7 === 0) simbolo += "🌱"; // Terra
        if (num % 11 === 0) simbolo += "💨"; // Ar
        return simbolo || num; // Se não for múltiplo, mantém o número
    }).join('');
}

// Exemplos de uso
const exemplos = [
    [2, 3, 5, 15, 21, 77, 8],
    [11, 14, 35, 9, 22, 55],
    [6, 10, 49, 33, 77]
];

console.log("🔥💧🌱💨 O Enigma do Mestre dos Elementos! 🔥💧🌱💨\n");
console.log("==============================================");

exemplos.forEach((entrada, index) => {
    const resultado = elementalPowerSum(entrada);
    console.log(`🌟 Exemplo ${index + 1}:`);
    console.log(`   🎯 Entrada: [${entrada.join(', ')}]`);
    console.log(`   ✨ Sequência mágica: "${resultado}"`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🍀 Que os ventos do destino soprem a seu favor!");
