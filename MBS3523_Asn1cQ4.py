import cv2
import random
print(cv2.__version__)  # check cv2 version

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')  # load face cascade classifier file

cam = cv2.VideoCapture(0)  # enable webcam capture and save to cam
# initialise variables
colour = (0,0,0)
x = y = w = h = counter = 0
while True:
    # change text and square with random colour when counter refreshes
    if counter == 0:
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if counter >= 10:
        counter = -1

    _, frame = cam.read()  # start capture and save to frame

    faces = faceCascade.detectMultiScale(frame, 1.1, 3)  # detect frontal face

    # draw square if face exist, reset when not exist and disable the function of imgCrop
    if len(faces):
        x = faces[0][0]
        y = faces[0][1]
        w = faces[0][2]
        h = faces[0][3]
        cv2.rectangle(frame, (x, y), (x + w, y + h), colour, 3)
    else:
        x = y = w = h = 0

    imgCrop = frame[y:y+h, x:x+w]  # save colored face
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert colour form bgr to gray
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # return colour from gray to bgr, frame stays in gray scale with 3 color layers
    cv2.putText(frame, 'MBS3523 Assignment 1c - Q4  Name: Tong Ying Yui Eric', (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65,  # print color text
                colour, 2)
    frame[y:y + h, x:x + w] = imgCrop  # restore colored face

    cv2.imshow('MBS3523_Asn1cQ4', frame)  # create window call MBS3523 and show captured image

    counter += 1    # counter increment for changing the next text and square color

    if cv2.waitKey(5) & 0xff == ord('q'):  # wait 5ms and type q on keyboard
        break

cam.release()  # release resources
cv2.destroyAllWindows()  # close all created windows