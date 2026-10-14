import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Load the YOLOv8 model

cap = cv2.VideoCapture(2)  # Open the default camera (webcam)

while True:
    ret, frame = cap.read()
    if not ret:
        break   
    results = model(frame)  # Perform object detection
    annotated_frame = results[0].plot()  # Annotate the frame with detected objects
    cv2.imshow("Live Object Detection", annotated_frame)  # Display the annotated frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
cap.release()
cv2.destroyAllWindows()  # Close all OpenCV windows