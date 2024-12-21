/**
 * Função que verifica se dois chefes podem preparar pratos sem repetir ingredientes.
 * 
 * @param {string[]} chefeA - Lista de ingredientes do Chefe A.
 * @param {string[]} chefeB - Lista de ingredientes do Chefe B.
 * @returns {string} - "Sim" se não houver repetição, caso contrário "Não".
 */
function verificarIngredientes(chefeA, chefeB) {
    const ingredientesA = new Set(chefeA);
    const ingredientesB = new Set(chefeB);

    // Verificar se há interseção
    for (let ingrediente of ingredientesB) {
        if (ingredientesA.has(ingrediente)) {
            return "Não";
        }
    }

    return "Sim";
}

/**
 * Função para exibir entradas e saídas de forma formatada.
 * 
 * @param {string[]} chefeA - Lista de ingredientes do Chefe A.
 * @param {string[]} chefeB - Lista de ingredientes do Chefe B.
 */
function exibirResultado(chefeA, chefeB) {
    console.log("🧑‍🍳 Chefe A:");
    console.log(`Ingredientes: [${chefeA.join(", ")}]`);
    console.log("\n🧑‍🍳 Chefe B:");
    console.log(`Ingredientes: [${chefeB.join(", ")}]`);
    console.log("\n🔎 Verificando ingredientes...");
    const resultado = verificarIngredientes(chefeA, chefeB);
    console.log(`\n✅ Resultado: ${resultado}`);
    console.log("=".repeat(40), "\n");
}

// Exemplos de teste
console.log("🌌 Bem-vindo ao Grande Concurso de Culinária Intergaláctica! 🌌\n");
const exemplos = [
    {
        chefeA: ["batata", "cenoura", "cebola"],
        chefeB: ["alho", "pimentão", "cebola"],
    },
    {
        chefeA: ["pão", "queijo", "tomate"],
        chefeB: ["açúcar", "leite", "chocolate"],
    },
    {
        chefeA: ["arroz", "feijão", "carne"],
        chefeB: ["peixe", "frango", "arroz"],
    },
    {
        chefeA: ["uva", "maçã", "banana"],
        chefeB: ["laranja", "manga", "abacaxi"],
    },
];

// Testar todos os exemplos
exemplos.forEach(({ chefeA, chefeB }, index) => {
    console.log(`🔢 Exemplo ${index + 1}`);
    exibirResultado(chefeA, chefeB);
});
