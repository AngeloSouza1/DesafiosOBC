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

function transformarDragao(rugido) {
    // Mapeamento das vogais para suas posições no alfabeto
    const mapaVogais = {
        '15': 'o',
        '21': 'u',
        '1': 'a',
        '5': 'e',
        '9': 'i'
    };

    // Expressão regular para capturar números válidos, priorizando números maiores
    const regex = /15|21|1|5|9/g;

    // Substituir cada número pelas vogais corretas
    const rugidoOriginal = rugido.replace(regex, match => mapaVogais[match]);

    return rugidoOriginal;
}

// Função para exibir os resultados como tabela
async function exibirResultados(rugidos) {
    console.clear();
    console.log("=".repeat(50));
    console.log("🐉✨ Transforme o Dragão! ✨🐉".padStart(35).padEnd(50));
    console.log("=".repeat(50));
    console.log("\n| 🌟 Rugido Original      | 🔥 Rugido Transformado  |");
    console.log("-".repeat(50));

    for (const rugido of rugidos) {
        const resultado = transformarDragao(rugido);
        console.log(`| ${rugido.padEnd(22)} | ${resultado.padEnd(22)} |`);
    }

    console.log("=".repeat(50));
    console.log("🏆 Todos os rugidos foram restaurados! O reino está salvo! 🎉");
    console.log("=".repeat(50));
    await esperarEnter();
}

// Lista de rugidos para teste
const rugidos = [
    "f9r5br51th",  // firebreath
    "h15w15r1y15u", // howorayou
    "dr1g15n",      // dragon
    "b15nn15f"      // bonnof
];

// Exibir os resultados
exibirResultados(rugidos);
