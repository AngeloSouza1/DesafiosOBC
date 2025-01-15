function verificaRimas(palavras) {
    const finais = new Set();
  
    for (let palavra of palavras) {
      if (palavra.length >= 3) {
        const final = palavra.slice(-3);
        if (finais.has(final)) {
          return "Sim, temos uma rima!";
        }
        finais.add(final);
      }
    }
  
    return "Não há rimas por aqui.";
  }
  

// Testes
console.log(verificaRimas(['coração', 'beleza', 'portão', 'ração'])); // Sim, temos uma rima!
console.log(verificaRimas(['flor', 'amor', 'vento', 'brisa']));       // Não há rimas por aqui.
console.log(verificaRimas(['lua', 'nua', 'crua', 'frua']));           // Sim, temos uma rima!
