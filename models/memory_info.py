from dataclasses import dataclass


@dataclass
class MemoryInfo:
    total: int
    used: int
    free: int
    percent: float