import cv2
print(cv2.__version__)  # check cv2 version

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # enable webcam capture and save to cam
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # set frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)  # set frame height
cam.set(cv2.CAP_PROP_FPS, 30)  # set fps = 30
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # set video format as MJPG

while True:
    _, frame = cam.read()  # start capture and save to frame

    cv2.imshow('MBS3523', frame)  # create window call MBS3523 and show captured image
    if cv2.waitKey(5) & 0xff == ord('q'):  # wait 5ms and type q on keyboard
        break

cam.release()  # release resources
cv2.destroyAllWindows()  # close all created windows