from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

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

    # Main layout wrapped inside the parent Pulse panel
    layout = Layout(name="root")

    # Left side: Disk, Memory, CPU with flexible sizing
    # Right side: Top Processes and Network stacked vertically
    layout.split_row(
        Layout(name="stats", ratio=1, minimum_size=36),
        Layout(name="processes", ratio=2, minimum_size=60)
    )

    layout["processes"].split_column(
        Layout(name="top_processes", ratio=3),
        Layout(name="network", size=8)
    )

    layout["stats"].split_column(
        Layout(name="disk", ratio=1, minimum_size=7),
        Layout(name="memory", ratio=1, minimum_size=7),
        Layout(name="cpu", size=5)
    )

    # CPU Panel
    layout["cpu"].update(
        Panel(
            Align.center(f"[bold]{cpu_usage:.1f}%[/bold]", vertical="middle", width=16),
            title="CPU Usage",
            border_style="green",
            padding=(0, 1),
            expand=True
        )
    )

    # Memory Panel
    layout["memory"].update(
        Panel(
            "\n".join(
                [
                    f"Total : {format_bytes(memory.total)}",
                    f"Used  : {format_bytes(memory.used)}",
                    f"Free  : {format_bytes(memory.free)}",
                    f"Usage : {memory.percent:.1f}%"
                ]
            ),
            title="Memory",
            border_style="yellow",
            padding=(1, 2),
            expand=True
        )
    )

    # Disk Panel
    layout["disk"].update(
        Panel(
            "\n".join(
                [
                    f"Total : {format_bytes(disk.total)}",
                    f"Used  : {format_bytes(disk.used)}",
                    f"Free  : {format_bytes(disk.free)}",
                    f"Usage : {disk.percent:.1f}%"
                ]
            ),
            title="Disk",
            border_style="magenta",
            padding=(1, 2),
            expand=True
        )
    )

    # Processes Table
    process_table = Table(expand=True)

    process_table.add_column("PID", justify="right")
    process_table.add_column("Process")
    process_table.add_column("CPU %", justify="right")

    for process in processes:
        process_table.add_row(
            str(process.pid),
            process.name,
            f"{process.cpu_percent:.1f}"
        )

    network_panel = Panel(
        "\n".join(
            [
                f"Sent : {format_bytes(network.bytes_sent)}",
                f"Recv : {format_bytes(network.bytes_recv)}"
            ]
        ),
        title="Network",
        border_style="cyan",
        padding=(1, 2),
        expand=True
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

    layout["network"].update(network_panel)

    return Panel(
        layout,
        title="Pulse",
        title_align="center",
        border_style="cyan",
        padding=(1, 1)
    )


def render_dashboard():
    console.print(build_dashboard())