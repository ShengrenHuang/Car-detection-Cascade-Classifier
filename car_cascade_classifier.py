import cv2


car_cascade = cv2.CascadeClassifier('cars.xml')
cap = cv2.VideoCapture('video1.avi')
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.2, 3)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)


    cv2.imshow('img',frame)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

cap.release()


cv2.destroyALLWindows()
