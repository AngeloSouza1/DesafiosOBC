function reordenarFragmentos(fragmentos) {
  const ordemEsperada = ["iniciar", "autenticar", "conectar", "destruir"];

  return fragmentos
    .sort((a, b) => {
      const indexA = ordemEsperada.findIndex(palavra => a.includes(palavra));
      const indexB = ordemEsperada.findIndex(palavra => b.includes(palavra));
      return indexA - indexB;
    })
    .map(frag => frag.endsWith(';') ? frag : frag + ';') // garante ponto e vírgula
    .join(' ');
}

const entrada = ["iniciar()", "conectar();", "destruir();", "autenticar();"];
const resultado = reordenarFragmentos(entrada);

console.log("⚔️ Código Reordenado:");
console.log(resultado);


