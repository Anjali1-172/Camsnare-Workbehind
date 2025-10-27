def normalize_rssi(rssi):
    if rssi is None:
        return 0
    return max(0, min(100, int((rssi + 100) * 1.5)))  # Scale to 0–100

def rf_confidence(rf_strength):
    if rf_strength is None:
        return 0
    return min(100, int(rf_strength * 0.8))

def vendor_risk(vendor):
    risky_vendors = ["hikvision", "wyze", "tplink", "gopro", "xiaomi"]
    if not vendor:
        return 0
    vendor = vendor.lower()
    return 30 if any(v in vendor for v in risky_vendors) else 0

def thermal_score(temp):
    if temp is None:
        return 0
    if temp > 60:
        return 25
    elif temp > 50:
        return 15
    elif temp > 40:
        return 5
    else:
        return 0

def estimate_location(rssi):
    if rssi is None:
        return "Unknown"
    if rssi > -40:
        return "Near (East)"
    elif rssi > -60:
        return "Mid-range (North)"
    elif rssi > -80:
        return "Far (West)"
    else:
        return "Distant (South)"

def infer_power_status(rssi):
    if rssi is None:
        return "Unknown"
    return "On" if rssi > -70 else "Off"

def classify_connection(mac):
    if mac.startswith("00:1A:7D") or mac.startswith("B8:27:EB"):
        return "Bluetooth"
    return "Wi-Fi"

def is_camera_like(device):
    keywords = ["camera", "cam", "hikvision", "wyze", "tplink", "gopro", "xiaomi"]
    name = device.get("name", "").lower()
    vendor = device.get("vendor", "").lower()
    return any(k in name or k in vendor for k in keywords) or device.get("lens_detected") or device.get("ir_detected")

def calculate_confidence(device):
    score = 0
    score += normalize_rssi(device.get("rssi"))
    score += rf_confidence(device.get("rf_strength"))
    score += vendor_risk(device.get("vendor"))
    score += thermal_score(device.get("temp"))
    if device.get("ir_detected"):
        score += 15
    if device.get("lens_detected"):
        score += int(20 * device.get("reflection_intensity", 0.8))
    return min(100, score)

def classify_device_type(device):
    name = device.get("name", "").lower()
    vendor = device.get("vendor", "").lower()

    if any(k in name for k in ["iphone", "android", "samsung", "pixel", "oneplus", "xiaomi", "oppo", "vivo", "realme"]):
        return "Smartphone (Camera)"
    elif any(k in vendor for k in ["hikvision", "wyze", "tplink", "gopro", "xiaomi", "dahua", "reolink", "arlo"]):
        return "IP Camera"
    elif "webcam" in name or "usb cam" in name or "logitech" in vendor:
        return "Webcam"
    elif device.get("lens_detected") or device.get("ir_detected"):
        return "Hidden Camera"
    elif "laptop" in name or "macbook" in name or "notebook" in name:
        return "Laptop (Webcam)"
    else:
        return "Unknown Device"


def assess_risk_level(score):
    if score > 70:
        return "⚠️ High Risk"
    elif score > 40:
        return "⚠️ Medium Risk"
    else:
        return "✅ Low Risk"
