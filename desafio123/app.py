import re

def analisar_planeta(lista_strings):
    soma_total = 0
    for s in lista_strings:
        numeros = re.findall(r'\d+', s)  # encontra todos os números na string
        soma_numeros = sum(map(int, numeros))  # converte e soma
        print(f"↪️ Números encontrados em '{s}': {numeros} → Soma parcial: {soma_numeros}")
        soma_total += soma_numeros

    print(f"\n🧮 Soma total dos números: {soma_total}")
    if soma_total % 12 == 0:
        print("🌍 Planeta Habitável")
        return "Planeta Habitável"
    else:
        print("☄️ Planeta Inóspito")
        return "Planeta Inóspito"

entrada = ["a3b4c2", "x0y1z2", "ab3cd4ef5"]
analisar_planeta(entrada)
