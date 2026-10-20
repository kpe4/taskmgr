import json
import platform
import time
import psutil
name_file = "../pc.json"


def search_data():
    pc_name = platform.node() + "NN"

    cpu_percent = psutil.cpu_percent()
    cpu_count = psutil.cpu_count(logical=False)
    thread_count = psutil.cpu_count(logical=True)

    cpu_freq = psutil.cpu_freq()
    cpu_speed = cpu_freq.current if cpu_freq else None

    virtual_memory = psutil.virtual_memory()

    disk_usage = psutil.disk_usage('/')

    return {
        "pc_name": pc_name,
        "cpu": {
            "percent": cpu_percent,
            "cores": cpu_count,
            "threads": thread_count,
            "speed_mhz": cpu_speed
        },
        "memory": {
            "total": virtual_memory.total,
            "available": virtual_memory.available,
            "used": virtual_memory.used,
            "percent": virtual_memory.percent
        },
        "disk": {
            "total": disk_usage.total,
            "used": disk_usage.used,
            "free": disk_usage.free,
            "percent": disk_usage.percent
        }
    }
def seve_data(data):
    with open(name_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    i = 10
    while i:
        print(i)
        seve_data(search_data())
        i -= 1
        time.sleep(5)
if __name__ == "__main__":
    main()