// modulo_previsao.mjs

/**
 * Função para prever o próximo número em uma série temporal.
 * Pode identificar padrões lineares, exponenciais ou quadráticos.
 *
 * @param {number[]} alinhamentos - Um array de números inteiros representando a série temporal.
 * @returns {number} - O próximo número previsto da série.
 * @throws {Error} - Se nenhum padrão conhecido for identificado.
 */
export function preverAlinhamento(alinhamentos) {
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

    // Tenta identificar um padrão linear
    const linearDiff = isLinear(alinhamentos);
    if (linearDiff !== false) {
        return alinhamentos[alinhamentos.length - 1] + linearDiff;
    }

    // Tenta identificar um padrão exponencial
    const expRatio = isExponential(alinhamentos);
    if (expRatio !== false) {
        return alinhamentos[alinhamentos.length - 1] * expRatio;
    }

    // Tenta identificar um padrão quadrático
    const quadDiff = isQuadratic(alinhamentos);
    if (quadDiff !== false) {
        const lastDiff = alinhamentos[alinhamentos.length - 1] - alinhamentos[alinhamentos.length - 2];
        return alinhamentos[alinhamentos.length - 1] + lastDiff + quadDiff;
    }

    throw new Error("Padrão não identificado. A série não corresponde a um padrão linear, exponencial ou quadrático.");
}
