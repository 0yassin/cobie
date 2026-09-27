from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def welcome():
    title = Text("COBIE",style="bold cyan")
    subtitle = Text("Your local AI coding agent",style="dim")
    subtitle2 = Text("Ask me anything ex: fix your project,chat,create a project ,ect",style="dim")
    content = Text()
    content.append_text(title)
    content.append("\n")
    content.append_text(subtitle)
    content.append("\n")
    content.append_text(subtitle2)
    
    console.print(
        Panel(
            content,border_style="cyan",
            padding=(1,4)
        )
    )
    console.print(
        "[dim]Type[/dim] [bold cyan]/help[/bold cyan]"
        "[dim] To see available commands.[/dim] \n"
    )
def user_prompt():
    return console.input("[bold cyan]> [/bold cyan]")
def show_response(res):
    console.print(
        Panel(
            res,
             title="[bold cyan]COBIE[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
    )
def show_goodbye():
    console.print("\n[bold cyan]Goodbye![/bold cyan]")
def show_message(message):
    console.print(f"[dim]{message}[/dim]")