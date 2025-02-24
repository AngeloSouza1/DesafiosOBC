function ordenarReino(vilas) {
  return vilas
    .filter(vila => vila !== 0)    
    .sort((a, b) => a - b);        
}


const entrada = [5, 0, 9, 7, 3, 0, 2];
const resultado = ordenarReino(entrada);
console.log(" Vilas restauradas:", resultado); 

