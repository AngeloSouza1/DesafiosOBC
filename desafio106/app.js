
function encontrarNumerosPerdidos(sequencia) {
    const numerosPerdidos = [];
    const min = Math.min(...sequencia);
    const max = Math.max(...sequencia);
    
    for (let i = min; i <= max; i++) {
        if (!sequencia.includes(i)) {
            numerosPerdidos.push(i);
        }
    }
    
    return numerosPerdidos;
}


const sequenciaPerdida = [1, 2, 3, 5, 6, 7, 9, 10];
const numerosFaltantes = encontrarNumerosPerdidos(sequenciaPerdida);

console.log("\uD83D\uDCCA✨ A Jornada dos Números Perdidos! ✨\uD83D\uDCCA\n");
console.log("==============================================");
console.log("🔢 Sequência fornecida:");
console.log(`   ${sequenciaPerdida.join(', ')}`);
console.log("----------------------------------------------");
console.log("🧙‍♂️ Números faltantes identificados:");
console.log(`   ${numerosFaltantes.join(', ')}`);
console.log("==============================================\n");
console.log("🚀 Ajude a restaurar a paz no reino mágico dos números perdidos!");
