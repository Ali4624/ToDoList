import json

from rich import print
from rich.console import Console
from rich.panel import Panel

import manager

console = Console()
username = None
password = None


def Checker(username):
    global password
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(
            Panel(
                "[bold red]Internal error![/bold red]\nPlease try again later.",
                title="Error",
                border_style="red",
            )
        )
        return

    if username in data.keys():
        password = console.input("\n[bold cyan]Enter your password:[/bold cyan] ")

        if data[username] == password:
            print(f"\n[bold green] Hello, {username}![/bold green]")
            manager.main_menu(username)
        else:
            print(
                "[bold red]Wrong username or password![/bold red]\nPlease try again..."
            )
    else:
        print("\n[bold yellow]Username not found![/bold yellow]\nPlease try again...\n")


def logging_in():
    global username
    print(
        Panel.fit("[bold magenta]ToDoList Login[/bold magenta]", border_style="magenta")
    )
    username = console.input("[bold blue]Enter your username:[/bold blue] ")
    Checker(username)
