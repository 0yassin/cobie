from cli.ui import console


def show_help():
    console.print(
        """
[bold cyan]COBIE Commands[/bold cyan]

  [bold]/help[/bold]     Show available commands
  [bold]/clear[/bold]    Clear conversation history
  [bold]/exit[/bold]     Exit COBIE
"""
    )

def clear_history(agent):
    agent.contents.clear()
    console.print("[green]✓ Conversation history cleared.[/green]")