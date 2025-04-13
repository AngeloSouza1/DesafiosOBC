function decipherDiary(codigo) {
    const resultado = [];
    const aCode = 'a'.charCodeAt(0);
  
    function backtrack(index, caminho) {
      if (index === codigo.length) {
        resultado.push(caminho);
        return;
      }
  
      // Tenta 1 dígito
      let num1 = parseInt(codigo.substring(index, index + 1), 10);
      if (num1 >= 1 && num1 <= 9) {
        let letra1 = String.fromCharCode(aCode + num1 - 1);
        backtrack(index + 1, caminho + letra1);
      }
  
      // Tenta 2 dígitos
      let num2 = parseInt(codigo.substring(index, index + 2), 10);
      if (num2 >= 10 && num2 <= 26) {
        let letra2 = String.fromCharCode(aCode + num2 - 1);
        backtrack(index + 2, caminho + letra2);
      }
    }
  
    backtrack(0, "");
    return resultado;
  }
  
  // 🧪 Teste
  const input = "123";
  const saidas = decipherDiary(input);
  
  // 🖨️ Exibe as saídas no formato do desafio
  console.log("\n🔓 Decodificações possíveis:");
  console.log("[");
  saidas.forEach(str => console.log(`  '${str}',`));
  console.log("]");
  