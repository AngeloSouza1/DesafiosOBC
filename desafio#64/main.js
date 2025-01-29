// Função para decifrar a mensagem alienígena
function decifrarMensagem(codigo) {
    const alfabeto = 'abcdefghijklmnopqrstuvwxyz';
    let mensagem = '';

    for (const numero of codigo) {
        if (numero === 32) {
            mensagem += ' ';
        } else if (numero >= 1 && numero <= 26) {
            mensagem += alfabeto[numero - 1];
        }
    }
    return mensagem;
}

// Exemplo de uso
const mensagemCodificada = [3, 15, 4, 9, 14, 7, 32, 9, 19, 32, 6, 21, 14];
const mensagemDecifrada = decifrarMensagem(mensagemCodificada);

console.log("\uD83D\uDC7D✨ Missão Espacial: Decifrando a Mensagem dos Aliens! ✨\uD83D\uDC7D\n");
console.log("==============================================");
console.log(`📡 Mensagem Codificada: ${mensagemCodificada.join(', ')}`);
console.log(`🛸 Mensagem Decifrada: "${mensagemDecifrada}"`);
console.log("==============================================\n");
console.log("🌟 Que a força esteja com você! 🚀");