import asyncio
from bleak import BleakScanner
from datetime import datetime
from vendor_lookup import get_vendor

async def scan_bluetooth_live():
    try:
        devices = await BleakScanner.discover()
    except Exception as e:
        print("❌ Bluetooth scan error:", e)
        return []

    results = []
    for d in devices:
        mac = d.address
        name = d.name or "Unknown"
        vendor = get_vendor(mac)
        rssi = d.rssi if hasattr(d, "rssi") else -50  # fallback if RSSI not available

        results.append({
            "mac": mac,
            "name": name,
            "vendor": vendor or "Unknown Vendor",
            "rssi": rssi,
            "timestamp": datetime.now().isoformat()
        })
    return results
