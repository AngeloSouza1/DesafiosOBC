function decifrarCodigoMagico(codigo) {
  return codigo
    .split('')
    .reverse()
    .map(char => {
      if (/[a-z]/.test(char)) {
        return char.toUpperCase();
      } else if (/[A-Z]/.test(char)) {
        return char.toLowerCase();
      } else if (/\d/.test(char)) {
        const num = parseInt(char);
        return num % 2 === 0 ? (num / 2).toString() : (num * 3).toString();
      } else {
        return char;
      }
    })
    .join('');
}


console.log(decifrarCodigoMagico("ab3x!f2")); 
console.log(decifrarCodigoMagico("1234!@#$"));


