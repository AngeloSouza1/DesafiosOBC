function decifrarMelodia(notas) {
    const escala = {
      1: 'Dó',
      2: 'Ré',
      3: 'Mi',
      4: 'Fá',
      5: 'Sol',
      6: 'Lá',
      7: 'Si'
    };
  
    function ehPrimo(n) {
      if (n < 2) return false;
      for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
      }
      return true;
    }
  
    return notas.map(n => {
      let nota = escala[n];
      if (n % 2 === 0) nota += '↑';
      return ehPrimo(n) ? `${nota} ${nota}` : nota;
    });
  }
  

const entrada = [2, 3, 4, 5, 6, 7];
const resultado = decifrarMelodia(entrada);
console.log("🎶 Saída esperada:");
console.log(resultado);
