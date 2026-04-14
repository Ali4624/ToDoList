import time as t

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import login as log
import registration as reg

console = Console()


def Menu():
    while True:
        table = Table(
            title="[bold magenta]Main Menu[/bold magenta]",
            border_style="cyan",
            show_header=False,
            box=None,
        )
        table.add_row("[bold yellow]1.[/bold yellow] Login")
        table.add_row("[bold yellow]2.[/bold yellow] Registration")
        table.add_row("[bold yellow]3.[/bold yellow] Exit")

        print(Panel.fit(table, border_style="blue"))

        choice = console.input("[bold green]Enter your choice:[/bold green] ")

        try:
            if int(choice) == 3:
                with console.status("[bold red]Exiting the system...", spinner="dots"):
                    t.sleep(2.1)
                print("[italic gray]67[/italic gray]")
                break

            elif int(choice) == 2:
                reg.register()

            elif int(choice) == 1:
                log.logging_in()
            else:
                print("[bold red]Invalid option![/bold red] Please select 1, 2, or 3.")

        except ValueError:
            print("\n[bold red]Error:[/bold red] Enter an integer value please!\n")
