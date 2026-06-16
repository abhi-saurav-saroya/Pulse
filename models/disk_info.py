from dataclasses import dataclass


@dataclass
class DiskInfo:
    total: int
    used: int
    free: int
    percent: float