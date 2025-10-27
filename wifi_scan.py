import subprocess
import json
import shutil
import os
from datetime import datetime
from vendor_lookup import get_vendor


def scan_wifi_live():
    # Check if nmap is available
    if not shutil.which("nmap"):
        print("❌ Nmap not found in PATH.")
        return []

    # Warm-up ping to wake up network stack
    os.system("ping 127.0.0.1 > nul")

    # Try scanning with timeout
    try:
        result = subprocess.check_output(['nmap', '-sn', '192.168.1.1-50'], timeout=15).decode()
    except subprocess.TimeoutExpired:
        print("⚠️ First attempt timed out. Retrying...")
        try:
            result = subprocess.check_output(['nmap', '-sn', '192.168.1.1-50'], timeout=15).decode()
        except Exception as e:
            print("❌ Wi-Fi scan failed again:", e)
            return []

    devices = []
    lines = result.split('\n')
    current = {}

    for line in lines:
        if "Nmap scan report for" in line:
            current['ip'] = line.split(" ")[-1]
        elif "MAC Address" in line:
            parts = line.split("MAC Address: ")[1].split(" ")
            current["mac"] = parts[0]
            current["vendor"] = get_vendor(current["mac"])  # ✅ FIXED: now using current["mac"]
            current["timestamp"] = datetime.now().isoformat()
            devices.append(current)
            current = {}

    return devices
