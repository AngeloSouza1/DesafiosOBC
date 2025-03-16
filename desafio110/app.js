// Função para reorganizar as constelações mantendo substrings em ordem alfabética
function restaurarConstelacoes(mapaEstelar) {
    // Mapeia a frequência de cada caractere na string original
    let frequencia = {};
    for (let char of mapaEstelar) {
        frequencia[char] = (frequencia[char] || 0) + 1;
    }
    
    // Ordena as letras mantendo a contagem de repetições
    let letrasOrdenadas = Object.keys(frequencia).sort().map(char => char.repeat(frequencia[char])).join('');
    
    return letrasOrdenadas;
}

// Exemplos de uso
const exemplos = [
    "starplanetstar",
    "moonstarsun",
    "galaxyway"
];

console.log("\uD83D\uDEF8✨ O Mistério das Constelações Perdidas! ✨\uD83D\uDEF8\n");
console.log("==============================================");

exemplos.forEach((entrada, index) => {
    const resultado = restaurarConstelacoes(entrada);
    console.log(`🌌 Exemplo ${index + 1}:`);
    console.log(`   🔭 Entrada: "${entrada}"`);
    console.log(`   ✨ Constelações Restauradas: "${resultado}"`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🚀 Boa sorte, capitão estelar! A galáxia conta com você!");
