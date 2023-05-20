from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QPushButton, QLabel, QSizePolicy, QGridLayout, QFileDialog, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtGui import QImage, QPixmap

import threading
import time
import json

import utils.utils_ui
import networking.ditto_networking
import networking.ivs_rtmp
from networking.ditto_networking import Networking

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

         # 매 분의 n초마다 서버로 데이터 전송
        self.msg_to_server_interval = 5

        self.ditto_backend_url = "http://13.125.5.137:8000"
        self.rtmp_url = None # 보안 상의 이유로 rtmp url은 지웠습니다.
        self.networking = Networking()

        self.setWindowTitle("Drone Simulator")
        self.resize(800, 600)

        # 메인 위젯 설정
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 전체 레이아웃
        main_layout = QVBoxLayout(main_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 가로로 길쭉한 입력 필드
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("ex)")
        self.input_field.setText(self.ditto_backend_url)
        main_layout.addWidget(self.input_field)
        # grid_layout.addWidget(input_field, 0, 0, 1, 2)  # 2열로 확장

        # 'connect' 버튼
        connect_button = QPushButton("Validate")
        connect_button.clicked.connect(self.connection_check)
        # grid_layout.addWidget(connect_button, 0, 2)  # 다음 열에 배치
        
        head_layout = QHBoxLayout()
        head_layout.addWidget(self.input_field)
        head_layout.addWidget(connect_button)
        
        main_layout.addLayout(head_layout)
        # main_layout.addWidget(connect_button)
        # main_layout.addLayout(head_horizontal_layout)

        # 가로로 4등분하는 레이아웃 
        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 좌측 영역
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 이미지 라벨 (예시용)
        self.image_label = QLabel("Image")
        left_layout.addWidget(self.image_label)

        # Upload 버튼
        self.video_upload_button = QPushButton("Select Video", self)
        self.video_upload_button.clicked.connect(self.select_video)
        left_layout.addWidget(self.video_upload_button)

        self.json_upload_button = QPushButton("Select Json", self)
        self.json_upload_button.clicked.connect(self.select_json)
        left_layout.addWidget(self.json_upload_button)

        grid_layout.addWidget(left_widget, 0, 0)



        # 우측 영역
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        # 스크롤 뷰
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)

        # # 버튼 추가
        # for i in range(10):
        #     button = QPushButton(f"Button {i+1}")
        #     scroll_layout.addWidget(button)

        scroll_area.setWidget(scroll_content)
        right_layout.addWidget(scroll_area)

        grid_layout.addWidget(right_widget, 0, 1)

        main_layout.addLayout(grid_layout)

        # === 하단 영역 ===
        # status_label = QLabel("Not Validated")
        # self.statusBar().addPermanentWidget(status_label)

        # 좌측 패딩 추가
        left_padding = QWidget()
        left_padding.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.statusBar().insertPermanentWidget(0, left_padding)
        # ===

        # status bar에 추가할 위젯이 있다면 여기에 추가


        # 우측 패딩 추가
        right_padding = QWidget()
        right_padding.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.statusBar().insertPermanentWidget(2, right_padding)
        # ===

         # 상태 원 표시를 위한 QLabel
        self.status_icon = QLabel()
        self.status_icon.setFixedSize(10, 10)
        self.status_icon.setStyleSheet("border-radius: 5px; background-color: red;")
        self.statusBar().addWidget(self.status_icon)

        # 하단 영역
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_data_to_server)
        self.statusBar().addPermanentWidget(send_button)

        # 중앙 하단 정렬
        self.statusBar().setSizeGripEnabled(False)
        # self.statusBar().setStyleSheet("QStatusBar::item {border: none;}") #border :3px solid black; padding: 100px;")

        # 스크롤 바 스타일 설정
        scroll_area.setStyleSheet(
            "QScrollArea {border: none;}"
            "QScrollBar:vertical {width: 15px;}"
            "QScrollBar::handle:vertical {background: #888888; border-radius: 7px;}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {background: none;}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: none;}"
        )

        # 스크롤 속도 조절
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)


    """
    functions
    """
    def select_video(self):
        file_dialog = QFileDialog()
        video_file, _ = file_dialog.getOpenFileName(
            self, "Select Video", "", "Video Files (*.mp4 *.avi *.mkv)")

        self.video_url = video_file

        if video_file:
            thumbnail_data = utils.utils_ui.generate_thumbnail(video_file)
            q_image = QImage(thumbnail_data[0], thumbnail_data[1], thumbnail_data[2], QImage.Format.Format_RGB888)
            thumbnail = QPixmap.fromImage(q_image)
            if thumbnail:
                self.image_label.setPixmap(thumbnail.scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio))

    def select_json(self):
        file_dialog = QFileDialog()
        json_file, _= file_dialog.getOpenFileName(
            self, "Select Json(Flight Data)", "", "Json File (*.json)")
        
        if json_file:
            self.load_data(json_file)

    def connection_check(self):
        # 불리언 값을 받아와서 상태 원 표시를 변경
        is_validated = self.networking.is_alive(self.ditto_backend_url + "/api/")

        if is_validated:
            # self.status_label.setText("Validated")
            self.status_icon.setStyleSheet("border-radius: 5px; background-color: green;")
        else:
            # self.status_label.setText("Not Validated")
            self.status_icon.setStyleSheet("border-radius: 5px; background-color: red;")

    def load_data(self, json_path):
        with open(json_path, "r") as file:
            self.flight_data = json.load(file)
        
        for item in self.flight_data:
            label = QLabel()
            label.setText(f"Time: {item['time']} | Voltage: {item['voltage']}")
            self.scroll_layout.addWidget(label)

    def send_data_to_server(self):
        sending_msg_thread = threading.Thread(target=self.sending_msg_update)
        sending_msg_thread.daemon = True
        sending_msg_thread.start()

        video_streaming_thread = threading.Thread(target=self.video_streaming_update)
        video_streaming_thread.daemon = True
        video_streaming_thread.start()

    def sending_msg_update(self):
        for i in range(len(self.flight_data)):
            
            # self.networking.send_msg_to_server_with_params(self.ditto_backend_url + "/api/droneInfo/", params=self.flight_data[i])
            current_time = time.localtime()
            self.flight_data[i]['time'] = time.strftime('%H:%M:%S', current_time)
            print(self.flight_data[i])
           
            self.networking.send_msg_to_server_with_params('http://13.125.5.137:8000/api/droneinfo/', self.flight_data[i])
            time.sleep(5)

    def video_streaming_update(self):
        networking.ivs_rtmp.send_video_to_rtmp_server(self.video_url, self.rtmp_url)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
