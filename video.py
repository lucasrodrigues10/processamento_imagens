import cv2
import numpy as nps

cap = cv2.VideoCapture(0)

while True:
    existe_frame, frame = cap.read()
    cv2.imshow('webcam', frame)
    if (cv2.waitKey(1)) & (0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
