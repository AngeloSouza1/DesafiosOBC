// Função para encontrar o menor número cuja soma dos dígitos seja igual a magicNumber
function encontrarMenorNumero(magicNumber) {
    let numero = 1;
    
    while (true) {
        const somaDigitos = numero.toString().split('').reduce((acc, digito) => acc + parseInt(digito, 10), 0);
        if (somaDigitos === magicNumber) {
            return numero;
        }
        numero++;
    }
}

// Exemplos de uso
const exemplos = [15, 9, 11];
const resultados = exemplos.map(magicNumber => {
    const menorNumero = encontrarMenorNumero(magicNumber);
    return { magicNumber, menorNumero, soma: menorNumero.toString().split('').reduce((acc, digito) => acc + parseInt(digito, 10), 0) };
});

console.log("\uD83E\uDDD9✨ Derrote o Dragão Com a Sequência Mágica! ✨\uD83D\uDC09\n");
console.log("==============================================");
resultados.forEach(({ magicNumber, menorNumero, soma }) => {
    console.log(`🔥 Número mágico: ${magicNumber}`);
    console.log(`⚔️ Menor número encontrado: ${menorNumero}`);
    console.log(`💥 Soma dos dígitos: ${soma}`);
    console.log("----------------------------------------------");
});
console.log("==============================================\n");
console.log("🧙 Que sua magia seja forte e derrote o dragão! 🐉💪");