
// 🛡️ Função que retorna o cavaleiro que derrota o dragão
function enfrentarDragao(tipoDragao) {
    const fraquezas = {
        Fogo: "Cavaleiro de Água",
        Água: "Cavaleiro de Terra",
        Terra: "Cavaleiro de Fogo",
        Ar: "Cavaleiro de Terra"
    };

    return fraquezas[tipoDragao];
}

// 🧪 Testes de exemplo
const dragoes = ["Fogo", "Água", "Terra", "Ar"];
console.log("🐉✨ Saga dos Dragões Elementais ✨🐉");
console.log("==============================================");
console.log("|   Dragão   |    Cavaleiro que o derrota    |");
console.log("|------------|-------------------------------|");

dragoes.forEach(dragao => {
    const resposta = enfrentarDragao(dragao);
    console.log(`| ${dragao.padEnd(10, ' ')} | ${resposta.padEnd(30, ' ')} |`);
});

console.log("==============================================");
console.log("⚔️ A vitória é sua, bravo aventureiro!");
