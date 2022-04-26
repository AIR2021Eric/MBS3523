import cv2
import serial
import time

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

# enable serial communication
ser = serial.Serial('COM5', baudrate=115200, timeout=1)
time.sleep(0.5)
pos = 90

cam = cv2.VideoCapture(0)

# define hsv range (orange)
hueLow = 0
hueHigh = 59
satLow = 130
satHigh = 225
valueLow = 157
valueHigh = 255

while True:
    ret, img = cam.read()

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(imgHSV,(hueLow,satLow,valueLow),(hueHigh,satHigh,valueHigh))
    # print(mask1.shape)

    Contours, no_use = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(Contours)
    for cont in Contours:
        area = cv2.contourArea(cont)  # get area of a contour
        (x, y, w, h) = cv2.boundingRect(cont)
        print([x,y,w,h])

        # filter out area of contours with less than 100
        if area > 500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            errorPan = (x + w/2) - 640/2
            print('errorPan', errorPan)
            if abs(errorPan) > 20:
                pos = int(pos - errorPan/30)
                print(type(pos))
            if pos >= 170:
                pos = 170
                print("Out of range")
            if pos <= 0:
                pos = 0
                print("out of range")
            servoPos = str(pos) + '\r'
            ser.write(servoPos.encode())
            print('servoPos = ', servoPos)
            time.sleep(0.1)
    cv2.imshow('MBS3523 Webcam', img)

    if cv2.waitKey(1) & 0xff == 27:
        break

ser.close()
cam.release()
cv2.destroyAllWindows()