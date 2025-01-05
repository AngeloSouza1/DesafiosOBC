# main.py

from decoder import decode_message
from rich.console import Console
from rich.panel import Panel

def main():
    console = Console()

    # Mensagem inicial estilizada
    console.print(Panel("[bold blue]🪐 Bem-vindo ao Decodificador Espacial![/bold blue]", expand=False))
    console.print("[cyan]Prepare-se para decifrar as mensagens enigmáticas de Plutão![/cyan]\n")

    # Mensagens criptografadas de exemplo
    mensagens = [
        "xolrka#@",
        "mobpp jbbqfkd!",
        "dkluzg#@ynqf",
        "zrrg zl urneg zl sevraq"
    ]

    for i, mensagem in enumerate(mensagens, start=1):
        console.print(f"🚀 [bold yellow]Mensagem Encriptada {i}:[/bold yellow] [italic white]{mensagem}[/italic white]")
        mensagem_decifrada = decode_message(mensagem)
        console.print(f"✨ [bold green]Mensagem Decifrada:[/bold green] [italic cyan]{mensagem_decifrada}[/italic cyan]\n")
        console.print("--------------------------------------------------\n")

    # Mensagem de encerramento
    console.print("[bold blue]🌌 Decodificação concluída! Obrigado por ajudar a humanidade![/bold blue]")

if __name__ == "__main__":
    main()
