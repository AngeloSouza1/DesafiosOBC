// Função para transformar a string seguindo as regras mágicas
function transformarStringMagica(palavra) {
    const vogais = new Set(['a', 'e', 'i', 'o', 'u']);
    const alfabeto = 'abcdefghijklmnopqrstuvwxyz';
    
    let resultado = '';
    
    for (let char of palavra) {
        if (/[a-zA-Z]/.test(char)) {
            const isUpperCase = char === char.toUpperCase();
            const index = alfabeto.indexOf(char.toLowerCase());
            let novaLetra = alfabeto[(index + 1) % 26];
            
            if (vogais.has(novaLetra)) {
                novaLetra = isUpperCase ? novaLetra.toLowerCase() : novaLetra.toUpperCase();
            } else if (isUpperCase) {
                novaLetra = novaLetra.toUpperCase();
            }
            resultado += novaLetra;
        } else {
            resultado += char;
        }
    }
    return resultado;
}

// Exemplos de uso
const exemplos = [
    "hello", // Ifmmp
    "javascript", // Kbwbtdsjqu
    "Mago", // NbhP
    "OneBitCode", // PofCjuDpef
    "xyz" // yZa
];

console.log("\uD83E\uDDD9✨ A Jornada do Mago das Strings! ✨\uD83E\uDDD9\n");
console.log("==============================================");

exemplos.forEach((entrada, index) => {
    const resultado = transformarStringMagica(entrada);
    console.log(`📜 Exemplo ${index + 1}:`);
    console.log(`   🔤 Entrada: "${entrada}"`);
    console.log(`   ✨ Transformado: "${resultado}"`);
    console.log("----------------------------------------------");
});

console.log("==============================================\n");
console.log("🔮 Fortaleçam sua mente e dominem a magia das Strings!");
