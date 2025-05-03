const gerarSequencia = () => {
  const resultado = [];
  for (let n = 1; n < 500; n = n * 2 + 1) {
    resultado.push(n);
  }
  return resultado;
};

console.log(gerarSequencia());

