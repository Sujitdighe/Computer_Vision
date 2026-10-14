import cv2
from ultralytics import YOLO


cap = cv2.VideoCapture("tracking.mp4")  # Open the video file

model = YOLO("yolov8n.pt")  # Load the YOLOv8 model

while True:
    ret, frame = cap.read()  # Read a frame from the video

    results = model(frame, classes=[0])  # Perform object detection on the frame

    annotated_frame = results[0].plot()  # Annotate the frame with detected objects

    cv2.imshow("Object Detection", annotated_frame)  # Display the annotated frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()  # Release the video capture
cv2.destroyAllWindows()  # Close all OpenCV windows