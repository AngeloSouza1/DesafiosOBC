function ehPalindromo(n) {
  const s = String(n);
  return s === s.split('').reverse().join('');
}

function encontrarPalindromoDiv11(minimo) {
  let numero = minimo + 1;

  while (true) {
    if (ehPalindromo(numero) && numero % 11 === 0) {
      return numero;
    }
    numero++;
  }
}


const resultado = encontrarPalindromoDiv11(123456);
console.log("⏳ Número-palíndromo válido encontrado:", resultado);
