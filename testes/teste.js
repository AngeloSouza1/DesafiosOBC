const alphabet = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
    e: 5,
    f: 6,
    g: 7,
    h: 8,
    i: 9,
    j: 10,
    k: 11,
    l: 12,
    m: 13,
    n: 14,
    o: 15,
    p: 16,
    q: 17,
    r: 18,
    s: 19,
    t: 20,
    u: 21,
    v: 22,
    w: 23,
    x: 24,
    y: 25,
    z: 26,
  };
  
  // Remove acentos, letras especiais, espaços e converte as palavras em arrays de números
  function letterToNumber(arr) {
    const numberArr = [];
    arr.forEach((word) => {
      const currWord = word
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .split("")
        .map((letter) => alphabet[letter]);
      numberArr.push(currWord);
    });
    return numberArr;
  }
  
  // Troca os números que ultrapassam 26 pelos correspondentes e transforma a array de números em uma string
  function convertToString(arr) {
    const newArr = arr.map((num) => (num > 26 ? num - 26 : num));
    return newArr
      .map(
        (num) =>
          (num = Object.keys(alphabet).find((letter) => alphabet[letter] === num))
      )
      .join("");
  }
  
  // Função original baseada em soma de letras
  function magicWord(arr) {
    const numArr = letterToNumber(arr);
    const sumArr = [];
    const maxLength = Math.max(...numArr.map((array) => array.length));
  
    for (let i = 0; i < maxLength; i++) {
      let sum = 0;
      for (let j = 0; j < numArr.length; j++) {
        sum += numArr[j][i] || 0;
      }
      sumArr.push(sum);
    }
  
    console.log("Soma das posições:", sumArr);
    return convertToString(sumArr);
  }
  
  // NOVA FUNÇÃO com a lógica correta do desafio
  function palavraDoPoder(palavras) {
    const palavrasLimpas = palavras.map(p =>
      p.normalize("NFD")
       .replace(/[\u0300-\u036f]/g, "")
       .toLowerCase()
       .replace(/[^a-z]/g, "")
    );
  
    const primeirasLetras = palavrasLimpas.map(p => p[0]);
    const ultimasLetras = palavrasLimpas.slice().reverse().map(p => p.at(-1));
  
    return [...primeirasLetras, ...ultimasLetras].join('');
  }
  
  // Teste com as palavras mágicas
  let palavrasMagicas = ["magia", "dragão", "elfo"];

  
  console.log("🔮 Palavra com soma (magicWord):", magicWord(palavrasMagicas)); // venebo
  console.log("🔑 Palavra do Poder correta:", palavraDoPoder(palavrasMagicas)); // mdeooa
  