// Função para calcular as coordenadas finais após os comandos
function calcularCoordenadas(comandos) {
    let x = 0; // Coordenada inicial em x
    let y = 0; // Coordenada inicial em y

    for (const comando of comandos) {
        const [acao, quantidadeStr] = comando.split(' ');
        const quantidade = parseInt(quantidadeStr, 10);

        switch (acao) {
            case 'frente':
                y += quantidade;
                break;
            case 'trás':
                y -= quantidade;
                break;
            case 'esquerda':
                x -= quantidade;
                break;
            case 'direita':
                x += quantidade;
                break;
            default:
                console.error(`⚠️ Comando inválido: ${acao}`);
        }
    }

    return { x, y };
}

// Exemplo de uso
const comandos = ["frente 3", "esquerda 2", "trás 1", "direita 4"];
const coordenadasFinais = calcularCoordenadas(comandos);

console.log("\uD83D\uDC7B✨ Batalha dos Fantasmas: Relatório de Movimentação ✨\uD83D\uDC7B\n");
console.log("==============================================");
console.log("\u2694️ Comandos Executados: ");
comandos.forEach((comando, index) => {
    console.log(`  ${index + 1}. ${comando}`);
});
console.log("----------------------------------------------");
console.log(`\uD83D\uDCCF Coordenadas Finais:`);
console.log(`  📍 Posição X: ${coordenadasFinais.x}`);
console.log(`  📍 Posição Y: ${coordenadasFinais.y}`);
console.log("==============================================\n");
console.log("\uD83D\uDE80 Que os espíritos estejam ao seu lado na próxima batalha! \uD83C\uDF1F");
