from djitellopy import tello # The library that contains the functions to control the Drone
from time import sleep # wait function imported

drone = tello.Tello()
drone.connect() # connecting to drone *needs to connect to the drone's wifi first*

print(drone.get_battery()) # Battery percentage

drone.takeoff() # Drone launch
# drone.move_forward(30)
drone.send_rc_control(0, 20, 0, 0) # RC controls to 1: left-right, 2: forwards-backwards, 3: up-down, 4: yaw
sleep(2)#wait for 2 seconds
drone.send_rc_control(20, 0, 0, 0)
sleep(2)
drone.land() # Land the drone



