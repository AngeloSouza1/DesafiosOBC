from emoji_converter import converter_para_emoji

def main():
    print("Bem-vindo ao Musical Mix de Emoji 🎵🎸")
    print("Digite o nome de uma banda para convertê-lo em emojis mágicos!\n")

    while True:
        # Entrada do usuário
        nome_banda = input("Digite o nome da banda (ou 'sair' para encerrar): ").strip()

        if nome_banda.lower() == "sair":
            print("Obrigado por usar o Musical Mix de Emoji! 🎶")
            break

        if not nome_banda:
            print("Por favor, insira um nome válido!")
            continue

        # Converte o nome para emojis
        emoji_mix = converter_para_emoji(nome_banda)

        # Exibe o resultado
        print(f"Emoji Mix: {emoji_mix}\n")

# Executa o programa principal
if __name__ == "__main__":
    main()
