function somaDireita(lista) {
    const n = lista.length;
    const resultado = new Array(n); 
    let soma = 0; 
    
    // Itera de trás para frente
    for (let i = n - 1; i >= 0; i--) {
      resultado[i] = soma; // O valor atual do resultado é a soma acumulada
      soma += lista[i]; // Atualiza a soma acumulada
    }
    
    return resultado;
  }
  
  // Teste com o exemplo fornecido
  const entrada = [4, 2, 1, 3];
  const saida = somaDireita(entrada);
  
  console.log('Entrada:', entrada);
  console.log('Saída:', saida);
  