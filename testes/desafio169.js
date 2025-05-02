function jogosDoDestino(a, b, c) {
  const pedras = [a, b, c].sort((x, y) => x - y); 
  return (pedras[0] + pedras[1] > pedras[2]) ? "Sim" : "Não";
}


console.log(jogosDoDestino(3, 4, 5));    
console.log(jogosDoDestino(10, 1, 12));  
console.log(jogosDoDestino(8, 15, 17));  
