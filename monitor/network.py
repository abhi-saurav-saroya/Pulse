import psutil

from models.network_info import NetworkInfo


def get_network_info() -> NetworkInfo:
    network = psutil.net_io_counters()

    return NetworkInfo(
        bytes_sent=network.bytes_sent,
        bytes_recv=network.bytes_recv
    )