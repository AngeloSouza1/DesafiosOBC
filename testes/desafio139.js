function numeroMagico(A, B, n) {
    if (n === 1) return A;
    if (n === 2) return B;
  
    const sequencia = [A, B];
  
    for (let i = 2; i < n; i++) {
      const soma = sequencia[i - 1] + sequencia[i - 2];
      const digitos = soma.toString().split('').map(Number);
      const somaDosDigitos = digitos.reduce((acc, val) => acc + val, 0);
      sequencia.push(somaDosDigitos);
    }
  
    return sequencia[n - 1];
  }
  
  // 🧪 Exemplo:
  const A = 9;
  const B = 5;
  const n = 4;
  
  const resultado = numeroMagico(A, B, n);
  
  // 🖨️ Saída formatada
  console.log(`\n🔮 O ${n}º número mágico da sequência é: ${resultado}`);
  