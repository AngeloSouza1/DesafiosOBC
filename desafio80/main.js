// Função para inverter os bits de um número binário
function opostoMagico(binario) {
    let resultado = '';

    for (let i = 0; i < binario.length; i++) {
        if (binario[i] === '0') {
            resultado += '1';
        } else if (binario[i] === '1') {
            resultado += '0';
        } else {
            throw new Error("Entrada inválida: a string deve conter apenas '0' e '1'.");
        }
    }

    return resultado;
}

// Exemplos de uso
const exemplos = [
    { entrada: '101', esperado: '010' },
    { entrada: '111', esperado: '000' },
    { entrada: '000', esperado: '111' },
    { entrada: '11001', esperado: '00110' }
];

console.log("\u2728✨ O Jogo dos Opostos! ✨\u2728\n");
console.log("==============================================");

exemplos.forEach(({ entrada, esperado }, index) => {
    const resultado = opostoMagico(entrada);
    console.log(`🪞 Exemplo ${index + 1}:`);
    console.log(`   🔢 Entrada: "${entrada}"`);
    console.log(`   🌠 Resultado: "${resultado}"`);
    console.log(`   🎯 Esperado: "${esperado}"`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("⚔️ A magia dos opostos brilha no Reino Binário! 🌌");
