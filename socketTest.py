import socket
# from input import devices
# import xinput
speed_default = 0x02


def move_home():
    cmd = bytearray()
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x04)
    cmd.append(0xff)
    return cmd

def move_down(speed):
    cmd = bytearray()
    # print(tilt.to_bytes(2,'little'))
    # speed = '0x'+tilt
    #move down command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(0x01)
    #tilt speed
    cmd.append(speed)
    

    cmd.append(0x03)
    cmd.append(0x02)
    cmd.append(0xff)
    # print(cmd)
    send_command(cmd)
    # return cmd

def move_up(speed):
    cmd = bytearray()
    #move up command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(0x01)
    #tilt speed
    cmd.append(speed)

    cmd.append(0x03)
    cmd.append(0x01)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd


def move_left(speed):
    cmd = bytearray()
    #move left command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(speed)
    #tilt speed
    cmd.append(0x01)

    cmd.append(0x01)
    cmd.append(0x03)
    cmd.append(0xff)
    
    send_command(cmd)
    # return cmd

def move_right(speed):
    cmd = bytearray()
    #move right command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(speed)
    #tilt speed
    cmd.append(0x14)

    cmd.append(0x02)
    cmd.append(0x03)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd

def zoom_in(speed):
    cmd = bytearray()
    #Zoom in
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x04)
    cmd.append(0x07)
    cmd.append(0x02)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd


def zoom_out(speed):
    cmd = bytearray()
    #Zoom out
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x04)
    cmd.append(0x07)
    cmd.append(0x03)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd

def zoom_stop():
    cmd = bytearray()
    #Zoom out
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x04)
    cmd.append(0x07)
    cmd.append(0x00)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd

def focus_near():
    cmd = bytearray()
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x04)
    cmd.append(0x08)
    cmd.append(0x03)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd

def focus_far():
    cmd = bytearray()
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x04)
    cmd.append(0x08)
    cmd.append(0x02)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd

def focus_stop():
    cmd = bytearray()
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x04)
    cmd.append(0x07)
    cmd.append(0x00)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd

def move_stop():
    cmd = bytearray()
    #move stop command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(0x01)
    #tilt speed
    cmd.append(0x01)

    cmd.append(0x03)
    cmd.append(0x03)
    cmd.append(0xff)

    send_command(cmd)
    # return cmd

def create_socket(camip):
    try:
        global s
        global host
        global port

        s = socket.socket()
        host = camip
        port = 5678
    except socket.error as msg:
        print("Socket Creation Error: "+str(msg))

def connect_socket():
    try:
        global s
        global host
        global port
        print("Connecting to Port")
        s.connect((host,port))
        addr, mess = s.getpeername()
        # s.listen(5)
        print("Connection good: "+str(addr))
    except socket.error as msg:
        print("Socket Connection Error: "+ str(msg))
        

def send_command(cmd):
    try:
        # print("Sending cmd...")
        s.send(cmd)
        # print("Command Sent!")
        # s.close()
    except socket.error as msg:
        print("Send command Error: "+str(msg))


# create_socket()
# connect_socket()
# command = move_home()

# send_command(command)
# command = bytearray()


# send_command(command)
# command2 = move_down(0,0)
# print(command)


#Move Home

# connect_socket()
# send_command(command2)
