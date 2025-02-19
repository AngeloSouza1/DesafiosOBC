// Função para ordenar os jogadores por pontuação, mantendo a ordem original em caso de empate
function ordenarPontuacoes(jogadores) {
    return [...jogadores].sort((a, b) => b.pontuacao - a.pontuacao);
}

// Exemplo de uso
const jogadores = [
    { nome: 'Mario', pontuacao: 150 },
    { nome: 'Link', pontuacao: 200 },
    { nome: 'Donkey Kong', pontuacao: 200 },
    { nome: 'Sonic', pontuacao: 120 }
];

const rankingFinal = ordenarPontuacoes(jogadores);

console.log("\uD83C\uDFAE✨ A Batalha das Pontuações Épicas! ✨\uD83C\uDFAE\n");
console.log("==============================================");
console.log("🎮 Ranking dos Jogadores:");
rankingFinal.forEach((jogador, index) => {
    console.log(`   🏆 ${index + 1}º - ${jogador.nome}: ${jogador.pontuacao} pontos`);
});
console.log("==============================================\n");
console.log("🧙‍♂️ Que a força esteja com você para gerar o ranking definitivo!");
