function findPlanets(series) {
    if (!series.length) return [];
    
   
    let planetasComuns = new Set(series[0].split(''));
    
    for (let i = 1; i < series.length; i++) {
        planetasComuns = new Set(
            [...planetasComuns].filter(letra => series[i].includes(letra))
        );
    }
    
    return [...planetasComuns].sort();
}

// Exemplos de uso
const exemplos = [
    { entrada: ['abcd', 'bcf', 'bcefg'], esperado: ['b', 'c'] },
    { entrada: ['xyz', 'yxz', 'zxy'], esperado: ['x', 'y', 'z'] },
    { entrada: ['abc', 'def', 'ghi'], esperado: [] },
    { entrada: ['aeiou', 'eioua', 'iouae'], esperado: ['a', 'e', 'i', 'o', 'u'] }
];

console.log("\uD83D\uDF0C✨ Resgate Espacial: O Enigma dos Planetas Perdidos ✨\uD83D\uDF0C\n");
console.log("==============================================");

exemplos.forEach(({ entrada, esperado }, index) => {
    const resultado = findPlanets(entrada);
    console.log(`🪐 Exemplo ${index + 1}:`);
    console.log(`   🚀 Entrada: [${entrada.join(', ')}]`);
    console.log(`   🌌 Planetas Resgatados: [${resultado.join(', ')}]`);
    console.log(`   🎯 Esperado: [${esperado.join(', ')}]`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🌟 Boa sorte e que as estrelas estejam a seu favor!");
