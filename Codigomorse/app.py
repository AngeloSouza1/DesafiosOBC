MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}

def decifrar_cancao_perdida(mensagem_morse):
    try:
        palavras_morse = mensagem_morse.strip().split(' / ')
        
        mensagem_decifrada = []
        
        for palavra in palavras_morse:
            caracteres_morse = [morse for morse in palavra.split(' ') if morse]
            
    
            letras = [MORSE_CODE[morse] for morse in caracteres_morse]
            
   
            mensagem_decifrada.append(''.join(letras[::-1]))
     
        mensagem_final = ' '.join(mensagem_decifrada)
        
  
        return (
            "\n" + "=" * 40 +
            "\n🚀 Decifrando a Canção Perdida 🚀\n" +
            "=" * 40 +
            f"\nMensagem em código Morse: \"{mensagem_morse.strip()}\"\n" +
            "-" * 40 +
            f"\nMensagem decifrada: \"{mensagem_final}\"" +
            "\n" + "=" * 40
        )
    
    except KeyError as e:
        return (
            "\n" + "=" * 40 +
            "\n⚠️  Erro ao decifrar mensagem ⚠️\n" +
            "=" * 40 +
            f"\nCaractere Morse inválido encontrado: \"{e}\"" +
            "\nVerifique se todos os caracteres Morse estão corretos." +
            "\n" + "=" * 40
        )

# Teste com o exemplo fornecido
mensagem_morse = "...- .-. --- .-. / .-- ...-"

mensagem_decifrada = decifrar_cancao_perdida(mensagem_morse)
print(mensagem_decifrada)  # Saída estilizada
