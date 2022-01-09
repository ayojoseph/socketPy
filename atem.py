import PyATEMMax
switcher = PyATEMMax.ATEMMax()

# Connect
# switcher.connect("192.168.1.215")
# switcher.waitForConnection()

# Have fun!
# switcher.setAudioMixerMasterVolume(0.0)    # Set Master Volume: 1.8dB
# switcher.setPreviewInputVideoSource(0, 3)

def cut_transition():
    switcher.execCutME(0)

def auto_transition():
    switcher.execAutoME(0)
    

# cut_transition()

def connect_switcher(addr):
    try:
        print('Connecting to Atem Switcher...')
        switcher.connect(addr)
        switcher.waitForConnection(infinite=False)
        print('Connection Success')
    except switcher.error as msg:
        print("Connection to Atem Issue")


def disconnect_switcher():
    try:
        print('Connecting to Atem Switcher...')
        switcher.disconnect()
        # switcher.waitForConnection()
        print('Connection Success')
    except switcher.error as msg:
        print("Connection to Atem Issue")

# connect_switcher('192.168.1.215')
# cut_transition()
# disconnect_switcher()