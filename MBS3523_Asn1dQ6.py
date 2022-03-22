import cv2
import random

# define frame width and frame height
width = 640
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # enable webcam capture and save to cam
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # set frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # set frame height

# initialize variables
EVT = 0
pt1 = pt2 = (0,0)
colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# define function ROI
def ROI(event, x, y, flags, param):
    global EVT, pt1, pt2, colour    # make variables global

    # save point coordinate and update EVT when Left BUTTON is DOWN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"L btn down Event = {event} at point {x} {y}")
        EVT = event
        pt1 = (x, y)

    # save point coordinate and update EVT when Left BUTTON is UP
    if event == cv2.EVENT_LBUTTONUP:
        print(f"L btn down Event = {event} at point {x} {y}")
        EVT = event
        pt2 = (x, y)
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))   # update text colour

    # update EVT when Right BUTTON is UP
    if event == cv2.EVENT_RBUTTONUP:
        EVT = event
        print(f"R btn up   Event = {event}")


cv2.namedWindow('MBS3523_Asn1dQ6')      # create window MBS3523_Asn1dQ6
cv2.setMouseCallback('MBS3523_Asn1dQ6', ROI)    # set mouse call back with use of function ROI

cam = cv2.VideoCapture(0)   # enable webcam capture and save to cam

while True:
    _, img = cam.read() # start capture and save to img
    cv2.putText(img, 'MBS3523 Assignment 1d - Q6  Name: Tong Ying Yui Eric', (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65,  # print coloured text
                colour, 2)

    # when Left BUTTON is DOWN
    if EVT == 1:
        # if imgcrop window exist, change previous imgcrop to gray and update imgcrop
        if cv2.getWindowProperty('imgcrop', cv2.WND_PROP_VISIBLE) == 1.0:
            imgcrop[:,:] = 65
            cv2.imshow('imgcrop', imgcrop)

    # when Left BUTTON is UP, Left BUTTON was previously DOWN
    if EVT == 4:
        # if there are 2 different points with both at different column and row
        # draw rectangle with the 2 points and crop image, then update imgcrop
        if (pt1 != pt2) and (pt1[0] != pt2[0]) and (pt1[1] != pt2[1]):
            img = cv2.rectangle(img, pt1, pt2, (0, 125, 125), 5)
            imgcrop = img[min(pt1[1], pt2[1]): max(pt1[1], pt2[1]), min(pt1[0], pt2[0]):max(pt1[0], pt2[0])]
            cv2.imshow('imgcrop',imgcrop)

    # when Right BUTTON is UP
    if EVT == 5:
        # if imgcrop window exist, destroy imgcrop window
        if cv2.getWindowProperty('imgcrop',cv2.WND_PROP_VISIBLE) == 1.0:  # if imgcrop window exist
            cv2.destroyWindow('imgcrop')
        EVT = 0  # reset EVT

    cv2.imshow('MBS3523_Asn1dQ6', img)  # display img in window
    if cv2.waitKey(1) & 0xff == 27: break   # wait 1ms and type Esc on keyboard
cv2.destroyAllWindows()     # close all created windows