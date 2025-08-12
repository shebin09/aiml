import cv2
import matplotlib.pyplot as plt
import os

cap = cv2.VideoCapture(0)  # 0 = default webcam
ret, frame = cap.read()
cap.release()

if not ret:
    raise Exception("Could not capture image from webcam")

# Convert from BGR (OpenCV default) to RGB
image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(image)