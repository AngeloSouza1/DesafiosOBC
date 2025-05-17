(async () => {
  const chalk = (await import('chalk')).default;
  const Table = (await import('cli-table3')).default;

  function ehPrimo(n) {
    if (n <= 1) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) return false;
    }
    return true;
  }

  function menorEnergiaPrimo(n, portais, start, end) {
    const grafo = Array.from({ length: n + 1 }, () => []);
    for (const [origem, destino, custo] of portais) {
      grafo[origem].push({ destino, custo });
    }

    console.log(chalk.bold.bgMagenta.white(`\n🔭 DESAFIO #179: A TRAVESSIA INTERPLANETÁRIA DE ALGOR`));
    console.log(chalk.gray('='.repeat(60)));

    const grafoTable = new Table({
      head: ['Planeta Origem', 'Destino', 'Custo'],
      colWidths: [18, 10, 10]
    });
    portais.forEach(([origem, destino, custo]) => grafoTable.push([origem, destino, custo]));
    console.log(chalk.cyan.bold('\n🌌 Portais Espaciais Disponíveis:'));
    console.log(grafoTable.toString());

    const dist = Array(n + 1).fill(Infinity);
    const visitado = Array(n + 1).fill(false);
    dist[start] = 0;

    const fila = [{ planeta: start, custo: 0 }];

    const logTable = new Table({
      head: ['Planeta Atual', 'Ação', 'Destino', 'Novo Custo'],
      colWidths: [18, 15, 10, 14]
    });

    while (fila.length) {
      fila.sort((a, b) => a.custo - b.custo);
      const { planeta, custo } = fila.shift();

      if (visitado[planeta]) continue;
      visitado[planeta] = true;

      grafo[planeta].forEach(({ destino, custo: c }) => {
        const novoCusto = custo + c;
        if (novoCusto < dist[destino]) {
          dist[destino] = novoCusto;
          fila.push({ planeta: destino, custo: novoCusto });
          logTable.push([planeta, 'Atualizado', destino, novoCusto]);
        }
      });
    }

    console.log(chalk.yellow.bold('\n🛰️ Jornada Registrada:'));
    console.log(logTable.toString());

    const custoFinal = dist[end];
    console.log(chalk.gray('\n' + '='.repeat(60)));
    console.log(chalk.magenta.bold(`🏁 Chegada ao planeta ${end}`));
    console.log(chalk.magenta(`🔋 Energia mínima necessária: ${custoFinal}`));

    if (ehPrimo(custoFinal)) {
      console.log(chalk.greenBright.bold(`✅ ${custoFinal} é um número primo. Viagem válida!`));
    } else {
      console.log(chalk.redBright.bold(`❌ ${custoFinal} não é primo. A viagem não atende aos critérios.`));
    }
    console.log(chalk.gray('='.repeat(60)));
  }


  const numeroPlanetas = 5;
  const portais = [
    [1, 2, 10],
    [2, 3, 15],
    [3, 4, 5],
    [4, 5, 3],
    [1, 5, 40]
  ];
  const planetaInicio = 1;
  const planetaFim = 5;

  menorEnergiaPrimo(numeroPlanetas, portais, planetaInicio, planetaFim);
})();
