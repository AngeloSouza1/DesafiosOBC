# main.py
from modulo_missoes import gerar_missao

def main():
    print("🌟 Bem-vindo ao Gerador de Missões de RPG! 🌟\n")
    missao = gerar_missao()

    print("🌟 Sua Missão Épica 🌟")
    print("----------------------")
    print(f"🎯 Objetivo: {missao['objetivo']}")
    print(f"🗺️ Local: {missao['local']}")
    print(f"⚔️ Vilão: {missao['vilao']}")
    print("----------------------")
    print("Prepare-se para a aventura! 🧙‍♂️🧝‍♀️")

if __name__ == "__main__":
    main()
