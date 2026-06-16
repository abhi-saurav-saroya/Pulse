from rich.console import Console
from rich.panel import Panel

console = Console()


def render_dashboard():
    console.print(
        Panel(
            "Pulse\n ->Your System's Heartbeat",
            title="Pulse - Your System's Heartbeat"
        )
    )