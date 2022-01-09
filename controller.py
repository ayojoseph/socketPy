# socketTest.py>
# atem.py>

from socketTest import *
from atem import *
import xinput
from operator import itemgetter, attrgetter
import ctypes
import sys
import time
from operator import itemgetter, attrgetter
from itertools import count, starmap
from pyglet import event

camera_IP = '192.168.1.246'
switcher_IP = '192.168.1.215'
"""
Grab 1st available gamepad, logging changes to the screen.
L & R analogue triggers set the vibration motor speed.
"""
def select_camera(camNum):
    if camNum == 1:
        print("Camera: ",camNum," Selected!")
        camera_IP = '192.168.1.243'
        create_socket(camera_IP)
        connect_socket()
    elif camNum == 2:
        print("Camera: ",camNum," Selected!")
        camera_IP = '192.168.1.246'
        create_socket(camera_IP)
        connect_socket()


joysticks = xinput.XInputJoystick.enumerate_devices()
device_numbers = list(map(attrgetter('device_number'), joysticks))

print('found %d devices: %s' % (len(joysticks), device_numbers))

if not joysticks:
    sys.exit(0)

j = joysticks[0]
print('using %d' % j.device_number)

battery = j.get_battery_information()
print(battery)

#connecting to camera and switcher
create_socket(camera_IP)
connect_socket()
connect_switcher(switcher_IP)

@j.event
def on_button(button, pressed):
    print('button', button, pressed)
    if (button == 9 and pressed):  #Change Camera
        select_camera(1)
    elif (button == 10 and pressed):    #Change Camera
        select_camera(2)
    elif (button == 2 and pressed):     #Move down
        move_down(7)
    elif (button == 2 and not pressed):
        move_stop()
    elif (button == 1 and pressed):     #Move up
        move_up(0)
    elif (button == 1 and not pressed):
        move_stop()
    elif (button == 3 and pressed):     #Move left
        move_left(0)
    elif (button == 3 and not pressed):
        move_stop()
    elif (button == 4 and pressed):     #Move right
        move_right(0)
    elif (button == 4 and not pressed):
        move_stop()
    elif (button == 16 and pressed):     #Zoom In
        zoom_in(0)
    elif (button == 16 and not pressed):
        zoom_stop()
    elif (button == 13 and pressed):     #Zoom Out
        zoom_out(0)
    elif (button == 13 and not pressed):
        zoom_stop()
    elif (button == 7 and pressed):     #Cut Transition
        cut_transition()
    elif (button == 8 and pressed):     #Auto Transition
        auto_transition()
    elif (button == 5 and pressed):     #Speed change
        auto_transition()

left_speed = 0
right_speed = 0

@j.event
def on_axis(axis, value):
    left_speed = 0
    right_speed = 0

    # print('axis', axis, value)
    if axis == "left_trigger":
        left_speed = value
    elif axis == "right_trigger":
        right_speed = value
    # j.set_vibration(left_speed, right_speed)

while True:
    j.dispatch_events()
    time.sleep(.01)