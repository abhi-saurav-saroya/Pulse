import os
import psutil

from models.disk_info import DiskInfo


def get_disk_info() -> DiskInfo:
    drive = os.path.abspath(os.sep)

    disk = psutil.disk_usage(drive)

    return DiskInfo(
        total = disk.total,
        used = disk.used,
        free = disk.free,
        percent = disk.percent
    )