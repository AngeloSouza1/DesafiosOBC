function palindromeNumbers(inicio, fim) {
  return Array.from({ length: fim - inicio + 1 }, (_, i) => i + inicio)
    .filter(n => {
      const s = String(n);
      return s === [...s].reverse().join('');
    });
}


console.log(palindromeNumbers(100, 150));
