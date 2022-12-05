import socket
import time

def sendCommand(s, content):
    content += '\r\n'
    s.sendall(content.encode())
x = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#your swtich ip here
s.connect(("172.20.10.5", 6000))
#how many times to run
val = 3
#how long you want to wait for people to join in seconds
rQueue = 60
#how long to assume users will take for raid completion be generous in seconds
rTime = 60

while x < val:
    sendCommand(s, "click A")
    print('opens raid menu')
    time.sleep(1.5)
    sendCommand(s, "click A")
    print('challenge as group')
    time.sleep(2)
    sendCommand(s, "click A")
    print('link code')
    time.sleep(10)
    sendCommand(s, "click A")
    print('ready up')
    #time  to get everyone in
    time.sleep(rQueue)
    sendCommand(s, "click A")
    print('start raid')
    #time to load into raid
    time.sleep(10)
    #time to finish raid
    time.sleep(rTime)
    sendCommand(s, "click DDOWN")
    print('dont catch')
    time.sleep(1)
    sendCommand(s, "click A")
    print('Complete raid')
    time.sleep(7.5)
    sendCommand(s, "click A")
    time.sleep(15)
    time.sleep(5)
    print('Home menu')
    sendCommand(s, "click HOME")
    time.sleep(1)
    sendCommand(s, "click X")
    print('opens close game menut')
    time.sleep(.5)
    sendCommand(s, "click A")
    print('closes game')
    time.sleep(4)
    sendCommand(s, "click A")
    print('opens user menu')
    time.sleep(1)
    sendCommand(s, "click A")
    print('Picks default user')
    time.sleep(22)
    sendCommand(s, "click A")
    print('Starts games')
    time.sleep(22)
    sendCommand(s, "click X")
    print('Opens Menu')
    time.sleep(.75)
    sendCommand(s, "click L")
    print('Connects to Internet')
    #more time for slower connectiosn
    time.sleep(20)
    sendCommand(s, "click A")
    print('connected?')
    time.sleep(1)
    sendCommand(s, "click B")
    print('Closes menu')
    time.sleep(3)
    x = x+1
