const { preverAlinhamento } = require('./modulo_previsao');

document.getElementById('predictButton').addEventListener('click', () => {
    const serieInput = document.getElementById('serieInput').value;
    const resultDiv = document.getElementById('result');

    if (!serieInput) {
        resultDiv.innerHTML = "❌ Por favor, insira uma série de números.";
        return;
    }

    try {
        const series = serieInput.split(',').map(num => parseInt(num.trim(), 10));
        const nextAlignment = preverAlinhamento(series);
        resultDiv.innerHTML = `✨ Próximo alinhamento previsto: ${nextAlignment}`;
    } catch (error) {
        resultDiv.innerHTML = `❌ Erro: ${error.message}`;
    }
});
