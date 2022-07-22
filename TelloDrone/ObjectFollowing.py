from djitellopy import Tello
import numpy as np
import cvzone
import cv2
import KeyboardControlModule
from ObjectRecognitionModule import *
from balltrackingmod import balltracking
from obrecognitionclass import balldetect

running = True
data = []
bt = balltracking()
bd = balldetect()


drone = Tello()
drone.connect()
drone.for_back_velocity = 0
drone.left_right_velocity = 0
drone.up_down_velocity = 0
drone.yaw_velocity = 0
drone.speed = 0
drone.streamoff()
drone.streamon()




fbrange = [600, 800]
lrrange = [500, 900]
udrange = [500, 900]

global data





print(drone.get_battery())

while True:
    while running == True:
        global data
        frame_read = drone.get_frame_read()
        myFrame = frame_read.frame
        correctDetection = bd.balldetect()
        data = bt.GetPos()
        x = data[0]
        y = data[1]
        z = data[2]

        if y < udrange[0]:
            drone.up_down_velocity = 30
        elif y > udrange[1]:
            drone.up_down_velocity = -30
        elif x < lrrange[0]:
            drone.yaw_velocity = 30
        elif x > lrrange[1]:
            drone.yaw_velocity = -30
        elif z < fbrange[0]:
            drone.for_back_velocity = 30
        elif z > fbrange[1]:
            drone.for_back_velocity = -30
        else:
            drone.for_back_velocity = 0
            drone.left_right_velocity = 0
            drone.yaw_velocity = 0
            drone.up_down_velocity = 0

        if drone.send_rc_control:
            drone.send_rc_control(drone.left_right_velocity, drone.for_back_velocity, drone.up_down_velocity, drone.yaw_velocity)


















