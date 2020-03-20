import drone
import time

drone1 = drone.Drone('192.168.10.1',8889)

#Info printed
drone1.battery()
drone1.printinfo()

#Takeoff Drone
drone1.takeOff()
time.sleep(2)

#Square routine

#Moving forward + rotating 90 degrees
drone1.forward(25)
time.sleep(2)
drone1.rotateCW("90")
time.sleep(2)

#
drone1.forward(25)
time.sleep(2)
drone1.rotateCW("90")
time.sleep(2)

#
drone1.forward(25)
time.sleep(2)
drone1.rotateCW("90")
time.sleep(2)

#
drone1.forward(25)
time.sleep(2)
drone1.rotateCW("90")
time.sleep(2)

# cross movement
drone1.forward(25)
time.sleep(2)
drone1.back(25)
time.sleep(2)
drone1.left(25)
time.sleep(2)
drone1.right(25)
time.sleep(2)
drone1.right(25)
time.sleep(2)
drone1.left(25)
time.sleep(2)
drone1.back(25)
time.sleep(2)
drone1.forward(25)
time.sleep(2)

#Land
drone1.battery()
drone1.printinfo()
drone1.land()

#end program
drone1.end()

