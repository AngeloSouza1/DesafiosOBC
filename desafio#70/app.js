// Função para filtrar planetas com tamanho > 1000 e distância < 3000
function filtrarPlanetas(matriz) {
    return matriz
    .filter(planeta => planeta[0] !== 'Terra' && planeta[1] > 1000 && planeta[2] < 3000)
    .map(planeta => planeta[0]);
}

// Exemplo de uso
const matrizPlanetas = [
    ['Terra', 510072, 0],
    ['Marte', 1448, 225],
    ['Júpiter', 61419, 588],
    ['Saturno', 42700, 1200],
    ['Planeta-X', 950, 3200]
];

const planetasFiltrados = filtrarPlanetas(matrizPlanetas);

console.log("\uD83D\uDE80✨ Embarque na Missão Espacial das Matrizes! ✨\uD83D\uDE80\n");
console.log("==============================================");
console.log("🌌 Setor da Galáxia Analisado:");
console.log(matrizPlanetas.map(p => `   🪐 ${p[0]} - Tamanho: ${p[1]}, Distância: ${p[2]}`).join('\n'));
console.log("----------------------------------------------");
console.log("🌠 Planetas Selecionados:");
console.log(`   🚀 ${planetasFiltrados.join(', ')}`);
console.log("==============================================\n");
console.log("🌟 Aliste-se agora e nos ajude a mapear a galáxia!");
