// Função para calcular a chave mágica
function calcularChaveMagica(n) {
    const chaveMagica = [];

    // Calcula os valores da fórmula para i variando de 0 até n-1
    for (let i = 0; i < n; i++) {
        const valor = 3 * Math.pow(i, 2) + 2 * i + 1;
        chaveMagica.push(valor);
    }

    return chaveMagica;
}

// Função principal para entrada e saída
function main() {
    const valores = [5, 7]; // Entradas para os valores de n

    console.log("🌌 [Resgate do Gatinho Byte] 🌌\n");

    for (const n of valores) {
        console.log(`🔑 Código do mundo explorado: ${n}`);
        console.log("\n✨ Calculando a chave mágica...\n");

        const chave = calcularChaveMagica(n);

        console.log("📜 Chave Mágica Gerada:");
        console.log(chave);
        console.log("\n--------------------------------------------------\n");
    }

    console.log("🚀 Missão concluída! O Byte foi resgatado com sucesso! 🐱💻");
}

// Executa a função principal
main();
