import psutil


def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=None)