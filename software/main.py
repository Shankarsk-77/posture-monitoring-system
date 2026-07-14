import cv2
import mediapipe as mp
from posture_detector import PostureDetector

cap = cv2.VideoCapture(0)

detector = PostureDetector()

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = detector.detect(frame)

    cv2.imshow("AI Posture Monitoring System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
