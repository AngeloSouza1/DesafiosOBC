function cifrarMensagemAlienigena(mensagem) {
    const vogais = ['a', 'e', 'i', 'o', 'u'];
    
    function proximaConsoante(letra) {
      if (letra === 'z') return 'b';
      let codigo = letra.charCodeAt(0);
      do {
        codigo++;
        if (codigo > 'z'.charCodeAt(0)) codigo = 'a'.charCodeAt(0);
      } while (vogais.includes(String.fromCharCode(codigo)));
      return String.fromCharCode(codigo);
    }
  
    return mensagem.split('').map(char => {
      if (/[a-z]/.test(char)) {
        return vogais.includes(char) ? char : proximaConsoante(char);
      }
      return char; 
    }).join('');
  }
  

  const mensagem = "hello world";
  console.log("🔓 Mensagem decifrada:", cifrarMensagemAlienigena(mensagem)); 

  