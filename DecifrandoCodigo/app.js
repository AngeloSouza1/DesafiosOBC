function decodificarMensagem(codigo) {
    const numeros = codigo.split(" ");

    const converterParaLetra = (num) => {
        const posicao = Math.sqrt(Number(num));
        if (Number.isInteger(posicao) && posicao >= 1 && posicao <= 26) {
            return String.fromCharCode(96 + posicao);
        }
        return "?"; // Caso inválido, retorna um símbolo de erro
    };

    const letras = numeros.map(converterParaLetra);

    return letras.join(" ");
}

// Função para exibir o resultado de maneira estilizada
function mostrarResultado(codigo) {
    const mensagemDecodificada = decodificarMensagem(codigo);
    console.log("🛸 Código Galáctico: " + codigo);
    console.log("🔓 Mensagem Decodificada: " + mensagemDecodificada);
    console.log("-------------------------------------------------\n");
}

// Exemplos de entrada:
const exemplos = [
    "1 4 9 16 25", // "a b c d e"
    "36 49 64 81", // "f g h i"
    "121 144 169",  // "k l m"
    "225 196 169 144", // "o n m l"
    "1 100 225"     // "a j o"
];

// Mostrar resultados para cada exemplo:
console.log("🌌 Decifrando o Código Galáctico 🚀\n");
exemplos.forEach(mostrarResultado);
