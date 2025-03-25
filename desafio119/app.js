// 🧙‍♂️ Torre dos Feiticeiros - Palavra do Poder
function encontrarPalavraDoPoder(palavras) {
    // Obtemos a primeira letra de cada palavra
    const primeirasLetras = palavras.map(palavra => palavra[0]);

    // Obtemos a última letra de cada palavra, na ordem reversa
    const ultimasLetras = palavras.slice().reverse().map(palavra => palavra[palavra.length - 1]);

    // Juntamos tudo para formar a Palavra do Poder
    return primeirasLetras.join('') + ultimasLetras.join('');
}

// Exemplo do pergaminho mágico 🪄
const palavrasMagicas = ["magia", "dragão", "elfo"];
const palavraDoPoder = encontrarPalavraDoPoder(palavrasMagicas);

// Saída estilizada
console.log("🧙‍♂️✨ Torre dos Feiticeiros: A Palavra do Poder ✨🧙‍♂️");
console.log("==============================================");
console.log(`📜 Pergaminho: ${JSON.stringify(palavrasMagicas)}`);
console.log("----------------------------------------------");
console.log(`🔮 Palavra do Poder: "${palavraDoPoder}"`);
console.log("==============================================");
