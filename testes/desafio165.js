function resgatarCorPerdida(matriz) {
    const n = matriz.length;
    let soma = 0;
  
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i !== j && i + j !== n - 1) {
          soma += matriz[i][j];
        }
      }
    }
  
    return soma;
  }
  

  const exemplo1 = [ 
    [8, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ];
  
  const exemplo2 = [
    [1, 0, 2, 4],
    [5, 6, 0, 3],
    [7, 2, 8, 1],
    [0, 3, 4, 2]
  ];
  
  console.log("🎨 Exemplo 1 - Saída:", resgatarCorPerdida(exemplo1)); 
  console.log("🎨 Exemplo 2 - Saída:", resgatarCorPerdida(exemplo2)); 
  