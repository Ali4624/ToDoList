import json
import os

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

import manager

console = Console()
username = None
password = None


def validator(prompt, is_password=False):
    while True:
        data = Prompt.ask(prompt, password=is_password)

        if len(data) >= 8 and any(char.isdigit() for char in data):
            return data
        else:
            print(
                Panel(
                    "[bold red]Validation Failed[/bold red]\n"
                    "Requirements: [yellow]At least 8 characters[/yellow] & [yellow]1 digit[/yellow].",
                    border_style="red",
                )
            )


def save_user(file, username, password):
    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    data[username] = password

    with open(file, "w") as Ow:
        json.dump(data, Ow, indent=4)


def register():
    global username, password

    console.clear()
    print(
        Panel.fit(
            "[bold green]Create New Account[/bold green]",
            subtitle="Security Requirements: 8+ chars & 1 digit",
            border_style="green",
        )
    )

    username = validator("[bold blue]Choose Username[/bold blue]")

    if os.path.exists("users.json"):
        with open("users.json", "r") as ch:
            try:
                if username in json.load(ch).keys():
                    print(
                        "\n[bold red]Username already exists[/bold red] Please try another one\n"
                    )
                    return
            except json.JSONDecodeError:
                pass

    password = validator("[bold blue]Choose Password[/bold blue]", is_password=True)

    save_user("users.json", username, password)

    print(f"\n[bold green]Welcome{username}[/bold green] Account created successfully")
    manager.main_menu(username)
