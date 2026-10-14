import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Open the default camera

frames = []  # List to store captured frames

gap = 5

count = 0

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        print("Failed to capture frame")
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    frames.append(gray_frame)  # Append the frame to the list

    if len(frames) > gap + 1:
        frames.pop(0)

    cv2.putText(frame, f"Frame Count: {len(frames)}", (10, 30),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)
    
    if len(frames) > gap:
        diff = cv2.absdiff(frames[0], frames[-1])  # Calculate the difference between the last two frames
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) < 2000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)   

        motion = any(cv2.contourArea(c) > 2000 for c in contours)  # Check if there is significant motion

        if motion:
            cv2.putText(frame, "Motion Detected", (10, 50), 
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2)
            cv2.imwrite('motion_detected.jpg', frame)  # Save the frame with motion detected
            print("Motion detected, frame saved as 'motion_detected.jpg'")

        cv2.imshow('Motion Detection', frame)  # Display the frame with motion detection
    count += 1
    #cv2.imshow('Camera Feed', frame)  # Display the frame  
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows

