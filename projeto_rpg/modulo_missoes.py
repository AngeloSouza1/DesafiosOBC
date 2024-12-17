import random

# Listas com opções de objetivos, locais e vilões
objetivos = [
    "Recuperar um artefato perdido",
    "Salvar um refém",
    "Explorar uma região inóspita",
    "Proteger uma aldeia"
]

locais = [
    "Floresta Encantada",
    "Montanhas Geladas",
    "Caverna do Dragão",
    "Cidade Submersa"
]

viloes = [
    "Feiticeiro das Sombras",
    "Dragão Ancião",
    "Rei Elfo Corrompido",
    "Pirata Fantasmagórico"
]

# Função para gerar uma missão aleatória
def gerar_missao():
 
    objetivo = random.choice(objetivos)
    local = random.choice(locais)
    vilao = random.choice(viloes)

    return {
        "objetivo": objetivo,
        "local": local,
        "vilao": vilao
    }
