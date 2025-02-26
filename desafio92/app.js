// Função para converter idade em anos terrestres para anos-luz (em milhas)
function idadeEmAnosLuz(idadeTerrestre) {
    const UM_ANO_LUZ_EM_MILHAS = 5.879e12; // 5.879 trilhões de milhas
    return idadeTerrestre * UM_ANO_LUZ_EM_MILHAS;
}

// Exemplos de uso
const idades = [25, 30, 40, 50];

console.log("\uD83D\uDE80✨ Transforme sua idade em anos-luz! ✨\uD83D\uDE80\n");
console.log("==============================================");

idades.forEach(idade => {
    const idadeConvertida = idadeEmAnosLuz(idade);
    console.log(`🪐 Idade terrestre: ${idade} anos`);
    console.log(`   ✨ Distância percorrida em anos-luz: ${idadeConvertida.toLocaleString('en-US')} milhas`);
    console.log(`   🚀 Isso equivale a viajar através do espaço por ${idade} anos na velocidade da luz!`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🌠 Desperte o viajante das estrelas dentro de você e explore o cosmos!");
