function encontrarPalavrasEncantadas(palavras) {
    const encantadas = [];
    let somaAnterior = 0;

    for (let i = 0; i < palavras.length; i++) {
        const palavra = palavras[i];
        const tamanho = palavra.length;
        const indice = i + 1;

        if (somaAnterior === tamanho * indice) {
            encantadas.push(palavra);
        }

        somaAnterior += tamanho;
    }

    return encantadas;
}

// Exemplo de uso
const palavras = ['arbustos', 'fada', 'gigantes', 'unicórnios', 'dragão', 'misterio'];
const resultado = encontrarPalavrasEncantadas(palavras);

console.log(`🌟 Palavras encantadas encontradas na floresta:`, resultado);
