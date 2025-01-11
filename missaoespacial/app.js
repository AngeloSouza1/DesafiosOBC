// Função para decodificar mensagens alienígenas
function decodificarMensagem(mensagem) {
    const deslocamento = 3; // Número de posições para voltar no alfabeto
    const alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    // Decodificação da mensagem
    let mensagemDecodificada = '';

    for (const char of mensagem) {
        if (char === ' ') {
            // Mantém espaços inalterados
            mensagemDecodificada += ' ';
        } else {
            // Encontra o índice da letra decodificada
            const indiceAtual = alfabeto.indexOf(char);
            const novoIndice = (indiceAtual - deslocamento + alfabeto.length) % alfabeto.length;
            mensagemDecodificada += alfabeto[novoIndice];
        }
    }

    return mensagemDecodificada;
}

// Mensagens codificadas para teste
const mensagensCodificadas = [
    "KHOOR ZRUOG", // HELLO WORLD
    "FRQJUDWXODWLRQV", // CONGRATULATIONS
    "WKH HDUWK LV URXQG", // THE EARTH IS ROUND
    "ZHOFRPH WR WKH IXWXUH", // WELCOME TO THE FUTURE
    "BRDYH SURJUDPPHU" // BRAVE PROGRAMMER
];

// Importação dinâmica de chalk
(async () => {
    const chalk = await import('chalk'); // Importa o chalk dinamicamente

    console.log(chalk.default.blue.bold("🌌 Decodificação de Mensagens Alienígenas 🌌\n"));

    for (const mensagemCodificada of mensagensCodificadas) {
        const mensagemDecodificada = decodificarMensagem(mensagemCodificada);
        console.log(chalk.default.yellow.bold("🔹 Mensagem Codificada: ") + chalk.default.cyan(mensagemCodificada));
        console.log(chalk.default.green.bold("🔹 Mensagem Decodificada: ") + chalk.default.white(mensagemDecodificada));
        console.log(chalk.default.magenta("--------------------------------------------------\n"));
    }
})();
