// Função para preencher a sequência mágica de comprimento n
function preencherLacunas(n) {
    if (n < 2) {
        throw new Error("O valor de n deve ser maior ou igual a 2.");
    }

    const sequencia = [0, 1];

    for (let i = 2; i < n; i++) {
        sequencia.push(sequencia[i - 1] + sequencia[i - 2]);
    }

    return sequencia;
}

// Exemplos de uso
const exemplos = [
    { n: 6, esperado: [0, 1, 1, 2, 3, 5] },
    { n: 8, esperado: [0, 1, 1, 2, 3, 5, 8, 13] },
    { n: 10, esperado: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] },
    { n: 2, esperado: [0, 1] }
];

console.log("\uD83D\uDD0D✨ O Mistério dos Números Perdidos ✨\uD83D\uDD0D\n");
console.log("==============================================");

exemplos.forEach(({ n, esperado }, index) => {
    const resultado = preencherLacunas(n);
    console.log(`📜 Exemplo ${index + 1}:`);
    console.log(`   🔢 Entrada: n = ${n}`);
    console.log(`   ✨ Sequência Gerada: [${resultado.join(', ')}]`);
    console.log(`   🎯 Resultado Esperado: [${esperado.join(', ')}]`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🔮 Use o poder místico do JavaScript para restaurar a sequência completa!");
