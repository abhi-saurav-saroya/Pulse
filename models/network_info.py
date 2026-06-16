from dataclasses import dataclass


@dataclass
class NetworkInfo:
    bytes_sent: int
    bytes_recv: int