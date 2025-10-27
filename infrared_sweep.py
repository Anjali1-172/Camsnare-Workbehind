import cv2
import numpy as np
from datetime import datetime
import time 

def detect_ir_leds():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Infrared scan: Camera not available.")
        return []

    detected = []
    start_time = time.time()
    while True:
        if time.time() - start_time > 10:
            break  # Run for 10 seconds
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (0, 0, 200), (180, 25, 255))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 30:
                x, y, w, h = cv2.boundingRect(cnt)
                detected.append({
                    "location": f"IR hotspot at ({x},{y})",
                    "timestamp": datetime.now().isoformat(),
                    "ir_detected": True
                })

        cv2.imshow("Infrared Camera Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return detected
