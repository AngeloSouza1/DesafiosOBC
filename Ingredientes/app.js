function criarPlaylistIngredientes(ingredientes) {

    const tabelaGeneros = {
        'Alho': 'Salsa',
        'Tomate': 'Jazz',
        'Manjericão': 'Rock',
        'Queijo': 'Clássico',
        'Macarrão': 'Pop',
        'Pimenta': 'Reggae'
    };

 
    let playlist = `
===========================
🎵🎶 COZINHANDO COM MÚSICAS 🎶🎵
===========================\n`;

 
    ingredientes.forEach(ingrediente => {
        const genero = tabelaGeneros[ingrediente] || 'Desconhecido';
        if (genero !== 'Desconhecido') {
            playlist += `✅ Ingrediente: ${ingrediente.padEnd(10)} ➡️ Gênero: ${genero}\n`;
        } else {
            playlist += `❌ Ingrediente: ${ingrediente.padEnd(10)} ➡️ Gênero: Não encontrado\n`;
        }
    });

    playlist += `
===========================
🌟 Aproveite sua dança culinária! 🌟
`;

    return playlist;
}

// Exemplo de uso
const ingredientesEntrada = ['Alho', 'Tomate', 'Macarrão', 'Chocolate'];
const playlist = criarPlaylistIngredientes(ingredientesEntrada);

console.log(playlist);
/* Saída esperada:

===========================
🎵🎶 COZINHANDO COM MÚSICAS 🎶🎵
===========================
✅ Ingrediente: Alho       ➡️ Gênero: Salsa
✅ Ingrediente: Tomate     ➡️ Gênero: Jazz
✅ Ingrediente: Macarrão   ➡️ Gênero: Pop
❌ Ingrediente: Chocolate  ➡️ Gênero: Não encontrado
===========================
🌟 Aproveite sua dança culinária! 🌟
*/
