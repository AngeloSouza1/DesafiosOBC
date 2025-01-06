// Função calcularMagia
function calcularMagia(numerosMagicos) {

    const totalElementos = numerosMagicos.length;
    const somaNumeros = numerosMagicos.reduce((acumulador, numero) => acumulador + numero, 0);
    const resultado = somaNumeros * totalElementos;

    // Log detalhado com emojis e explicações
    console.log("🌟 [A Magia dos Loops está sendo calculada...] 🌟");
    console.log(`🪄 Números Mágicos: ${numerosMagicos.join(", ")}`);
    console.log(`🔢 Total de Elementos: ${totalElementos}`);
    console.log(`➕ Soma dos Números Mágicos: ${somaNumeros}`);
    console.log(`✖️ Multiplicação: ${somaNumeros} * ${totalElementos}`);
    console.log(`✨ Resultado da Magia: ${resultado}`);

    return resultado;
}

// Teste da função
const numerosMagicos = [2, 3, 5];
const resultado = calcularMagia(numerosMagicos);

console.log("=============================================\n");

const numerosMagicos1 = [1, 4, 7, 9];
const resultado1 = calcularMagia(numerosMagicos1);

console.log("=============================================\n");