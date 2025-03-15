// Função para reorganizar as letras em ordem alfabética, preservando os caracteres especiais
function encontrarCodigo(texto) {
    // Extrai apenas as letras e ordena
    const letrasOrdenadas = texto.replace(/[^a-zA-Z]/g, '').split('').sort();
    let index = 0;
    
    // Reconstrói a string, mantendo os caracteres especiais nas mesmas posições
    return texto.split('').map(char => /[a-zA-Z]/.test(char) ? letrasOrdenadas[index++] : char).join('');
}

// Exemplos de uso
const exemplos = [
    "a#c@d!e?g%",
    "g#e@d!c?b%a",
    "z!y@x#w$v%u",
    "m#n@o!p?q%r"
];

console.log("\u2694\uFE0F✨ Aventura do Código Perdido! ✨\u2694\uFE0F\n");
console.log("==============================================");

exemplos.forEach((entrada, index) => {
    const resultado = encontrarCodigo(entrada);
    console.log(`🛡️ Exemplo ${index + 1}:`);
    console.log(`   🔤 Entrada: "${entrada}"`);
    console.log(`   ✨ Código Organizado: "${resultado}"`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🏰 Ajude-nos a encontrar o Código Perdido! 💻⚔️");
