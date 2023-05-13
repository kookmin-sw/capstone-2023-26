from drone_info import DroneInfo
import time
import threading

class Drone:
    def __init__(self):
        # 매 분의 n초마다 서버로 데이터 전송
        self.msg_to_server_interval = 10
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
            print(self.target_drone_info.get_attitude())
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
            print(f'execute! {time.strftime('%Y-%m-%d', current_time)}')
            # target_idx = int(current_time.tm_sec / self.msg_to_server_interval)
            self.send_msg_to_server('test')
            # print(current_time.tm_sec / self.msg_to_server_interval)

    def send_msg_to_server(self, msg):
        pass

if __name__=="__main__":
    drone_main = Drone()
    drone_main.drone_main()

    # main 루프가 종료되면 update문도 함께 종료됨.
    time.sleep(10)