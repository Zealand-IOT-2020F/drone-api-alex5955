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
        print("Sent command: " + command)

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
        self.sendCommand("forward " + amount)

    def back(self, amount):
        self.sendCommand("back " + amount)

    def rotateCW(self,x):
        self.sendCommand("cw" + x)

    def rotateCCW(self,x):
        self.sendCommand("ccw" + x)

    def printinfo(self):
        print("Hallo Drone at : IP:" + self.ip + " Port: " + self.port)

    def left(self, amount):
        self.sendCommand("left " + amount)
    
    def right(self, amount):
        self.sendCommand("right " + amount)
