function somaNumerosMagicos(n) {
    let soma = 0;

    // Calcula a soma dos números múltiplos de 3 ou 5
    for (let i = 1; i <= n; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            soma += i;
        }
    }

    return soma;
}

function apresentarResultados() {
    // Exemplos de entradas para teste
    const exemplos = [10, 15, 3, 20, 50, 100];

    console.log(`
===========================================
🐉✨ DESAFIO DO DRAGÃO NUMÉRICO ✨🐉
===========================================`);

    exemplos.forEach(n => {
        const resultado = somaNumerosMagicos(n);
        console.log(`
📜 Entrada: n = ${n}
💡 Soma dos números mágicos: ${resultado}
-------------------------------------------`);
    });

    console.log(`
🎉 Obrigado por ajudar o cavaleiro a derrotar o Dragão Numérico!
🧙 Que sua lógica programe muitos finais felizes!
===========================================
`);
}

// Chama a função de apresentação dos resultados
apresentarResultados();
