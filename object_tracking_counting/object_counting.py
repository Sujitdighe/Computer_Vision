import cv2
from ultralytics import YOLO
import numpy as np

cap = cv2.VideoCapture('walking.mp4')  # Open the video file
unique_id =  set()  # Set to store unique object IDs
model = YOLO("yolov8n.pt")  # Load the YOLOv8 model

while True:
    ret, frame = cap.read()
    results = model.track(frame, classes=[0], persist=False, verbose=False) 
    
    annotated_frame = results[0].plot()  # Annotate the frame with detected objects

    if results[0].boxes and results[0].boxes.id is not None:
        ids = results[0].boxes.id.numpy()

        for oid in ids:
            unique_id.add(oid)
            
        cv2.putText(annotated_frame, f"Unique IDs: {len(unique_id)}", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Object Tracking", annotated_frame)  # Display the annotated frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break   
cap.release()  # Release the video capture
cv2.destroyAllWindows()  # Close all OpenCV windows
      