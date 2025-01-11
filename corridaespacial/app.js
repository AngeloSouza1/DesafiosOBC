const readline = require('readline');

// Função para calcular o tempo necessário para a viagem espacial
function calcularTempo(distancia, velocidade) {
    if (velocidade <= 0 || velocidade > 100) {
        throw new Error("\u26A0 A velocidade deve ser um número entre 1 e 100.");
    }
    if (distancia <= 0) {
        throw new Error("\u26A0 A distância deve ser um número maior que 0.");
    }

    const tempo = distancia / (velocidade / 100);
    return parseFloat(tempo.toFixed(2));
}

// Configuração do readline para interação com o usuário
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

async function iniciarCorrida() {
    const chalk = await import('chalk'); // Importação dinâmica de chalk

    console.log(chalk.default.blue.bold("\uD83C\uDF0C Bem-vindo à Corrida Espacial dos Funny Aliens! \uD83C\uDF0C\n"));

    console.log(chalk.default.green.bold("🎮 Entradas e Saídas Esperadas:\n"));
    console.log(chalk.default.yellow("| 🌌 Distância (anos-luz) | 🚀 Velocidade (% da luz) | ⏳ Tempo Esperado (anos) |")
        + "\n" + chalk.default.yellow("|------------------------|-------------------------|-------------------------|"));
    console.log(chalk.default.cyan("|           4           |           25           |          16.00         |")
        + "\n" + chalk.default.cyan("|          15           |           75           |          20.00         |")
        + "\n" + chalk.default.cyan("|           9           |           50           |          18.00         |\n"));

    rl.question(chalk.default.blue("\uD83D\uDF0C Informe a distância da corrida em anos-luz (apenas números inteiros): "), (distanciaInput) => {
        rl.question(chalk.default.blue("\uD83D\uDE80 Informe a velocidade do foguete como porcentagem da velocidade da luz (entre 1 e 100): "), (velocidadeInput) => {
            try {
                const distancia = parseInt(distanciaInput, 10);
                const velocidade = parseFloat(velocidadeInput);

                const tempo = calcularTempo(distancia, velocidade);

                console.log(chalk.default.magenta("\n\uD83D\uDF1F Resultado Final:\n"));
                console.log(chalk.default.yellow("| 🌌 Distância (anos-luz) | 🚀 Velocidade (% da luz) | ⏳ Tempo Calculado (anos) |")
                    + "\n" + chalk.default.yellow("|------------------------|-------------------------|--------------------------|"));
                console.log(chalk.default.green(`|           ${distancia.toString().padStart(6)}       |           ${velocidade.toFixed(2).padStart(6)}       |          ${tempo.toFixed(2).padStart(6)}       |`));
                console.log(chalk.default.blue("\n\uD83C\uDFC1 Obrigado por participar desta aventura intergaláctica! \uD83C\uDFC1\n"));
            } catch (error) {
                console.error(chalk.default.red(`\n\u26A0 Erro: ${error.message}\n`));
            } finally {
                rl.close();
            }
        });
    });
}

// Inicia a interação com o usuário
iniciarCorrida();
