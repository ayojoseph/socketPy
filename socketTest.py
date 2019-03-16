import socket
# from inputs import devices
# import xinput


def move_home():
    cmd = bytearray()
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x04)
    cmd.append(0xff)
    return cmd

def move_down(pan,tilt):
    cmd = bytearray()
    #move down command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(0x01)
    #tilt speed
    cmd.append(0x14)

    cmd.append(0x03)
    cmd.append(0x02)
    cmd.append(0xff)
    return cmd

def move_up(pan,tilt):
    cmd = bytearray()
    #move up command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(0x01)
    #tilt speed
    cmd.append(0x14)

    cmd.append(0x03)
    cmd.append(0x01)
    cmd.append(0xff)
    return cmd


def move_left(pan,tilt):
    cmd = bytearray()
    #move left command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(0x01)
    #tilt speed
    cmd.append(0x01)

    cmd.append(0x01)
    cmd.append(0x03)
    cmd.append(0xff)
    return cmd

def move_right(pan,tilt):
    cmd = bytearray()
    #move right command
    cmd.append(0x81)
    cmd.append(0x01)
    cmd.append(0x06)
    cmd.append(0x01)
    #pan speed
    cmd.append(0x01)
    #tilt speed
    cmd.append(0x14)

    cmd.append(0x02)
    cmd.append(0x03)
    cmd.append(0xff)
    return cmd

def move_stop(pan,tilt):
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
    return cmd

def create_socket():
    try:
        global s
        global host
        global port

        s = socket.socket()
        host = '192.168.2.243'
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
        print("Sending cmd...")
        s.send(cmd)
        print("Command Sent!")
        # s.close()
    except socket.error as msg:
        print("Send command Error: "+str(msg))


create_socket()
connect_socket()
command = move_home()

# send_command(command)
# command = bytearray()


send_command(command)
command2 = move_down()
# print(command)


#Move Home

# connect_socket()
send_command(command2)

