from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

questions = [
    {
        "q": "What is the capital of Nigeria?",
        "options": ["Lagos", "Abuja", "Port Harcourt", "Kano"],
        "answer": "Abuja"
    },
    {
        "q": "Which programming language are we using right now?",
        "options": ["Java", "Python", "JavaScript", "C++"],
        "answer": "Python"
    },
    {
        "q": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "q": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Control Processing Unit", "Central Power Unit"],
        "answer": "Central Processing Unit"
    }
]

console.print(Panel.fit("[bold cyan]🎯 General Knowledge Quiz[/bold cyan]", border_style="blue"))

name = Prompt.ask("[bold green]What is your name?[/bold green]")

console.print(f"\nHello, {name}! Let's test your knowledge.\n")

score = 0

for i, q in enumerate(questions, 1):
    console.print(f"[bold yellow]Question {i}/{len(questions)}:[/bold yellow]")
    console.print(f"[bold]{q['q']}[/bold]\n")
    
    for idx, option in enumerate(q["options"], 1):
        console.print(f"{idx}. {option}")
    
    answer = Prompt.ask("\nYour answer (1-4)", choices=["1","2","3","4"])
    
    selected = q["options"][int(answer)-1]
    
    if selected == q["answer"]:
        console.print("[bold green]✅ Correct![/bold green]\n")
        score += 1
    else:
        console.print(f"[bold red]❌ Wrong! The correct answer was: {q['answer']}[/bold red]\n")

console.print(Panel.fit(f"[bold]Quiz Completed![/bold]\nYour Score: [cyan]{score}/{len(questions)}[/cyan]", border_style="green"))

if score == len(questions):
    console.print("[bold green]🏆 Perfect Score! You're amazing![/bold green]")
elif score >= len(questions)//2:
    console.print("[bold yellow]Good job! Keep learning.[/bold yellow]")
else:
    console.print("[bold red]Better luck next time. Practice makes perfect![/bold red]")

console.print(f"\nThanks for playing, {name}! 💪")
