import socket
# from inputs import devices
import xinput

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
command = bytearray()

send_command(command)
# command = bytearray()
#move down command
command.append(0x81)
command.append(0x01)
command.append(0x06)
command.append(0x01)
command.append(0x01)
command.append(0x14)
command.append(0x03)
command.append(0x02)
command.append(0xff)

send_command(command)
command2 = bytearray()
# print(command)


#Move Home
command.append(0x81)
command.append(0x01)
command.append(0x06)
command.append(0x04)
command.append(0xff)
# connect_socket()
send_command(command2)