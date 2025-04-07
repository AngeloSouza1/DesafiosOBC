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

// 🧪 Teste com o exemplo do desafio
const eventosHistoricos = [
  "Guerra1939Mundial",
  "Moon1969Landing",
  "Wall1989Fall",
  "Twin2001Towers"
];

hackearTempo(eventosHistoricos); // Esperado: 7898
