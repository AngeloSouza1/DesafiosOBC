function preverAlinhamento(alinhamentos) {
    if (alinhamentos.length < 2) {
        throw new Error("A série deve ter pelo menos dois elementos para prever o próximo alinhamento.");
    }

    // Função para verificar se a diferença entre elementos é constante (padrão linear)
    function isLinear(arr) {
        const diff = arr[1] - arr[0];
        for (let i = 2; i < arr.length; i++) {
            if (arr[i] - arr[i - 1] !== diff) {
                return false;
            }
        }
        return diff;
    }

    // Função para verificar se a razão entre elementos é constante (padrão exponencial)
    function isExponential(arr) {
        const ratio = arr[1] / arr[0];
        for (let i = 2; i < arr.length; i++) {
            if (arr[i] / arr[i - 1] !== ratio) {
                return false;
            }
        }
        return ratio;
    }

    // Função para verificar se a diferença das diferenças é constante (padrão quadrático)
    function isQuadratic(arr) {
        let firstDiffs = [];
        for (let i = 1; i < arr.length; i++) {
            firstDiffs.push(arr[i] - arr[i - 1]);
        }

        let secondDiffs = [];
        for (let i = 1; i < firstDiffs.length; i++) {
            secondDiffs.push(firstDiffs[i] - firstDiffs[i - 1]);
        }

        const isConstant = secondDiffs.every(diff => diff === secondDiffs[0]);
        return isConstant ? secondDiffs[0] : false;
    }

    // Verifica se o padrão é linear
    const linearDiff = isLinear(alinhamentos);
    if (linearDiff !== false) {
        return alinhamentos[alinhamentos.length - 1] + linearDiff;
    }

    // Verifica se o padrão é exponencial
    const expRatio = isExponential(alinhamentos);
    if (expRatio !== false) {
        return alinhamentos[alinhamentos.length - 1] * expRatio;
    }

    // Verifica se o padrão é quadrático
    const quadDiff = isQuadratic(alinhamentos);
    if (quadDiff !== false) {
        const lastDiff = alinhamentos[alinhamentos.length - 1] - alinhamentos[alinhamentos.length - 2];
        return alinhamentos[alinhamentos.length - 1] + lastDiff + quadDiff;
    }

    throw new Error("Padrão não identificado. A série não corresponde a um padrão linear, exponencial ou quadrático.");
}

module.exports = { preverAlinhamento };
