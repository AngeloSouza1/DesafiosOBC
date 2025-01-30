function isPalindromo(n) {
  const str = n.toString();
  return str === str.split('').reverse().join('');
}

function calculatePalindromicSum(start, end) {
  const palindromos = [];

  for (let i = start; i <= end; i++) {
    if (isPalindromo(i)) {
      palindromos.push(i);
    }
  }

  const soma = palindromos.reduce((acc, num) => acc + num, 0);

  console.log(`Saída esperada: ${soma} (que vem dos palíndromos ${palindromos.join(', ')})`);
  return soma;
}


calculatePalindromicSum(10, 150);
