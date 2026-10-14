import cv2
from ultralytics import YOLO


USB_CAMERA_INDEX = 2  # Brio 100 (/dev/video2)  index for laptop cam 0
cap = cv2.VideoCapture(USB_CAMERA_INDEX)

if not cap.isOpened():
    cap.release()
    raise RuntimeError(
        f"Could not open the USB camera at index {USB_CAMERA_INDEX}. "
        "Set USB_CAMERA_INDEX to the camera's device index."
    )

model = YOLO("yolov8n.pt")  # Load the YOLOv8 model

try:
    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            print("Could not read a frame from the USB camera.")
            break

        results = model(frame)  # Perform object detection on the frame

        annotated_frame = results[0].plot()  # Annotate the frame with detected objects

        cv2.imshow("Object Detection", annotated_frame)  # Display the annotated frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break
finally:
    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows