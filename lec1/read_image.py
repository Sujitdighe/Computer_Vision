import cv2

img1 = cv2.imread('download.jpeg')
img2 = cv2.imread('dataset-card.png')

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)  
cv2.waitKey(0)  # Wait for a key press to close the windows
cv2.imwrite('output_image.jpg', img1)  # Save the first image as a JPEG file