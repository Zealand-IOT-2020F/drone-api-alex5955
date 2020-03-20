import socket
import time

class Drone(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip,self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendCommand("command")    

    def sendCommand(self, command):
        self.sock.sendto(command.encode(), (self.address))
        #data = self.sock.recvfrom(1518)
        #print(data.decode(encoding="utf-8"))
        print("Sent message: " + command)

    def takeOff(self):
        self.sendCommand("takeoff")

    def land(self):
        self.sendCommand("land")

    def battery(self):
        self.sendCommand("battery?")

    def end(self):
        print("close")
        self.sock.close()
        
    def forward(self, amount):
        self.sendCommand("forward " + str(amount))

    def back(self, amount):
        self.sendCommand("back " + str(amount))

    def rotateCW(self,amount):
        self.sendCommand("cw" + str(amount))

    def rotateCCW(self,amount):
        self.sendCommand("ccw" + str(amount))

    def printinfo(self):
        print("Hallo Drone at : IP:" + str(self.ip) + " Port: " + str(self.port))

    def left(self, amount):
        self.sendCommand("left " + str(amount))
    
    def right(self, amount):
        self.sendCommand("right " + str(amount))
