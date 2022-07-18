from djitellopy import tello# The library that contains the functions to control the Drone
import cv2 # Computer Vision lIbrary

drone = tello.Tello() # connecting to Tello Drone *Needs to be connected it its wifi first*
drone.connect()

print(drone.get_battery())

drone.streamon() # sending drone video to PC

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360, 240)) # defining the window frame size
    cv2.imshow("Image", img) # opening up the window to show the drone's camera and titling it
    cv2.waitKey(1) # pause
