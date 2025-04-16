function podeFormarPalindromo(assentos) {
    const contagem = {};
  
    for (let num of assentos) {
      contagem[num] = (contagem[num] || 0) + 1;
    }
  
    let impares = 0;
  
    for (let qtd of Object.values(contagem)) {
      if (qtd % 2 !== 0) {
        impares++;
      }
    }
  
    const resultado = impares <= 1;
  

    console.log("º Assentos recebidos:", JSON.stringify(assentos));
    console.log("º Contagem dos números:", contagem);
    console.log("º Números com contagem ímpar:", impares);
    console.log("º Pode formar palíndromo? ➤", resultado ? "✅ SIM!" : "❌ NÃO!");
    console.log("=".repeat(60));
  
    return resultado;
  }
  

  podeFormarPalindromo([1, 2, 3, 2, 1]); // true
  podeFormarPalindromo([1, 2, 3]);       // false
  podeFormarPalindromo([7, 7, 3, 3, 3]); // true
  podeFormarPalindromo([4, 5, 6, 7]);    // false
  