const readline = require('readline');

/**
 * Limpa a tela do terminal.
 */
function limparTela() {
    console.clear();
}

/**
 * Função para encontrar o menor valor de n tal que a soma dos quadrados
 * consecutivos de 1 a n seja igual ao Número Mágico.
 * Mostra os passos detalhados no processo.
 * 
 * @param {number} S - Número Mágico a ser encontrado.
 * @returns {number} - O menor valor de n ou -1 se não existir.
 */
function encontrarNumeroMagico(S) {
    let soma = 0;
    let n = 0;
    const passos = [];

    while (soma < S) {
        n++;
        soma += n * n;
        passos.push(`n = ${n}, soma = ${soma}`);
    }

    return { resultado: soma === S ? n : -1, passos };
}

/**
 * Exibe o menu principal e lida com a interação do usuário.
 */
function exibirMenu() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const mostrarMenu = () => {
        limparTela();
        console.log('🟢 Bem-vindo ao Reino Matemático! 🟢');
        console.log('-----------------------------------');
        console.log('1️⃣  Calcular o Número Mágico');
        console.log('2️⃣  Explicação do Número Mágico');
        console.log('3️⃣  Sair');
        console.log('-----------------------------------');
    };

    const aguardarEnterParaMenu = () => {
        rl.question('\nPressione Enter para voltar ao menu...', () => {
            mostrarMenu();
            rl.question('Digite sua escolha: ', tratarEscolha);
        });
    };

    const tratarEscolha = (opcao) => {
        switch (opcao.trim()) {
            case '1':
                rl.question('\nDigite o Número Mágico desejado: ', (input) => {
                    const numeroMagico = parseInt(input);

                    if (isNaN(numeroMagico) || numeroMagico <= 0) {
                        console.log('\n❌ Por favor, insira um número inteiro positivo válido.');
                        aguardarEnterParaMenu();
                    } else {
                        const { resultado, passos } = encontrarNumeroMagico(numeroMagico);

                        limparTela();
                        console.log(`🔍 Buscando o menor "n" para o Número Mágico ${numeroMagico}...`);
                        console.log('-----------------------------------');
                        passos.forEach((passo) => console.log(passo));
                        console.log('-----------------------------------');
                        if (resultado !== -1) {
                            console.log(`✅ Resultado: O menor valor de "n" é ${resultado}!`);
                        } else {
                            console.log(`🚨 Não existe um "n" que satisfaça o Número Mágico ${numeroMagico}.`);
                        }
                        aguardarEnterParaMenu();
                    }
                });
                break;

            case '2':
                limparTela();
                console.log('\n🔮 O que é um Número Mágico?');
                console.log('-----------------------------------');
                console.log('Um Número Mágico é obtido somando os quadrados consecutivos a partir de 1.');
                console.log('Por exemplo:');
                console.log('1² + 2² + 3² + 4² = 30. Portanto, 30 é um Número Mágico.');
                console.log('O desafio é encontrar o menor "n" tal que a soma dos quadrados seja igual ao Número Mágico.');
                console.log('-----------------------------------');
                aguardarEnterParaMenu();
                break;

            case '3':
                limparTela();
                console.log('👋 Adeus! Volte sempre ao Reino Matemático!');
                rl.close();
                break;

            default:
                console.log('\n❌ Opção inválida. Tente novamente.');
                aguardarEnterParaMenu();
        }
    };

    mostrarMenu();
    rl.question('Digite sua escolha: ', tratarEscolha);
}

// Iniciar o programa
exibirMenu();
