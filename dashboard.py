import streamlit as st
import psutil
import time

st.set_page_config(page_title="System Monitor", layout="wide")

st.title("📊 System Resource Monitoring Dashboard")

# Placeholders for dynamic update
cpu_placeholder = st.empty()
ram_placeholder = st.empty()
disk_placeholder = st.empty()

# Progress bars
cpu_bar = st.progress(0)
ram_bar = st.progress(0)
disk_bar = st.progress(0)

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # Update text
    cpu_placeholder.metric("CPU Usage", f"{cpu}%")
    ram_placeholder.metric("RAM Usage", f"{ram}%")
    disk_placeholder.metric("Disk Usage", f"{disk}%")

    # Update bars
    cpu_bar.progress(int(cpu))
    ram_bar.progress(int(ram))
    disk_bar.progress(int(disk))

    # Alerts
    if cpu > 80:
        st.warning(f"🚨 High CPU Usage: {cpu}%")
    if ram > 80:
        st.warning(f"🚨 High RAM Usage: {ram}%")
    if disk > 90:
        st.error(f"🚨 Disk Almost Full: {disk}%")

    time.sleep(2)