import datetime as dt

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


def create_new(username, plan):
    with open(f"{username}.txt", "a") as files:
        console.print("\n[bold cyan]Date Entry[/bold cyan]")
        due_date = Prompt.ask("Enter the due date [grey70](Year-Month-Day)[/grey70]")

        creation_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        files.write(
            f"{plan}\t-\t{creation_time}\n========================\n"
            f"The due date is {due_date}\n---------------------------------\n"
        )

        console.print(
            f"\n[bold green]✔[/bold green] Task '[italic]{plan}[/italic]' saved successfully!\n"
        )


def main_menu(username):
    console.clear()
    console.print(
        Panel(
            f"Welcome to [bold magenta]ToDoList Manager[/bold magenta], [yellow]{username}[/yellow]!",
            style="bold white",
            border_style="magenta",
        )
    )

    while True:
        menu_table = Table(box=None, show_header=False)
        menu_table.add_row("[bold cyan]1.[/bold cyan] Create a new list")
        menu_table.add_row("[bold cyan]2.[/bold cyan] Mark list as completed")
        menu_table.add_row("[bold cyan]3.[/bold cyan] Remove the list")
        menu_table.add_row("[bold red]4.[/bold red] Log out")

        print(
            Panel.fit(
                menu_table,
                title="[bold white]Actions[/bold white]",
                border_style="blue",
            )
        )

        choice = Prompt.ask(
            "\n[bold white]Enter your choice[/bold white]", choices=["1", "2", "3", "4"]
        )

        try:
            if choice == "1":
                plan = Prompt.ask("\n[bold yellow]What are your plans?[/bold yellow]")
                create_new(username, plan)

            elif choice == "2":
                console.print("[italic yellow]coming soon...[/italic yellow]")

            elif choice == "3":
                console.print("[italic yellow]coming soon...[/italic yellow]")

            elif choice == "4":
                console.print("[bold red]Logging out...[/bold red]")
                break

        except Exception as e:
            console.print(f"[bold red]An error occurred:[/bold red] {e}")
