import cv2

def show_alert(frame):

    cv2.putText(

        frame,

        "Bad Posture!",

        (20,40),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,0,255),

        2

    )
