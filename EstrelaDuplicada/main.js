// Função encontrarEstrelasDuplicadas
function encontrarEstrelasDuplicadas(estrelas) {
    const contador = new Map(); // Para contar as ocorrências
    const duplicadas = []; // Para armazenar as estrelas duplicadas

    for (const estrela of estrelas) {
        // Conta as ocorrências de cada estrela
        contador.set(estrela, (contador.get(estrela) || 0) + 1);
        
        // Adiciona ao array de duplicadas se for a segunda ocorrência
        if (contador.get(estrela) === 2) {
            duplicadas.push(estrela);
        }
    }

    return duplicadas;
}

// Teste da função com saída melhorada
function main() {
    const estrelas = ["Arcturus", "Sirius", "Vega", "Arcturus", "Rigel", "Vega"];

    console.log("🌌 [Aventura Espacial: O Contador de Estrelas] 🌌\n");
    console.log("📜 Mapa Estelar:");
    console.log(`   ${estrelas.join(", ")}\n`);

    const duplicadas = encontrarEstrelasDuplicadas(estrelas);

    if (duplicadas.length > 0) {
        console.log("✨ Estrelas que aparecem mais de uma vez:");
        duplicadas.forEach((estrela, index) => {
            console.log(`   ${index + 1}. ${estrela}`);
        });
    } else {
        console.log("🌟 Nenhuma estrela duplicada foi encontrada no mapa estelar.");
    }

    console.log("\n🚀 Missão concluída! Stardust agradece sua ajuda! 🌠");
}

// Executa a função principal
main();
