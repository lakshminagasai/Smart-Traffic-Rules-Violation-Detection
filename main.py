import cv2
import math
import time
from ultralytics import YOLO

# --- Load YOLO Models ---
vehicle_model = YOLO('yolov8n.pt')            # For car/bike detection
helmet_model = YOLO('helmet-yolov8n.pt')      # For helmet detection

video = cv2.VideoCapture('test.mp4')

WIDTH, HEIGHT = 1280, 720
SPEED_LIMIT = 30  # km/h

def estimate_speed(loc1, loc2, fps):
    d_pixels = math.sqrt((loc2[0]-loc1[0])**2 + (loc2[1]-loc1[1])**2)
    ppm = 8.8
    d_meters = d_pixels / ppm
    if fps == 0:
        fps = 18
    return d_meters * fps * 3.6

prev_boxes = {}
out = cv2.VideoWriter('output_minimal.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (WIDTH, HEIGHT))
print("🚗 Starting minimal Traffic Violation Detector...")

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    start_time = time.time()

    results = vehicle_model(frame, stream=True)
    current_boxes = {}

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = vehicle_model.names[cls]

            if label not in ["car", "motorbike", "motorcycle"]:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            color = (0, 255, 0)
            status_text = ""

            current_boxes[label] = (x1, y1, x2, y2)

            # --- SPEED CHECK ---
            speed = 0
            if label in prev_boxes:
                speed = estimate_speed(prev_boxes[label], current_boxes[label], fps=15)
                if speed > SPEED_LIMIT:
                    color = (0, 0, 255)
                    status_text = "Overspeeding"

            # --- HELMET CHECK (for bikes only) ---
            if label in ["motorbike", "motorcycle"]:
                roi = frame[y1:y2, x1:x2]
                helmet_detected = False
                if roi.size != 0:
                    helmet_results = helmet_model.predict(roi, conf=0.4, verbose=False)
                    for hr in helmet_results:
                        for hbox in hr.boxes:
                            h_label = helmet_model.names[int(hbox.cls[0])].lower()
                            if "helmet" in h_label:
                                helmet_detected = True
                if not helmet_detected:
                    color = (255,0,0)
                    status_text = "No Helmet"

            # --- Draw bounding box & label only if violation ---
            if status_text:
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, status_text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    prev_boxes = current_boxes
    end_time = time.time()
    fps = 1.0 / (end_time - start_time)

    cv2.imshow("Traffic Violation Detection", frame)
    out.write(frame)

    if cv2.waitKey(1) == 27:  # ESC to exit
        break

video.release()
out.release()
cv2.destroyAllWindows()
print("✅ Done. Output saved as output_minimal.avi")
