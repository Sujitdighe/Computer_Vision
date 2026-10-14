import cv2
from ultralytics import YOLO
import numpy as np
from collections import defaultdict, deque

cap = cv2.VideoCapture('car_tracking.mp4')  # Change to your vehicle video file

model = YOLO("yolov8n.pt") 

id_map = {}
next_id = 1

trail = defaultdict(lambda: deque(maxlen=30))
appear = defaultdict(int)

# Vehicle class IDs for COCO dataset: car=2, motorcycle=3, bus=5, truck=7
vehicle_classes = [2, 3, 5, 7]

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('annotated_round_racking.mp4', fourcc, fps, (width, height))

while True:
    ret, frames = cap.read()
    if not ret:
        break

    res = model.track(frames, persist=True, verbose=False)

    annotated_frame = frames.copy()

    if res[0].boxes and res[0].boxes.id is not None:
        boxes = res[0].boxes.xyxy.numpy()
        ids = res[0].boxes.id.numpy()
        classes = res[0].boxes.cls.numpy()  # Get class IDs

        for box, oid, cls_id in zip(boxes, ids, classes):
            if int(cls_id) not in vehicle_classes:
                continue  # Skip non-vehicle objects

            x1, y1, x2, y2 = map(int, box)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            appear[oid] += 1

            if appear[oid] >= 3 and oid not in id_map:
                id_map[oid] = next_id
                next_id += 1

            if oid in id_map:
                sid = id_map[oid]
                trail[oid].append((cx, cy))
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f"Vehicle ID: {sid}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.circle(annotated_frame, (cx, cy), 5, (0, 0, 255), -1)
                # Draw trail
                for i in range(1, len(trail[oid])):
                    cv2.line(annotated_frame, trail[oid][i - 1], trail[oid][i], (100, 100, 255), 2)

    out.write(annotated_frame)
    cv2.imshow("Vehicle Tracking", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
