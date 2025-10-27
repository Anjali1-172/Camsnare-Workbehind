'''
PURPOSE: Detect RF signals from transmitting devices.
Adds electromagnetic signal detection to Camsnare.

* RF (radio frequency) signals are wireless, high-frequency electromagnetic waves used to carry information across distances without physical wires * 
'''
import random
from datetime import datetime

def simulate_rf_sweep():
    rf_signals = [
        {"frequency": "2.4 GHz", "rf_strength": random.randint(30, 90)},
        {"frequency": "5.8 GHz", "rf_strength": random.randint(20, 70)},
        {"frequency": "900 MHz", "rf_strength": random.randint(10, 60)}
    ]
    for signal in rf_signals:
        signal["timestamp"] = datetime.now().isoformat()
    return rf_signals
