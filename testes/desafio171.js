function verificarMissao(nomeMissao) {
  function ehPrimo(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  const soma = nomeMissao
    .normalize("NFD") 
    .replace(/[\u0300-\u036f]/g, '') 
    .toLowerCase()
    .replace(/[^a-z]/g, '') 
    .split('')
    .reduce((acc, letra) => acc + (letra.charCodeAt(0) - 96), 0);

  return ehPrimo(soma) ? "Missão Mágica!" : "Missão Comum...";
}



console.log(verificarMissao("Resgatar Princesa"));      
console.log(verificarMissao("Resgatar Princesa Vi"));   
console.log(verificarMissao("Salvar o Reino"));         
console.log(verificarMissao("Derrotar o Dragão"));      
