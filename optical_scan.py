# PURPOSE: detect lens-like reflections using your cam and flashlight
# Helps detect covert lenses embedded in decor 
# adds a physical inspection layer to the project.
import cv2
import time
from datetime import datetime

def detect_reflections():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Optical scan: Camera not available.")
        return []

    print("🔦 Use a flashlight to scan the room while this runs...")
    detected = []
    
    start_time = time.time()
    while True:
        if time.time() - start_time > 10:
            break  # Run for 10 seconds
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 50:
                x, y, w, h = cv2.boundingRect(cnt)
                detected.append({
                    "location": f"Reflection at ({x},{y})",
                    "timestamp": datetime.now().isoformat(),
                    "lens_detected": True,
                    "reflection_intensity": 0.8  # Placeholder
                })

        cv2.imshow("Reflection Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return detected
