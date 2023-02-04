# socketTest.py>
# atem.py>

from socketTest import *
from atem import *
import xinput
from operator import itemgetter, attrgetter
import ctypes
import sys
import time
import struct
from operator import itemgetter, attrgetter
from itertools import count, starmap
from pyglet import event

camera_IP = '192.168.1.246'
switcher_IP = '192.168.1.215'
speed_arr = ["0x02","0x05","0x08"]
speed_str = speed_arr[0]
speed = int(speed_str, 16)
sp = 0x02
sp_num = 0
preview_arr = [2,3,4]
preview_num = 0
# print(type(int(speed_str,16)))
print("HUH: ",int(speed_str,16))
# print(type(sp))
"""
Grab 1st available gamepad, logging changes to the screen.
L & R analogue triggers set the vibration motor speed.
"""
def change_speed():
    global sp_num
    sp_num += 1
    speed_str = speed_arr[sp_num % 3]
    global speed
    speed = int(speed_str, 16)
    print("SPEED: ",speed)

def change_preview():
    global preview_num
    preview_num += 1
    setPreview(preview_arr[preview_num % 3])

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
        move_down(speed)
    elif (button == 2 and not pressed):
        move_stop()
    elif (button == 1 and pressed):     #Move up
        move_up(speed)
    elif (button == 1 and not pressed):
        move_stop()
    elif (button == 3 and pressed):     #Move left
        move_left(speed)
    elif (button == 3 and not pressed):
        move_stop()
    elif (button == 4 and pressed):     #Move right
        move_right(speed)
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
    # elif (button == 15 and pressed):     #Focus Near
        # focus_near(0)
    elif (button == 15 and not pressed):
        # focus_stop()
        select_camera(1)
    elif (button == 14 and pressed):     #Focus Far
        # focus_far()
        select_camera(2)
    elif (button == 7 and pressed):     #Cut Transition
        cut_transition()
    elif (button == 8 and pressed):     #Auto Transition
        auto_transition()
    elif (button == 5 and pressed):     #Speed change
        # auto_transition()
        change_preview()
    elif (button == 6 and pressed):     #Downstream change
        # downstream_transition()
        # setPreview(1)
        change_speed()
    elif (button == 10 and pressed):     #Speed change
        focus_near()
    elif (button == 9 and pressed):     #Downstream change
        focus_far()

left_speed = 0
right_speed = 0

@j.event
def on_axis(axis, value):
    left_speed = 0
    right_speed = 0

    print('axis', axis, value)
    if axis == "left_trigger":
        # left_speed = hex(struct.unpack('<Q', struct.pack('<d', value))[0])
        left_speed = "0x" + str(round(value,1))
        new_left_sp = left_speed.replace('.','')
        # print("Left: ",new_left_sp)
        # move_down(int(new_left_sp,16))
    elif axis == "right_trigger":
        right_speed = "0x" + str(round(value,1))
        new_right_sp = right_speed.replace('.','')
        # print("Left: ",new_right_sp)
        # move_up(int(new_right_sp,16))
    elif axis == "l_thumb_x":
        pan_speed = "0x" + str(round(abs(value),1))
        pan_speed = pan_speed.replace('.','')
        print("PAN Speed: ",pan_speed)
        # if value > 0.1:
            # move_right(int(pan_speed,16))
        # elif value < -0.1:
            # move_left(int(pan_speed,16))
        # else:
            # move_stop()
    elif axis == "l_thumb_y":
        tilt_speed = "0x" + str(round(abs(value),1))
        tilt_speed = tilt_speed.replace('.','')
        print("TILT Speed: ",tilt_speed)
        # if value > 0.1:
            # move_up(int(tilt_speed,16))
        # elif value < -0.1:
            # move_down(int(tilt_speed,16))
        # else:
            # move_stop() 
    # j.set_vibration(left_speed, right_speed)

# while True:
#     j.dispatch_events()
#     time.sleep(.01

def main():
    while True:
        j.dispatch_events()
        time.sleep(.01)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Closing App")
        disconnect_switcher()
        sys.exit(0)