from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import os
import subprocess

console = Console()

def run_program(filename, name=""):
    console.print(f"\n[bold blue]🚀 Launching {filename}...[/bold blue]")
    console.print("[dim]Press Ctrl+C if you want to return to menu early[/dim]\n")
    try:
        subprocess.run(["python3", filename])
    except KeyboardInterrupt:
        console.print("\n[yellow]Returned to main menu.[/yellow]")
    except:
        console.print("[red]Failed to launch the program.[/red]")

console.print(Panel.fit("[bold cyan]🚀 Acode Mini Apps Hub[/bold cyan]", border_style="blue"))

name = Prompt.ask("[bold green]What is your name?[/bold green]")

console.print(f"\n[bold magenta]Hello, {name}! 👋[/bold magenta]")
console.print("[bold]You're now a real mobile developer on Android![/bold]\n")

while True:
    console.print("[yellow]What would you like to do today?[/yellow]")

    table = Table(title="Available Mini Apps")
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Program", style="green")

    table.add_row("1", "Enhanced Calculator")
    table.add_row("2", "Number Guessing Game")
    table.add_row("3", "To-Do List")
    table.add_row("4", "Show current time")
    table.add_row("5", "Exit")

    console.print(table)

    choice = Prompt.ask("[bold]Enter your choice (1-5)[/bold]", choices=["1","2","3","4","5"])

    if choice == "1":
        run_program("calculator.py", name)
    elif choice == "2":
        run_program("guess.py", name)
    elif choice == "3":
        run_program("todo.py", name)
    elif choice == "4":
        from datetime import datetime
        now = datetime.now()
        console.print(f"\n[bold cyan]Current time:[/bold cyan] {now.strftime('%Y-%m-%d %H:%M:%S')}")
    elif choice == "5":
        console.print(f"[bold red]Goodbye, {name}! Keep coding and building 💪[/bold red]")
        break

    input("\nPress Enter to return to main menu...")
    console.clear()
