from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QPushButton, QLabel, QSizePolicy, QGridLayout, QFileDialog, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtGui import QImage, QPixmap

import utils_ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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
        self.input_field.setText("http://13.125.5.137:8000")
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
        left_layout.addWidget(self.json_upload_button)

        grid_layout.addWidget(left_widget, 0, 0)



        # 우측 영역
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        # 스크롤 뷰
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # 버튼 추가
        for i in range(10):
            button = QPushButton(f"Button {i+1}")
            scroll_layout.addWidget(button)

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
        self.statusBar().addPermanentWidget(send_button)

        # 중앙 하단 정렬
        self.statusBar().setSizeGripEnabled(False)
        self.statusBar().setStyleSheet("QStatusBar::item {border: none;}") #border :3px solid black; padding: 100px;")

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

    def select_video(self):
        file_dialog = QFileDialog()
        video_file, _ = file_dialog.getOpenFileName(
            self, "Select Video", "", "Video Files (*.mp4 *.avi *.mkv)")

        if video_file:
            thumbnail_data = utils_ui.generate_thumbnail(video_file)
            q_image = QImage(thumbnail_data[0], thumbnail_data[1], thumbnail_data[2], QImage.Format.Format_RGB888)
            thumbnail = QPixmap.fromImage(q_image)
            if thumbnail:
                self.image_label.setPixmap(thumbnail.scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio))

    def connection_check(self):
        

        # 불리언 값을 받아와서 상태 원 표시를 변경합니다.
        is_validated = True  # 여기에서 실제 불리언 값을 받아오는 로직을 작성해야 합니다.

        if is_validated:
            # self.status_label.setText("Validated")
            self.status_icon.setStyleSheet("border-radius: 5px; background-color: green;")
        else:
            # self.status_label.setText("Not Validated")
            self.status_icon.setStyleSheet("border-radius: 5px; background-color: red;")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
