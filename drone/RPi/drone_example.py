###################
from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
import time
import socket
import math
import argparse
####################

def connectMyCopter():
        vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)

        print ("version: %s" % vehicle.version)
        print ("Global location : %s" % vehicle.location.global_frame)
        print ("Local location : %s" % vehicle.location.local_frame)
        print ("Attitude : %s" % vehicle.attitude)

        return vehicle

def arm():
        print ("try Arming")
        time.sleep(2)

        vehicle.armed=True
        while vehicle.armed==False:
                print("Waiting for drone to become armed..")
                time.sleep(1)
                vehicle.armed=True

        print("Vehicle is now armed.")
        print("OMG props ars spinning!")

        return None

################

vehicle = connectMyCopter()
arm()

# '@vehicle.on_attribute()'는 드론의 속성값이 변경될 때마다 호출되는 콜백 함수를 등록하는 함수
@vehicle.on_attribute('attitude')
def attitude_listener(self, name, msg):
        print ("%s attribute is : %s" % (name, msg))
        # return None

while True:
        attitude_listener

print ("End of script.")
