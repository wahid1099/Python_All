# computer vision - cv2

# from cv2 import VideoCapture
# from cv2 import waitKey
import cv2

cap=cv2.VideoCapture(0)


while True:
    __, frame=cap.read()

    cv2.imshow("Output",frame)


    if cv2.waitKey(10) == ord ('q'):
        break

cap.release()
cv2.destroyAllWindows()