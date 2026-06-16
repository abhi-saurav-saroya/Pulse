import psutil
from models.memory_info import MemoryInfo


def get_memory_info() -> MemoryInfo:
    memory = psutil.virtual_memory()

    return MemoryInfo(
        total = memory.total,
        used = memory.used,
        free = memory.available,
        percent = memory.percent
    )