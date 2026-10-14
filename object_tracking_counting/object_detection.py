import cv2
from ultralytics import YOLO


model = YOLO('yolov8n.pt')  # Load the YOLOv8 model

image = cv2.imread('download.jpeg')  # Read the input image

results =model(image)

annotated_image = results[0].plot()  # Annotate the image with detected objects

cv2.imshow("Annotated image", annotated_image)

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows