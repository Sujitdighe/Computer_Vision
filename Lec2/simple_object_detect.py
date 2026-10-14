import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Load the YOLOv8 model

image = cv2.imread('output_image.jpg')  # Read the input image

results = model(image)  # Perform object detection

annotated_image = results[0].plot()  # Annotate the image with detected objects

cv2.imshow("Annotated Image", annotated_image)  # Display the annotated image
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows 