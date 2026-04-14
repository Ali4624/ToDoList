import datetime as dt
def create_new(username,plan):
    status = "Created"
    with open(f"{username}.txt", 'a') as files:
        due_date = input("\nEnter the data in Year-Month-Day format...\nEnter the due date of this task:")
        creation_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        files.write(f"{plan}\t-\t{creation_time}\n========================\nThe due date is {due_date}\n---------------------------------\nStatus:{status}")
def main_menu(username): 
    __username = username
    print("\n----------Welcome to ToDoList Manager!----------\n")
    choice = None
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
