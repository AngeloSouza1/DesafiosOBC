function menorNumeroNaoFormavel(vetor) {
    vetor.sort((a, b) => a - b);
  
    let menorNaoFormavel = 1;
  
    for (let num of vetor) {
      if (num > menorNaoFormavel) break;
      menorNaoFormavel += num;
    }
  
    return menorNaoFormavel;
  }
  
  
  console.log("🔍 Saída 1:", menorNumeroNaoFormavel([1, 2, 2, 7]));    
  console.log("🔍 Saída 2:", menorNumeroNaoFormavel([1, 1, 1, 1]));    
  console.log("🔍 Saída 3:", menorNumeroNaoFormavel([2, 3, 4, 10]));   

  