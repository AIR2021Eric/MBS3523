import cv2
import random
import math

print(cv2.__version__)  # check cv2 version

# define frame width and frame height
width = 640
height = 480

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # enable webcam capture and save to cam
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # set frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # set frame height
cam.set(cv2.CAP_PROP_FPS, 30)  # set fps = 30
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # set video format as MJPG

# define square moving speed, square size
# generate random degree between 15-75 degree, random square colour and random text colour
# define variables x,dx,y,dy with use of the variables above
speed = 15
sqSize = 80
degree = random.randint(15,75)
colourSq = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
colourTxt = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
x = random.randint(0, 640 - sqSize)
dx = int(speed*math.cos(math.radians(degree)))
y = random.randint(0, 480 - sqSize)
dy = int(-speed*math.sin(math.radians(degree)))

while True:
    _, frame = cam.read()  # start capture and save to frame
    # print square and text on frame
    cv2.rectangle(frame, (x, y), (x + sqSize, y + sqSize), colourSq, 2)
    cv2.putText(frame, 'MBS3523 Assignment 1b - Q3  Name: Tong Ying Yui Eric', (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, colourTxt, 2)

    # update next point
    x += dx
    y += dy

    # the square bounces back, generate next random square and text colour when touching the boundary
    if x >= width - sqSize or x <= 0:
        dx *= (-1)
        colourSq = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colourTxt = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if y >= height - sqSize or y <= 0:
        dy *= (-1)
        colourSq = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colourTxt = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    cv2.imshow('MBS3523_Asn1bQ3', frame)  # create window call MBS3523 and show captured image
    if cv2.waitKey(5) & 0xff == ord('q'):  # wait 5ms and type q on keyboard
        break

cam.release()  # release resources
cv2.destroyAllWindows()  # close all created windows