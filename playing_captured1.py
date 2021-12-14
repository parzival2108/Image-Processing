import cv2
import time



read_cap = cv2.VideoCapture("captured1.mp4")
if read_cap.isOpened() == False:
    print("Error FILE NOT FOUND or WRONG CODEC")
while read_cap.isOpened():
    ret, frame = read_cap.read()
    if ret == True:
        time.sleep(1/30)
        cv2.imshow("frame", frame)
        if cv2.waitKey(10) & 0xFF==ord("q"):
            break
    else:
        break
read_cap.release()
cv2.destroyAllWindows()