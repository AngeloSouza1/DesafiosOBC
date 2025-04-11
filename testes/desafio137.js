function geolocatorR2D2Z(coordenadasIniciais, instrucoes) {
    let [x, y] = coordenadasIniciais;
  
    for (const direcao of instrucoes) {
      switch (direcao.toLowerCase()) {
        case "norte":
          y -= 1;
          break;
        case "sul":
          y += 1;
          break;
        case "leste":
          x += 1;
          break;
        case "oeste":
          x -= 1;
          break;
        default:
          console.warn(`🚫 Direção inválida ignorada: "${direcao}"`);
      }
    }
  
    return [x, y];
  }
  
  // 🧪 Exemplo de uso:
  const coordenadasIniciais = [3, 3];
  const instrucoes = ["norte", "oeste", "sul", "leste", "norte"];
  
  const resultadoFinal = geolocatorR2D2Z(coordenadasIniciais, instrucoes);
  
  // 🖨️ Saída final formatada igual ao desafio:
  console.log("\n" + JSON.stringify(resultadoFinal));
  