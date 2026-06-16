import psutil
from models.process_info import ProcessInfo


def get_top_processes(limit: int = 5) -> list[ProcessInfo]:
    processes: list[ProcessInfo] = []

    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent']
    ):
        try:
            processes.append(
                ProcessInfo(
                    pid=process.info['pid'],
                    name=process.info['name'],
                    cpu_percent=process.info['cpu_percent']
                )
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    processes.sort(
        key=lambda process: process.cpu_percent,
        reverse=True
    )

    return processes[:limit]