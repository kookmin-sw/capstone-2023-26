from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
import time
import socket
import math
import argparse

class DroneInfo:
    def __init__(self):
        print('ditto_firmware is connecting to drone')
        self.vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)

        print('connected!')

        print ("version: %s" % self.vehicle.version)
        print ("Global location : %s" % self.vehicle.location.global_frame)
        print ("Local location : %s" % self.vehicle.location.local_frame)
        

    def get_attitude(self):
        return self.vehicle.attitude
        

    def get_position(self):
        # self.vehicle.gps_0.
        pass

    def get_groundspeed(self):
        return self.vehicle.groundspeed