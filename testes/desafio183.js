function decodificarMensagem(mensagem) {
  const vogais = { a: 'e', e: 'i', i: 'o', o: 'u', u: 'a' };
  
  return mensagem
    .split('')
    .map(char => {
      const lower = char.toLowerCase();

      if (vogais[lower]) {
        const novaVogal = vogais[lower];
        return char === char.toUpperCase()
          ? novaVogal.toUpperCase()
          : novaVogal;
      }

      
      if (/\d/.test(char)) {
        return parseInt(char, 10).toString(2);
      }

      
      return char;
    })
    .join('');
}


console.log(decodificarMensagem("Olá, Mundo 123!"));


console.log(decodificarMensagem("Espaço 9!"));

