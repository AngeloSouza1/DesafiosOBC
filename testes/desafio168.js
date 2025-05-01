function palindromeNumbers(inicio, fim) {
  const resultado = [];

  for (let i = inicio; i <= fim; i++) {
    const str = String(i);
    if (str === str.split('').reverse().join('')) {
      resultado.push(i);
    }
  }

  return resultado;
}


console.log(palindromeNumbers(100, 150));
