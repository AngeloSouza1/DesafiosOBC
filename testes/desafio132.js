function ehPrimo(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

function primosReversiveis(numeros) {
    let resultado = [];
    for (let numero of numeros) {
        const reverso = parseInt(numero.toString().split('').reverse().join(''));
        if (ehPrimo(numero) && ehPrimo(reverso)) {
            resultado.push(numero);
        }
    }
    return resultado;
}

// 🧪 Teste com entrada do exemplo
const entrada = [5, 12, 13, 17, 31, 40, 37, 71, 72, 73, 76, 79, 97];
const saida = primosReversiveis(entrada);

// 🎯 Saída
console.log("✨ Números primos reversíveis encontrados:", saida);
