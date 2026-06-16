from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_info
from monitor.disk import get_disk_info
from monitor.processes import get_top_processes

from utils.formatter import format_bytes

console = Console()

def render_dashboard():
    cpu_usage = get_cpu_usage()
    memory = get_memory_info()
    disk = get_disk_info()
    processes = get_top_processes()

    console.print(
        Panel(
            "Your System's Heartbeat",
            title="Pulse",
        )
    )

    console.print(
        Panel(
            f"{cpu_usage:.1f}%",
            title="CPU Usage"
        )
    )

    console.print(
        Panel(
            "\n".join([
                f"Total   : {format_bytes(memory.total)}",
                f"Used    : {format_bytes(memory.used)}",
                f"Free    : {format_bytes(memory.free)}",
                f"Usage   : {memory.percent}%"
            ]),
            title="Memory"
        )
    )

    console.print(
        Panel(
            "\n".join([
                f"Total   : {format_bytes(disk.total)}",
                f"Used    : {format_bytes(disk.used)}",
                f"Free    : {format_bytes(disk.free)}",
                f"Usage   : {disk.percent}%"
            ]),
            title="Disk"
        )
    )

    process_table = Table(show_header=True)

    process_table.add_column("PID")
    process_table.add_column("Name")
    process_table.add_column("CPU %")

    for process in processes:
        process_table.add_row(
            str(process.pid),
            process.name,
            str(process.cpu_percent)
        )

    console.print(
        Panel(
            process_table,
            title="Top Processes"
        )
    )