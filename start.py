import cv2
from ultralytics import YOLO
import time

# model
model = YOLO("yolov8n.pt")

# kamera
cap = cv2.VideoCapture(0)

# kamera çözünürlüğü
cap.set(3,1280)
cap.set(4,720)

# fullscreen pencere
cv2.namedWindow("Stark Vision", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Stark Vision", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

prev_time = 0

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # FPS kontrolü (stabil)
    current_time = time.time()
    fps = 1/(current_time-prev_time)
    prev_time = current_time

    # nesne tanıma
    results = model(frame, conf=0.5)

    frame = results[0].plot()

    # FPS yazdır
    cv2.putText(frame,f"FPS: {int(fps)}",(20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Stark Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()