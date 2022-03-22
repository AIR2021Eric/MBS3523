import cv2
import math

# define frame width and frame height
width = 640
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # enable webcam capture and save to cam
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # set frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # set frame height

def nil(x):
    pass

# create window and trackbars
cv2.namedWindow('MBS3523_Asn1dQ5')
cv2.createTrackbar('X_POS','MBS3523_Asn1dQ5',int(width/2),width,nil)
cv2.createTrackbar('Y_POS','MBS3523_Asn1dQ5',int(height/2),height,nil)

while True:
    _, img = cam.read() # start capture and save to img

    # get trackbars position
    x = cv2.getTrackbarPos('X_POS', 'MBS3523_Asn1dQ5')
    y = cv2.getTrackbarPos('Y_POS', 'MBS3523_Asn1dQ5')

    # create 3 colours, colour changes when trackbar position changes
    colourA = int(255*y/480)
    colourB = int(255*x/640)
    colourC = int(255*math.sqrt(x**2+y**2)/800)

    # assign colours
    colourX = (255-colourB,colourC,colourA)
    colourY = (colourC,255-colourA,colourB)
    colourT = (colourA, colourB, 255-colourC)

    # draw lines and put text in img
    img = cv2.line(img, (x, 0), (x, height), colourX, 3)
    img = cv2.line(img, (0, y), (width, y), colourY, 3)
    cv2.putText(img, 'MBS3523 Assignment 1d - Q5  Name: Tong Ying Yui Eric', (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65,  # print color text
                colourT, 2)

    cv2.imshow('MBS3523_Asn1dQ5', img)  # display img in window
    if cv2.waitKey(1) & 0xff == 27:  # wait 1ms and type Esc on keyboard
        break

cv2.destroyAllWindows()  # close all created windows