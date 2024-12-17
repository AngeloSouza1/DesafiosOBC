from modulo_decode import decodificar_mensagem

def main():
    print("🚀 Bem-vindo ao Decodificador de Mensagens Espaciais! 🌌")
    mensagem_codificada = input("\nDigite a mensagem codificada: ")
    mensagem_decodificada = decodificar_mensagem(mensagem_codificada)
    print(f"\n🔓 Mensagem decodificada: {mensagem_decodificada}")

if __name__ == "__main__":
    main()
