import asyncio
from datetime import datetime
from bluetooth_scan import scan_bluetooth_live
from thermal_scan import simulate_thermal_scan
from rf_sweep import simulate_rf_sweep
from wifi_scan import scan_wifi_live
from signal_utils import (
    calculate_confidence,
    estimate_location,
    infer_power_status,
    classify_connection,
    is_camera_like,
    classify_device_type,
    assess_risk_level,
)

def scan_camera_devices(scan_range=10):
    all_devices = []

    try:
        print("🔍 Bluetooth scan...")
        bluetooth = asyncio.run(scan_bluetooth_live())
        for device in bluetooth:
            if device.get("rssi") and abs(device["rssi"]) > (100 - scan_range * 5):
                continue
            device["confidence_score"] = calculate_confidence(device)
            device["location"] = estimate_location(device.get("rssi"))
            device["power_status"] = infer_power_status(device.get("rssi"))
            device["connection_type"] = "Bluetooth"
            device["device_type"] = classify_device_type(device)
            device["risk_level"] = assess_risk_level(device["confidence_score"])
            all_devices.append(device)
        print(f"✅ Bluetooth devices detected: {len(bluetooth)}")
    except Exception as e:
        print("❌ Bluetooth scan failed:", e)

    try:
        print("🌡️ Thermal scan...")
        thermal = simulate_thermal_scan()
        for spot in thermal:
            spot["confidence_score"] = calculate_confidence(spot)
            spot["location"] = spot.get("location", "Unknown")
            spot["power_status"] = "On"
            spot["connection_type"] = "Thermal"
            spot["device_type"] = classify_device_type(spot)
            spot["risk_level"] = assess_risk_level(spot["confidence_score"])
            all_devices.append(spot)
        print(f"✅ Thermal hotspots detected: {len(thermal)}")
    except Exception as e:
        print("❌ Thermal scan failed:", e)

    try:
        print("📡 RF sweep...")
        rf = simulate_rf_sweep()
        for signal in rf:
            if signal.get("rf_strength") and signal["rf_strength"] < (scan_range * 10):
                signal["confidence_score"] = calculate_confidence(signal)
                signal["location"] = "RF Zone"
                signal["power_status"] = "Unknown"
                signal["connection_type"] = "RF"
                signal["device_type"] = classify_device_type(signal)
                signal["risk_level"] = assess_risk_level(signal["confidence_score"])
                all_devices.append(signal)
        print(f"✅ RF signals detected: {len(rf)}")
    except Exception as e:
        print("❌ RF sweep failed:", e)

    try:
        print("📶 Wi-Fi scan...")
        wifi = scan_wifi_live()
        for device in wifi:
            if device.get("rssi") and abs(device["rssi"]) > (100 - scan_range * 5):
                continue
            device["confidence_score"] = calculate_confidence(device)
            device["location"] = estimate_location(device.get("rssi"))
            device["power_status"] = infer_power_status(device.get("rssi"))
            device["connection_type"] = "Wi-Fi"
            device["device_type"] = classify_device_type(device)
            device["risk_level"] = assess_risk_level(device["confidence_score"])
            all_devices.append(device)
        print(f"✅ Wi-Fi devices detected: {len(wifi)}")
    except Exception as e:
        print("❌ Wi-Fi scan failed:", e)

    print("✅ Fusion complete. Filtering camera-bearing devices...")

    camera_devices = [
        d for d in all_devices
        if "Camera" in d.get("device_type", "") or is_camera_like(d)
    ]

    print(f"🎯 Camera-bearing devices found: {len(camera_devices)}")
    return camera_devices

# ✅ Compatibility alias
scan_non_camera = scan_camera_devices

def scan_infrared():
    try:
        print("🔦 Infrared scan started...")
        from infrared_sweep import detect_ir_leds
        results = detect_ir_leds()
        for r in results:
            r["confidence_score"] = calculate_confidence(r)
            r["location"] = r.get("location", "Unknown")
            r["power_status"] = "On"
            r["connection_type"] = "Infrared"
            r["device_type"] = classify_device_type(r)
            r["risk_level"] = assess_risk_level(r["confidence_score"])
        return results
    except Exception as e:
        print("❌ Infrared scan failed:", e)
        return []

def scan_optical():
    try:
        print("📷 Optical scan started...")
        from optical_scan import detect_reflections
        results = detect_reflections()
        for r in results:
            r["confidence_score"] = calculate_confidence(r)
            r["location"] = r.get("location", "Unknown")
            r["power_status"] = "On"
            r["connection_type"] = "Optical"
            r["device_type"] = classify_device_type(r)
            r["risk_level"] = assess_risk_level(r["confidence_score"])
        return results
    except Exception as e:
        print("❌ Optical scan failed:", e)
        return []