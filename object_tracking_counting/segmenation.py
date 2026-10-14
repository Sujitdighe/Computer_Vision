import cv2
from ultralytics import YOLO
import numpy as np

model = YOLO('yolov8n-seg.pt')  # Use segmentation model

cap = cv2.VideoCapture('walking.mp4')  # Open the video file

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, classes=[0], persist=True, verbose=False)
    
    for r in results:
        annontated_frame = frame.copy()

        if r.masks is not None and r.boxes is not None and r.boxes.id is not None:
            masks = r.masks.data.numpy()
            boxes = r.boxes.xyxy.numpy()
            ids = r.boxes.id.numpy()

            if masks.size == 0:
                continue

            for i, mask in enumerate(masks):
                personal_id = ids[i]
                x1, y1, x2, y2 = map(int, boxes[i])
                mask_resized = cv2.resize(mask.astype(np.uint8)*255, (frame.shape[1], frame.shape[0]))
                contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                # Create a color mask
                color_mask = np.zeros_like(annontated_frame)
                cv2.drawContours(color_mask, contours, -1, (255, 100, 200), -1)  # Light blue fill
                
                # Overlay the color mask with transparency
                annontated_frame = cv2.addWeighted(annontated_frame, 1.0, color_mask, 0.4, 0)
                
                # Draw contour edge
                cv2.drawContours(annontated_frame, contours, -1, (0, 189, 208), 2)
                cv2.putText(annontated_frame, f"ID: {personal_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Object Tracking", annontated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
