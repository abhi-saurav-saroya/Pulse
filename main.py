from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_info
from monitor.disk import get_disk_info
from monitor.processes import get_top_processes

def main():
    print("\n=== PULSE : Your System's Heartbeat ===\n")
    
    cpu_usage = get_cpu_usage()
    memory = get_memory_info()
    disk = get_disk_info()
    processes = get_top_processes()
    
    print(f"CPU Usage: {cpu_usage}%")
    
    print("\nMemory")
    print(f"  Total   : {memory.total}")
    print(f"  Used    : {memory.used}")
    print(f"  Free    : {memory.free}")
    print(f"  Percent : {memory.percent}%")
    
    print("\nDisk")
    print(f"  Total   : {disk.total}")
    print(f"  Used    : {disk.used}")
    print(f"  Free    : {disk.free}")
    print(f"  Percent : {disk.percent}%")
    
    print("\nTop Processes")
    print("-" * 50)
    
    for process in processes:
        print(
            f"PID: {process.pid:<8}"
            f"Name: {process.name:<25}"
            f"CPU: {process.cpu_percent}%"
        )



if __name__ == "__main__":
    main()
