def ativar_hyperdrive(dia):
    # Dicionário associando cada dia ao módulo correto
    modulos = {
        "segunda-feira": "Módulo de Propulsão",
        "terça-feira": "Módulo de Navegação",
        "quarta-feira": "Módulo de Comunicações",
        "quinta-feira": "Módulo de Defesa",
        "sexta-feira": "Módulo de Pesquisa",
        "sábado": "Módulo de Lazer",
        "domingo": "Módulo de Manutenção"
    }

    # Padroniza a entrada para minúsculas e remove espaços extras
    dia = dia.lower().strip()

    # Verifica se o dia é válido
    if dia in modulos:
        print("\n🚀 **Ativação do Hyperdrive Iniciada!** 🌌")
        print(f"📅 Dia da semana: {dia.capitalize()}")
        print(f"🛠️ Módulo ativado: {modulos[dia]}")
        print("✅ **Hyperdrive pronto para o salto no hiperespaço!**\n")
        return modulos[dia]
    else:
        print("\n⚠️ **Erro! Dia inválido informado.**")
        print("🔍 Certifique-se de digitar corretamente o dia da semana!\n")
        return "Dia inválido"

# 🔥 Testes
ativar_hyperdrive("quarta-feira")
ativar_hyperdrive("domingo")
ativar_hyperdrive("Segunda-feira")
ativar_hyperdrive("terça-feira")
ativar_hyperdrive("Feriado")  # Teste de erro
