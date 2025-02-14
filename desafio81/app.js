// Função para calcular a energia mágica gerada por combinações de ingredientes
function calcularEnergiaMagica(ingredientes) {
    const tabelaAlquimia = {
        'Eye of Newt,Dragon Scale': 50,
        'Toad Slime,Bat Wing': 30,
        'Unicorn Horn,Phoenix Feather': 100
    };

    let energiaTotal = 0;
    let usados = new Set();

    for (let i = 0; i < ingredientes.length; i++) {
        for (let j = i + 1; j < ingredientes.length; j++) {
            let combinacao1 = `${ingredientes[i]},${ingredientes[j]}`;
            let combinacao2 = `${ingredientes[j]},${ingredientes[i]}`;
            
            if (tabelaAlquimia[combinacao1] && !usados.has(combinacao1) && !usados.has(combinacao2)) {
                energiaTotal += tabelaAlquimia[combinacao1];
                usados.add(combinacao1);
                usados.add(combinacao2);
            }
        }
    }
    
    return energiaTotal;
}

// Exemplos de uso
const exemplos = [
    { entrada: ['Eye of Newt', 'Dragon Scale', 'Toad Slime', 'Bat Wing', 'Unicorn Horn', 'Phoenix Feather'], esperado: 180 },
    { entrada: ['Eye of Newt', 'Dragon Scale'], esperado: 50 },
    { entrada: ['Toad Slime', 'Bat Wing', 'Unicorn Horn', 'Phoenix Feather'], esperado: 130 },
    { entrada: ['Eye of Newt', 'Bat Wing', 'Phoenix Feather'], esperado: 0 }
];

console.log("\uD83E\uDDD9✨ A Tabela de Alquimia de PotionCraft ✨\uD83E\uDDD9\n");
console.log("==============================================");

exemplos.forEach(({ entrada, esperado }, index) => {
    const resultado = calcularEnergiaMagica(entrada);
    console.log(`🧪 Exemplo ${index + 1}:`);
    console.log(`   🧙 Ingredientes: [${entrada.join(', ')}]`);
    console.log(`   ✨ Energia Mágica Gerada: ${resultado} unidades`);
    console.log(`   🎯 Esperado: ${esperado} unidades`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🧙‍♂️ Misture bem os ingredientes e libere o poder da alquimia! ⚗️");
