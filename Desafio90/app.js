// Função para decifrar uma mensagem cifrada com a Cifra de César (deslocamento de -1)
function decifrarCifraCesar(mensagem) {
    return mensagem.split('').map(char => {
        if (/[a-zA-ZÀ-ÿ]/.test(char)) { // Inclui caracteres acentuados
            let codigo = char.charCodeAt(0);
            let novoCodigo = codigo - 1;
            
            if (char === 'a') novoCodigo = 'z'.charCodeAt(0);
            if (char === 'A') novoCodigo = 'Z'.charCodeAt(0);
            
            return String.fromCharCode(novoCodigo);
        }
        if (char === '!') return ' '; // Substitui '!' por espaço
        if (char === ' ') return "'"; // Substitui espaço extra por apóstrofo
        return char; // Mantém outros caracteres especiais
    }).join('');
}

// Exemplo de uso
const mensagemCifrada = "Uif!hpmefo!lfz!up!uif!vojwfstf t!tfdsfut!jt!ivoo!pg!dpogvtjpo";
const mensagemDecifrada = decifrarCifraCesar(mensagemCifrada);

console.log("\uD83C\uDF0C✨ Decifrador Intergaláctico ✨\uD83C\uDF0C\n");
console.log("==============================================");
console.log("🔐 Mensagem Cifrada:");
console.log(`   "${mensagemCifrada}"`);
console.log("----------------------------------------------");
console.log("🔓 Mensagem Decifrada:");
console.log(`   "${mensagemDecifrada}"`);
console.log("==============================================\n");
console.log("🌟 Que o código esteja com você!");