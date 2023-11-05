import cv2
import numpy as np

# Load a pre-trained classifier for detecting Braille dots (This is a simple example)
braille_classifier = cv2.CascadeClassifier('braille_classifier.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 for default camera, you can change it to a specific camera if needed

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for easier processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Braille dots
    braille_dots = braille_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Iterate through detected dots
    for (x, y, w, h) in braille_dots:
        # Draw a rectangle around the detected Braille dot
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected Braille dots
    cv2.imshow('Braille Scanner', frame)

    # Check for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
