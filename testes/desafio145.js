function folhasColoridas(n) {
    if (n < 1 || n > 30) {
      throw new Error("O valor de n deve estar entre 1 e 30");
    }
  
    let fib = [1, 1];
    for (let i = 2; i < n; i++) {
      fib[i] = fib[i - 1] + fib[i - 2];
    }
  
    let soma = 0;
    for (let i = 0; i < n; i++) {
      soma += fib[i] * (i + 1); // (i + 1) porque os dias começam em 1
    }
  
    return soma;
  }
  
 
  const dia = 5;
  console.log(`🌿 Total de folhas até o dia ${dia}:`, folhasColoridas(dia)); 
  