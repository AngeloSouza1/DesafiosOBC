# modulo.py

def calcular_forca_final(forca_inicial, pocao_vermelha, pocao_azul, pocao_verde, fases):
  
    # A força inicial do Pixel
    forca = forca_inicial

    # Cada poção vermelha dobra a força
    for _ in range(pocao_vermelha):
        forca *= 2

    # Cada poção azul aumenta a força em 3
    forca += pocao_azul * 3

    # Cada poção verde aumenta a força em 2 vezes o número da fase
    forca += pocao_verde * (2 * fases)

    return forca
