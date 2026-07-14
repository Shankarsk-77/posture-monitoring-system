import cv2
import mediapipe as mp

class PostureDetector:

    def __init__(self):

        self.mpPose = mp.solutions.pose

        self.pose = self.mpPose.Pose()

        self.mpDraw = mp.solutions.drawing_utils

    def detect(self, img):

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = self.pose.process(rgb)

        if results.pose_landmarks:

            self.mpDraw.draw_landmarks(
                img,
                results.pose_landmarks,
                self.mpPose.POSE_CONNECTIONS
            )

        return img
