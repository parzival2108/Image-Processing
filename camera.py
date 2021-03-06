import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter("captured1.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

while True:
    ret, frame = cap.read()
    
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    writer.write(frame)
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()