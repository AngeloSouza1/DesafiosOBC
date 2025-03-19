function decifrarMapaAscii(listaNumeros) {
    return listaNumeros.map(num => String.fromCharCode(num)).join('');
}


const entrada = [72, 101, 108, 108, 111, 33];
const saida = decifrarMapaAscii(entrada);

console.log(`Mapa decifrado: "${saida}" `);
