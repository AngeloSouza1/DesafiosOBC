def escape_room_solution(meme_strings):

    import logging

    # Configura o logger
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    # Palavras-chave relevantes para tendências de memes
    trends = {
        "Such": "S", "Much": "M", "Challenge": "C", 
        "All": "M", "Base": "B", "Belong": "B",
        "One": "A", "Does": "A", "Not": "A", 
        "Simply": "A", "Asking": "C", "Help": "C",
        "This": "T", "Is": "I", "Fine": "F",
        "Keep": "K", "Calm": "C", "Code": "C", "On": "O",
        "Why": "W", "To": "T", "Infinity": "I", "Beyond": "B",
        "Hakuna": "H", "Matata": "M"
    }

    magic_phrase = ""

    logging.info("Iniciando o processamento das frases.")
    for index, meme in enumerate(meme_strings, 1):
        logging.debug(f"Processando frase {index}: {meme}")

        # Limpa e quebra a string em palavras
        words = ''.join(char if char.isalnum() or char.isspace() else '' for char in meme).split()
        logging.debug(f"Palavras extraídas e limpas: {words}")
        
        # Captura apenas a primeira palavra relevante
        found_relevant = False
        for word in words:
            if word.capitalize() in trends:
                magic_phrase += trends[word.capitalize()]
                logging.debug(f"Palavra relevante encontrada: {word} -> {trends[word.capitalize()]}")
                found_relevant = True
                break  

        if not found_relevant:
            logging.debug(f"Nenhuma palavra relevante encontrada na frase {index}.")
            magic_phrase += "-"  # Adiciona um marcador para frases sem palavras relevantes

        logging.debug(f"Resultado parcial da frase mágica: {magic_phrase}")

    logging.info(f"Frase mágica final: {magic_phrase}")
    return magic_phrase
