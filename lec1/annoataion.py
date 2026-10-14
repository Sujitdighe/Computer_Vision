import cv2

import numpy as np

canavas = np.zeros((500, 500, 3), dtype="uint8")  # Create a blank canvas

cv2.line(canavas, (0, 0), (500, 500), (0, 0, 255), 2)  # Draw a blue line
