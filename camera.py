import cv2
import os

# Set up the camera
cap = cv2.VideoCapture(0)

# Capture an image
ret, frame = cap.read()

# Define the file path and name for the captured image
save_path = 'C:/Users/Joel/Desktop/Intern2/'
file_name = 'image1.jpg'

# Save the image to the specified folder
cv2.imwrite(os.path.join(save_path, file_name), frame)

# Release the camera
cap.release()

# Run the object detection script
os.system('python object_detection.py')
