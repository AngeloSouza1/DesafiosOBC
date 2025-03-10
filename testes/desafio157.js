function encontrarSequencia(matriz) {
  const linhas = matriz.length;
  const colunas = matriz[0].length;

  const direcoes = [
    { dx: 0, dy: 1 },   
    { dx: 0, dy: -1 },  
    { dx: 1, dy: 0 },   
    { dx: -1, dy: 0 },  
    { dx: 1, dy: 1 },   
    { dx: -1, dy: -1 }, 
    { dx: 1, dy: -1 },  
    { dx: -1, dy: 1 }   
  ];

  for (let i = 0; i < linhas; i++) {
    for (let j = 0; j < colunas; j++) {
      for (let dir of direcoes) {
        let x = i;
        let y = j;
        const caminho = [[x, y]];

        while (
          x + dir.dx >= 0 &&
          x + dir.dx < linhas &&
          y + dir.dy >= 0 &&
          y + dir.dy < colunas &&
          matriz[x + dir.dx][y + dir.dy] === matriz[x][y] + 1
        ) {
          x += dir.dx;
          y += dir.dy;
          caminho.push([x, y]);
          if (caminho.length >= 3) {
            const [iniX, iniY] = caminho[0];
            const [fimX, fimY] = caminho[caminho.length - 1];
            return `(${iniX}, ${iniY}) -> (${fimX}, ${fimY})`;
          }
        }
      }
    }
  }

  return "Nenhuma sequência encontrada.";
}


const matriz = [
  [5, 4, 3, 11],
  [2, 6, 5, 3],
  [9, 7, 8, 5]
];

console.log("🔍 Resultado:", encontrarSequencia(matriz));
