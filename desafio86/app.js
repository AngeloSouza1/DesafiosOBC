// Função para ordenar as palavras magicamente
function ordenarPalavras(magia) {
    return magia.split(' ').sort().join(' ');
}

// Exemplos de uso
const exemplos = [
    "dragão elfo feiticeiro mago unicórnio",
    "espada arco poção escudo bastão",
    "trovão relâmpago tempestade vendaval tornado",
    "fogo terra água ar éter"
];

console.log("\u2694\uFE0F✨ A Jornada do Herói: Batalha de Palavras ✨\u2694\uFE0F\n");
console.log("==============================================");

exemplos.forEach((entrada, index) => {
    const resultado = ordenarPalavras(entrada);
    console.log(`📜 Exemplo ${index + 1}:`);
    console.log(`   🔤 Entrada: "${entrada}"`);
    console.log(`   ✨ Ordenado: "${resultado}"`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🧙‍♂️ Que a força das palavras esteja com você! 🌟✨");
