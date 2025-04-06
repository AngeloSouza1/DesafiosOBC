function detectorDeSabores(salgadinhos) {
    // Usamos Set para remover duplicatas e depois ordenamos com sort
    const saboresUnicos = [...new Set(salgadinhos)].sort((a, b) => a - b);
    return saboresUnicos;
  }
  
  // Exemplo de uso:
  const coleta = [8, 3, 4, 8, 2, 3, 4, 10, 10];
  const resultado = detectorDeSabores(coleta);
  
  console.log("🛸 Tipos de salgadinhos coletados (sem repetições):", resultado);
  