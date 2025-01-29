// Função para encontrar o segundo menor número único em uma lista
function segundoMenorNumero(lista) {
    // Remove duplicatas e ordena os números em ordem crescente
    const numerosUnicos = [...new Set(lista)].sort((a, b) => a - b);
    
    // Retorna o segundo menor número, se houver pelo menos dois números únicos
    return numerosUnicos.length > 1 ? numerosUnicos[1] : null;
}

// Exemplos de uso
const exemplos = [
    { entrada: [30, 15, 22, 15, 42, 7, 7, 2], esperado: 7 },
    { entrada: [10, 5, 5, 20, 3, 3, 1], esperado: 3 },
    { entrada: [100, 50, 50, 25, 10, 5, 5, 2], esperado: 5 },
    { entrada: [8, 3, 3, 3, 1, 0, 0, -1], esperado: 0 },
    { entrada: [4, 4, 4, 4, 4, 4, 4], esperado: null }, // Caso sem segundo menor número
];

console.log("\uD83E\uDDD9✨ A Caverna dos Números Místicos! ✨\uD83E\uDDD9\n");
console.log("==============================================");

exemplos.forEach(({ entrada, esperado }, index) => {
    const resultado = segundoMenorNumero(entrada);
    console.log(`📜 Exemplo ${index + 1}:`);
    console.log(`   Números fornecidos: ${entrada.join(', ')}`);
    console.log(`   🔮 Segundo menor número único: ${resultado}`);
    console.log(`   ✅ Resultado esperado: ${esperado}`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("⚔️ Que seus algoritmos sejam tão afiados quanto sua espada!");