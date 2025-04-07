function processActions(actions, initialValue) {
    let current = initialValue;
  
    console.log("🧠 Iniciando com valor:", current);
  
  
    const sortedActions = [...actions].sort((a, b) => a.id - b.id);
  
  
    const operations = {
      add: (val) => {
        console.log(`➕ Somando ${val} ao ${current}`);
        current += val;
      },
      multiply: (val) => {
        console.log(`✖️ Multiplicando ${current} por ${val}`);
        current *= val;
      },
      subtract: (val) => {
        console.log(`➖ Subtraindo ${val} de ${current}`);
        current -= val;
      },
      reset: () => {
        console.log(`🔄 Resetando valor para ${initialValue}`);
        current = initialValue;
      }
    };
  
  
    for (const { type, value } of sortedActions) {
      const handler = operations[type];
      if (handler) {
        handler(value);
        console.log(`📍 Valor atual: ${current}\n`);
      } else {
        console.warn(`⚠️ Ação desconhecida: ${type}`);
      }
    }
  
    console.log("✅ Resultado final:", current);
    return current;
  }
  
  
  const actions = [
    { id: 1, type: 'add', value: 10 },
    { id: 2, type: 'multiply', value: 2 },
    { id: 3, type: 'subtract', value: 5 },
    { id: 4, type: 'reset', value: 0 },
    { id: 5, type: 'add', value: 3 }
  ];
  
  processActions(actions, 5);
  function hackearTempo(palavrasCodificadas) {
    let somaAnos = 0;
  
    console.log("🕰️ Iniciando decodificação dos eventos históricos...\n");
  
    for (const palavra of palavrasCodificadas) {
      const match = palavra.match(/\d+/); // Extrai o número (ano) da string
  
      if (match) {
        const ano = parseInt(match[0]);
        console.log(`🔍 Evento: "${palavra}" ➡️ Ano detectado: ${ano}`);
        somaAnos += ano;
      } else {
        console.log(`⚠️ Nenhum número encontrado na palavra: "${palavra}"`);
      }
    }
  
    console.log(`\n🧠 Ano final decodificado: ${somaAnos}`);
    return somaAnos;
  }
  
  
  const eventosHistoricos = [
    "Guerra1939Mundial",
    "Moon1969Landing",
    "Wall1989Fall",
    "Twin2001Towers"
  ];
  
  hackearTempo(eventosHistoricos); 
  