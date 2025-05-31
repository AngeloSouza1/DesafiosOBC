function codificarMensagem(frase) {
  const mapaVogais = {
    'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
    'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
  };

  return frase
    .split('')
    .map(char => mapaVogais[char] || char)
    .join('');
}

const frase = "Missões com JavaScript são sempre emocionantes!";
console.log(codificarMensagem(frase));
