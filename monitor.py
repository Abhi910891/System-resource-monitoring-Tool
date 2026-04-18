import psutil
import time
from datetime import datetime

LOG_FILE = "logs.txt"

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, ram, disk

def log_data(cpu, ram, disk):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%\n")

def check_alerts(cpu, ram, disk):
    if cpu > 80:
        print(f"🚨 High CPU Usage: {cpu}%")
    if ram > 80:
        print(f"🚨 High RAM Usage: {ram}%")
    if disk > 90:
        print(f"🚨 High Disk Usage: {disk}%")

def monitor():
    while True:
        cpu, ram, disk = get_system_stats()

        print(f"CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%")

        log_data(cpu, ram, disk)
        check_alerts(cpu, ram, disk)

        time.sleep(2)

if __name__ == "__main__":
    monitor()