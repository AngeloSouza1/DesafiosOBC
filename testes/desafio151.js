function descobrirMensagemOriginal(texto) {
  const tamanho = texto.length;

  for (let i = 1; i <= tamanho / 2; i++) {
    const fragmento = texto.slice(0, i);
    const repetido = fragmento.repeat(tamanho / i);
    
    if (repetido === texto) {
      return fragmento;
    }
  }

  return texto; 



console.log(descobrirMensagemOriginal('memecliquesmemecliquesmemecliques')); // ➜ 'memecliques'
console.log(descobrirMensagemOriginal('bananabanana'));                       // ➜ 'banana'
console.log(descobrirMensagemOriginal('looplooplooploop'));                   // ➜ 'loop'
