function ehPrimo(num) {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function identificarNumerosPrimos(lista) {
  return lista.filter(ehPrimo);
}

// Teste
const asteroides = [4, 7, 9, 11, 13, 17, 19, 22];
const primosMineraveis = identificarNumerosPrimos(asteroides);

console.log("🛰️ Asteroides com Números Primos:");
console.log(primosMineraveis);
