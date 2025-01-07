from monstros import crie_monstros
from rich.console import Console
from rich.table import Table

def main():
    console = Console()

    # Exemplo de dados
    dados = [
        {"nome": "Dragão da Sombra 🐉", "ataque": 150, "defesa": 80, "magia": 200},
        {"nome": "Goblin Intrigante 🧝‍♂️", "ataque": 70, "defesa": 50, "magia": 20},
        {"nome": "Gigante das Montanhas 🗻", "ataque": 120, "defesa": 200, "magia": 50},
        {"nome": "Elfo Misterioso 🧙‍♂️", "ataque": 90, "defesa": 60, "magia": 120}
    ]

    # Chama a função crie_monstros
    monstros_fortes = crie_monstros(dados)

    # Exibe os resultados com cores e emojis
    if monstros_fortes:
        console.print("[bold magenta]Monstros acima da média de poder total:[/bold magenta]\n")

        # Cria uma tabela para exibir os monstros
        table = Table(title="Monstros Fortes 💪", style="bold green")
        table.add_column("Nome", style="bold cyan")
        table.add_column("Ataque", style="red")
        table.add_column("Defesa", style="blue")
        table.add_column("Magia", style="purple")
        table.add_column("Poder Total", style="gold1")

        # Adiciona os dados dos monstros à tabela
        for monstro in monstros_fortes:
            poder_total = monstro["ataque"] + monstro["defesa"] + monstro["magia"]
            table.add_row(
                monstro["nome"],
                str(monstro["ataque"]),
                str(monstro["defesa"]),
                str(monstro["magia"]),
                f"[bold]{poder_total}[/bold]"
            )

        # Exibe a tabela
        console.print(table)
    else:
        console.print("[bold red]Nenhum monstro está acima da média de poder total! 😢[/bold red]")

if __name__ == "__main__":
    main()
