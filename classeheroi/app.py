class Heroi:
    def __init__(self, nome, poder, nivel_forca):
        self.nome = nome
        self.poder = poder
        self.nivel_forca = nivel_forca

    def acao(self):
        return f"{self.nome} usa sua habilidade de {self.poder} com força de {self.nivel_forca}!"
        
# Teste com exemplo fornecido
heroi = Heroi("Super Dev", "Codificação", 9001)
print(heroi.acao())

# Criando mais heróis
heroi2 = Heroi("Mestre dos Bugs", "Encontrar e corrigir bugs", 8500)
heroi3 = Heroi("Guardião do Design", "Criar interfaces incríveis", 7000)

# Exibindo as ações
print(heroi2.acao())
print(heroi3.acao())
