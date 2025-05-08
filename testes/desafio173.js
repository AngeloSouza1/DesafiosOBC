function decifrarMelodia(notas) {
    let resultado = [];
    for (let i = 0; i < notas.length; i += 3) {
      const grupo = notas.slice(i, i + 3)
        .map(num => String.fromCharCode(64 + num)) 
        .join('');
      resultado.push(grupo);
    }
    return resultado.join(' ');
  }
  

  const entrada = [1, 2, 3, 1, 2, 3, 1];
  console.log("🎵 Melodia decifrada:");
  console.log(decifrarMelodia(entrada)); 
  