function decifraDragao(mensagem) {
    return mensagem.split('').map(char => {
      if (char >= 'a' && char <= 'z') {
        // Código ASCII do oposto: 'a' => 97, 'z' => 122
        const codigoOposto = 122 - (char.charCodeAt(0) - 97);
        return String.fromCharCode(codigoOposto);
      } else {
        // Mantém espaços e caracteres especiais
        return char;
      }
    }).join('');
  }
  
  // 🧪 Teste de exemplo:
  const mensagem = "dsviv k zg";
  const resultado = decifraDragao(mensagem);
  
  // ✨ Resultado
  console.log("🐉 Mensagem dos Dragões:", mensagem);
  console.log("🧙 Tradução para o idioma humano:", resultado);
