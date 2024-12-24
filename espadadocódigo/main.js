// Dicionário de Código Morse
const morseCode = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',
    'e': '.',     'f': '..-.',  'g': '--.',   'h': '....',
    'i': '..',    'j': '.---',  'k': '-.-',   'l': '.-..',
    'm': '--',    'n': '-.',    'o': '---',   'p': '.--.',
    'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',
    'y': '-.--',  'z': '--..',  ' ': '/'
  };
  
  // Função para converter texto em Código Morse
  function converterParaMorse(frase) {
    const fraseLimpa = frase.toLowerCase().replace(/[^a-z\s]/g, ''); // Remove caracteres inválidos
    const morse = [...fraseLimpa]
      .map(char => morseCode[char] || '') // Converte cada caractere para Morse
      .join(' '); // Junta os códigos com espaço entre letras
    return morse.trim();
  }
  
  // Botão "Converter para Morse"
  document.getElementById('convertButton').addEventListener('click', () => {
    const inputText = document.getElementById('inputText').value; // Obtém o valor do input
    const outputMorse = converterParaMorse(inputText); // Converte para Morse
    const outputMorseElement = document.getElementById('outputMorse');
    
    if (outputMorse) {
      outputMorseElement.textContent = outputMorse; // Exibe o resultado
      document.getElementById('resetButton').style.display = 'inline-block'; // Mostra o botão "Reiniciar"
    } else {
      outputMorseElement.textContent = 'Por favor, insira um texto válido.'; // Mensagem de erro
    }
  });
  
  // Botão "Reiniciar"
  document.getElementById('resetButton').addEventListener('click', () => {
    document.getElementById('inputText').value = ''; // Limpa o campo de texto
    document.getElementById('outputMorse').textContent = ''; // Limpa o resultado exibido
    document.getElementById('resetButton').style.display = 'none'; // Esconde o botão "Reiniciar"
  });
  