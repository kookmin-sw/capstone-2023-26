from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
import time
import socket
import math
import argparse

import json

class DroneInfo:
    def __init__(self):
        print('ditto_firmware is connecting to drone')
        try:
            self.vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)

            print('connected!')

            print ("version: %s" % self.vehicle.version)
            print ("Global location : %s" % self.vehicle.location.global_frame)
            print ("Local location : %s" % self.vehicle.location.local_frame)
        except:
            self.vehicle = None
            print("can't connect to vehicle")
        

    def get_attitude(self):
        if self.vehicle:
            return self.vehicle.attitude
        else:
            return "{100, 200}"
        

    def get_position(self):
        # self.vehicle.gps_0.
        json_data = None
        if self.vehicle:
            # print(self.vehicle.gps_0)
            location_global = self.vehicle.location.global_frame
            data = {'lat':location_global.lat, 'lon': location_global.lon, 'alt':location_global.alt}
        else:
            data = {'x': 100, 'y': 200}
            json_data = json.dumps(data)

        return data


    def get_groundspeed(self):
        if self.vehicle:
            return self.vehicle.groundspeed
        else:
            return "10"
        # return self.vehicle.groundspeed