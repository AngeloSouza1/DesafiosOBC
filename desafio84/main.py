import random

def gerador_de_memes(linguagem, aspecto):
    templates = [
        f"🖥️💡 Quando você programa em **{linguagem}**, {aspecto} é praticamente um ritual! 🤓",
        f"😂 Quem programa em **{linguagem}** sabe que {aspecto} faz parte do dia a dia! 🎢",
        f"🔥 Se você usa **{linguagem}**, já aceitou que {aspecto} é inevitável... 💀",
        f"🔍 Debugar em **{linguagem}** sem {aspecto}? **MITO!** 🚨",
        f"🛠️ Programar em **{linguagem}** sem {aspecto} é como café sem cafeína: **simplesmente não existe!** ☕💻",
        f"📜 No grande livro da programação, está escrito: **'{aspecto}' faz parte da experiência de codar em {linguagem}!**",
        f"🚀 Todo dev de **{linguagem}** já enfrentou **{aspecto}** pelo menos uma vez na vida! 🎯",
        f"⚡ Codar em **{linguagem}** sem {aspecto} é um universo paralelo que ninguém descobriu ainda! 🛸",
        f"💾 *'Ctrl + Z'* não pode te salvar de {aspecto} enquanto usa **{linguagem}**! 😵",
        f"🧙‍♂️ Quem programa em **{linguagem}** aprende a lidar com {aspecto} como um verdadeiro **mago do código**! 🪄"
    ]

    meme = random.choice(templates)
    return f"\n🎭 **Meme do Dia:**\n{meme}\n"

# 🔥 **Testes**
print(gerador_de_memes('Python', 'debugging o café da manhã'))
print(gerador_de_memes('JavaScript', 'descobrir que o código só funciona no console'))
print(gerador_de_memes('C++', 'lutar contra erros de memória'))
print(gerador_de_memes('Java', 'esperar a JVM carregar'))
print(gerador_de_memes('Ruby', 'achar um erro e perceber que é só um espaço a mais'))
