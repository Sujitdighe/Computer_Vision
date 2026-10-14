import cv2

img = cv2.imread('dataset-card.png')

resized_img = cv2.resize(img, (500, 500))  # Resize the image to 800x600 pixels
cv2.imshow('Resized Image', resized_img)  # Display the resized image

greyscale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
cv2.imshow('Greyscale Image', greyscale_img)  # Display the grayscale image

blurring_img = cv2.GaussianBlur(resized_img, (5, 5), 0)  # Apply Gaussian blur
cv2.imshow('Blurred Image', blurring_img)  # Display the blurred image

edged_img = cv2.Canny(resized_img, 100, 200)  # Apply Canny edge detection
cv2.imshow('Edged Image', edged_img)  # Display the edges detected in the image     

cv2.waitKey(0)  # Wait for a key press to close the windows
cv2.destroyAllWindows()  # Close all OpenCV windows