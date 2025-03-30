def calcular_poder_total(comandos):
    poder_total = 1  
    poder_atual = 1

    fogo_consec = 0
    agua_count = 0
    terra_count = 0
    ar_consec = 0
    terra_valor = 1
    elemento_anterior = ""

    print(f"[START] poder_total = {poder_total}, poder_atual = {poder_atual}")

    for i, comando in enumerate(comandos):
        print(f"\n[{i}] Comando: {comando}")

        if comando == "Fogo":
            if elemento_anterior == "Fogo":
                fogo_consec += 1
            else:
                fogo_consec = 1

            if fogo_consec > 3:
                print("🔥 Explosão! Resetando poder_atual.")
                poder_atual = 1
                fogo_consec = 1

            poder_atual *= 2
            poder_total += poder_atual
            print(f"🔥 Fogo ativado: poder_atual = {poder_atual}, poder_total = {poder_total}")
            elemento_anterior = "Fogo"

        elif comando == "Água":
            agua_count += 1
            poder_total += poder_atual
            print(f"💧 Água ativada: poder_atual = {poder_atual}, poder_total = {poder_total}")

            if agua_count % 3 == 0:
                poder_atual *= 3
                print(f"💧 Água x3! Novo poder_atual = {poder_atual}")

            elemento_anterior = "Água"
            fogo_consec = 0
            ar_consec = 0

        elif comando == "Terra":
            terra_count += 1
            poder_total += terra_valor
            print(f"🌱 Terra ativada: terra_valor = {terra_valor}, poder_total = {poder_total}")

            if terra_count % 5 == 0:
                terra_valor *= 2
                print(f"🌱 Terra DOBROU! Novo terra_valor = {terra_valor}")

            elemento_anterior = "Terra"
            fogo_consec = 0
            ar_consec = 0

        elif comando == "Ar":
            if elemento_anterior == "Ar":
                ar_consec += 1
            else:
                ar_consec = 1

            if ar_consec == 4:
                redemoinho = poder_atual ** 2
                poder_total += redemoinho
                print(f"🌀 Redemoinho! Somando {redemoinho}, poder_total = {poder_total}")
                ar_consec = 0
            else:
                poder_total += poder_atual
                print(f"🌀 Ar ativado: poder_atual = {poder_atual}, poder_total = {poder_total}")

            elemento_anterior = "Ar"
            fogo_consec = 0

    print(f"\n[END] poder_total = {poder_total}")
    return poder_total


entrada = ["Fogo", "Fogo", "Água", "Terra", "Fogo", "Água", "Água", "Ar", "Ar", "Ar", "Ar", "Terra"]
calcular_poder_total(entrada)
