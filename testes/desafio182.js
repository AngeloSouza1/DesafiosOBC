function decifrarMensagem(codigos) {
  return codigos
    .map(code => String.fromCharCode(code))
    .reverse()
    .join('');
}

console.log(decifrarMensagem([111, 108, 108, 101, 72])); 
console.log(decifrarMensagem([100, 108, 114, 111, 87])); 
