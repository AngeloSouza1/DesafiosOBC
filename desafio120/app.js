// 🧙 Função mágica para encontrar o número mais frequente
function magicConsole(arr) {
    const frequencia = {};

    // Contamos quantas vezes cada número aparece
    arr.forEach(num => {
        frequencia[num] = (frequencia[num] || 0) + 1;
    });

    // Procuramos o número com maior frequência e menor valor em caso de empate
    let maisFrequente = arr[0];

    for (let num in frequencia) {
        if (
            frequencia[num] > frequencia[maisFrequente] ||
            (frequencia[num] === frequencia[maisFrequente] && Number(num) < maisFrequente)
        ) {
            maisFrequente = Number(num);
        }
    }

    return maisFrequente;
}

// 🧪 Teste com exemplo da missão
const exemplo = [4, 1, 2, 2, 4, 4, 6, 7, 4, 2];
const resultado = magicConsole(exemplo);

// 🎇 Saída estilizada
console.log("🧙‍♂️✨ Jornada do Console Mágico ✨🧙‍♂️");
console.log("==============================================");
console.log(`🔢 Array de energias mágicas: ${JSON.stringify(exemplo)}`);
console.log("----------------------------------------------");
console.log(`🔮 Número mágico mais frequente: ${resultado}`);
console.log("==============================================");
