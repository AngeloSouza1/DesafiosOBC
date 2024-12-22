const readline = require('readline');

// Função para pausar até o usuário pressionar Enter
function esperarEnter() {
    return new Promise(resolve => {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        rl.question("\nPressione Enter para continuar... ⚔️\n", () => {
            rl.close();
            resolve();
        });
    });
}

function divisiveisPorTres(numeros) {
    // Filtrar os números que são divisíveis por 3
    const divisiveis = numeros.filter(num => num % 3 === 0);

    // Ordenar os números em ordem crescente
    divisiveis.sort((a, b) => a - b);

    return divisiveis;
}

// Função para exibir a saída com moldura, centralização e emojis
async function exibirResultado(numeros) {
    console.clear(); // Limpa a tela
    console.log("=".repeat(40));
    console.log("⚔️✨ Aventuras no Reino dos Arrays! ✨⚔️".padStart(35).padEnd(40));
    console.log("=".repeat(40));
    
    console.log("\n🔮 Números mágicos recebidos:");
    console.log(" ".repeat(10) + numeros.join(", "));

    const resultado = divisiveisPorTres(numeros);

    if (resultado.length > 0) {
        console.log("\n🔥 Números divisíveis por 3, ordenados:");
        console.log(" ".repeat(10) + resultado.join(", ") + " ✨");
        console.log("\n🏰 Sir Loop-a-Lot avança em sua jornada!");
    } else {
        console.log("\n😅 Nenhum número divisível por 3 foi encontrado!");
        console.log("🕵️‍♂️ Sir Loop-a-Lot não encontrou pistas... volte mais tarde!");
    }
    console.log("=".repeat(40));

    await esperarEnter(); // Pausa até pressionar Enter
}

// Exemplo de uso
(async function () {
    const numerosMagicos = [7, 3, 9, 12, 15, 2];
    await exibirResultado(numerosMagicos);
})();
