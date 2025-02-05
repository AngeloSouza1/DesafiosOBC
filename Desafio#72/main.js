// Função para verificar se o herói consegue completar a jornada
function calculateJourney(caminho, energiaInicial) {
    let energia = energiaInicial;
    
    for (let i = 0; i < caminho.length; i++) {
        energia -= caminho[i];
        if (energia <= 0) {
            return false;
        }
    }
    return true;
}

// Exemplos de uso
const exemplos = [
    { caminho: [3, 2, 4, 1], energia: 10, esperado: true },
    { caminho: [5, 6, 3, 2, 5], energia: 14, esperado: false },
    { caminho: [1, 1, 1, 1, 1], energia: 5, esperado: true },
    { caminho: [10, 5, 1], energia: 12, esperado: false },
    { caminho: [2, 2, 2, 2], energia: 7, esperado: true }
];

console.log("\u2728✨ A Jornada do Herói no Mundo dos Arrays! ✨\u2728\n");
console.log("==============================================");

exemplos.forEach(({ caminho, energia, esperado }, index) => {
    const resultado = calculateJourney(caminho, energia);
    console.log(`🛡️ Exemplo ${index + 1}:`);
    console.log(`   🔢 Caminho: [${caminho.join(', ')}]`);
    console.log(`   ⚡ Energia inicial: ${energia}`);
    console.log(`   ✅ Consegue completar a jornada? ${resultado}`);
    console.log(`   🎯 Resultado esperado: ${esperado}`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🛡️ Boa sorte, e que sua lógica seja seu escudo!");
