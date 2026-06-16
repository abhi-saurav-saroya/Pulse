from time import sleep

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.live import Live

from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_info
from monitor.disk import get_disk_info
from monitor.network import get_network_info
from monitor.processes import get_top_processes

from utils.formatter import format_bytes


console = Console()


def build_dashboard() -> Panel:
    cpu_usage = get_cpu_usage()
    memory = get_memory_info()
    disk = get_disk_info()
    network = get_network_info()
    processes = get_top_processes()

    layout = Layout(name="root")

    layout.split_row(
        Layout(name="stats", size=38),
        Layout(name="processes", minimum_size=70)
    )

    layout["processes"].split_column(
        Layout(name="top_processes", ratio=3, minimum_size=16),
        Layout(name="network", size=10)
    )
    
    layout["stats"].split_column(
        Layout(name="disk", ratio=1, minimum_size=8),
        Layout(name="memory", ratio=1, minimum_size=8),
        Layout(name="cpu", size=7)
    )

    # CPU Panel
    layout["cpu"].update(
        Panel(
            Align.center(
                f"[bold]{cpu_usage:.1f}%[/bold]",
                vertical="middle"
            ),
            title="CPU Usage",
            border_style="green",
            padding=(0, 1),
            expand=True
        )
    )

    # Memory Panel
    layout["memory"].update(
        Panel(
            Align.center(
                "\n".join(
                    [
                        f"Total : {format_bytes(memory.total)}",
                        f"Used  : {format_bytes(memory.used)}",
                        f"Free  : {format_bytes(memory.free)}",
                        f"Usage : {memory.percent:.1f}%"
                    ]
                ),
                vertical="middle"
            ),
            title="Memory",
            title_align="center",
            border_style="yellow",
            padding=(1, 2),
            expand=True
        )
    )

    # Disk Panel
    layout["disk"].update(
        Panel(
            Align.center(
                "\n".join(
                    [
                        f"Total : {format_bytes(disk.total)}",
                        f"Used  : {format_bytes(disk.used)}",
                        f"Free  : {format_bytes(disk.free)}",
                        f"Usage : {disk.percent:.1f}%"
                    ]
                ),
                vertical="middle"
            ),
            title="Disk",
            title_align="center",
            border_style="magenta",
            padding=(1, 2),
            expand=True
        )
    )

    # Processes Table
    process_table = Table(expand=True)

    process_table.add_column("PID", justify="center")
    process_table.add_column("Process", justify="center")
    process_table.add_column("CPU %", justify="center")

    for process in processes:
        name = process.name or "Unknown"

        if len(name) > 25:
            name = name[:22] + "..."

        process_table.add_row(
            str(process.pid),
            name,
            f"{process.cpu_percent:.1f}"
        )

    layout["top_processes"].update(
        Panel(
            process_table,
            title="Top Processes",
            border_style="blue",
            padding=(1, 1),
            expand=True
        )
    )

    # Network Panel
    network_panel = Panel(
        Align.center(
            "\n".join(
                [
                    f"Sent : {format_bytes(network.bytes_sent)}",
                    f"Recv : {format_bytes(network.bytes_recv)}"
                ]
            ),
            vertical="middle"
        ),
        title="Network",
        title_align="center",
        border_style="cyan",
        padding=(1, 2),
        expand=True
    )

    layout["network"].update(network_panel)

    return Panel(
        layout,
        title="Pulse",
        title_align="center",
        border_style="cyan",
        padding=(1, 1)
    )


def render_dashboard():
    try:
        with Live(
            console=console,
            screen=True
        ) as live:

            while True:
                live.update(build_dashboard())
                sleep(1)

    except KeyboardInterrupt:
        console.print("\n\n\n[yellow]\t\t\t\tPulse stopped.[/yellow]")