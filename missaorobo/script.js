function traduzirMensagem(codigo) {
    const sequencias = codigo.trim().split(' ');
    let mensagem = '';

    sequencias.forEach(seq => {
        const repeticoes = (seq.match(/beepboop/g) || []).length;
        if (repeticoes > 0) {
            mensagem += String.fromCharCode(96 + repeticoes); // 'a' = 1, 'b' = 2, ...
        }
    });

    return mensagem;
}

function traduzir() {
    const entrada = document.getElementById("entrada").value;
    const resultado = traduzirMensagem(entrada);
    document.getElementById("resultado").innerHTML = `
        <h2>Resultado:</h2>
        <p>${resultado}</p>
    `;
}
