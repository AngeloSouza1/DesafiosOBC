// Função para ordenar as letras de cada palavra em ordem alfabética
function ordenarLetrasNasPalavras(frase) {
    return frase.split(' ')
        .map(palavra => palavra.split('').sort().join(''))
        .join(' ');
}

// Exemplos de uso
const exemplos = [
    "salc otiolech smiusano",
    "programacao javascript desafio",
    "galaxia biblioteca robo"
];

console.log("\uD83E\uDD16📚 A Dança das Letras Desordenadas! 📚\uD83E\uDD16\n");
console.log("==============================================");

exemplos.forEach((entrada, index) => {
    const resultado = ordenarLetrasNasPalavras(entrada);
    console.log(`🤖 Exemplo ${index + 1}:`);
    console.log(`   🔤 Entrada: "${entrada}"`);
    console.log(`   ✨ Letras ordenadas: "${resultado}"`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🌌 Boa sorte, e que a força esteja com você ao ajudar nossos amigos robôs!");
