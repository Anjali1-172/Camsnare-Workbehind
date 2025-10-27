'''
PURPOSE: Detect heat signatures using thermal Camera or Simulated IR sensor input.
Reveals hotspots from hidden electronics or devices.
'''

import random
from datetime import datetime

def simulate_thermal_scan():
    hotspots = [
        {"location": "Smoke Detector (Ceiling)", "temp": random.randint(30, 65)},
        {"location": "Wall Clock (East Wall)", "temp": random.randint(25, 70)},
        {"location": "Charging Adapter (Near Bed)", "temp": random.randint(30, 60)},
        {"location": "Air Vent (North Wall)", "temp": random.randint(25, 55)},
        {"location": "Curtain Rod (Window Side)", "temp": random.randint(20, 50)}
    ]

    suspicious = []
    for spot in hotspots:
        if spot["temp"] > 50:
            spot["timestamp"] = datetime.now().isoformat()
            suspicious.append(spot)
    return suspicious
