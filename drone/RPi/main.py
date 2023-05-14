from drone_info import DroneInfo
import time
from datetime import datetime

import threading

import requests
import json

class Drone:
    def __init__(self):
        # 매 분의 n초마다 서버로 데이터 전송
        self.msg_to_server_interval = 5
        # self.message_sent_status_list = [0] * int(60 / self.msg_to_server_interval)
        # print(self.message_sent_status_list)

        self.main_loop_interval = 1/30
        self.enabled = True

        self.target_drone_info = DroneInfo()

    def drone_main(self):
        
        # print(self.main_loop_interval)
        update_thread = threading.Thread(target=self.drone_update)
        sending_msg_thread = threading.Thread(target=self.sending_msg_update)

        update_thread.daemon = True
        sending_msg_thread.daemon = True

        update_thread.start()
        sending_msg_thread.start()

    def drone_update(self):
        while self.enabled:
            # print('drone-update')
            # print(self.target_drone_info.get_attitude())
            # self.evaluate_conditon_to_server()
            # print(time.localtime().tm_sec)

            time.sleep(self.main_loop_interval)    

    def sending_msg_update(self):
        while self.enabled:
            # print(time.localtime().tm_sec)
            self.evaluate_conditon_to_server()
            time.sleep(1)
        
    def evaluate_conditon_to_server(self):
        current_time = time.localtime()
        if current_time.tm_sec % self.msg_to_server_interval == 0:
            pos_json = self.target_drone_info.get_position()
            voltage = 11.1
            event_id = 1

            # data = {
            #     'time': "17:30:00",
            #     'coordinate': [0, 0],
            #     'voltage': 101.1,
            #     'event_id': 1
            # }

            url = 'http://13.209.19.200:8000/api/droneinfo/'
            data = {
                'time': time.strftime('%H:%M:%S', current_time),
                'coordinate': pos_json,
                'voltage': voltage,
                'event_id': event_id
            }

            self.send_msg_to_server(url, data)
            # response = requests.post(url, json=data)
            # print(response.status_code)

    def send_msg_to_server(self, url, params):
        response = requests.post(url, json=params)
        
        # response = requests.post(url, json=params)
        # print(response.url)

        print(response.status_code)
        # print(response.text)

if __name__=="__main__":
    drone_main = Drone()
    drone_main.drone_main()

    # main 루프가 종료되면 update문도 함께 종료됨.
    time.sleep(10)