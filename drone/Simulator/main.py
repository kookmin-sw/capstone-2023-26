import subprocess
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
import cv2

"""
Todo
- 서버에 영상 스트리밍 할 때, 시작 시각을 직접 지정할 수 있게 해줘야(년원일시분초)
"""


class VideoThumbnailWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Thumbnail")
        self.setGeometry(100, 100, 300, 200)

        self.thumbnail_label = QLabel(self)
        self.thumbnail_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.select_button = QPushButton("Select Video", self)
        self.select_button.clicked.connect(self.select_video)

        layout = QVBoxLayout()
        layout.addWidget(self.thumbnail_label)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

    def select_video(self):
        file_dialog = QFileDialog()
        video_file, _ = file_dialog.getOpenFileName(
            self, "Select Video", "", "Video Files (*.mp4 *.avi *.mkv)")

        if video_file:
            thumbnail = self.generate_thumbnail(video_file)
            if thumbnail:
                self.thumbnail_label.setPixmap(thumbnail.scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio))

    def generate_thumbnail(self, video_file):
        # 여기에서 비디오 파일을 처리하여 썸네일을 생성하는 코드를 작성해야 합니다.
        # 이 예제에서는 썸네일 생성 부분은 비워두었습니다.
        # 썸네일 생성에는 OpenCV, FFmpeg 등의 라이브러리를 사용할 수 있습니다.
        # 비디오 파일을 처리하여 썸네일 이미지를 반환하는 함수를 작성해주세요.
        # thumbnail = your_thumbnail_generation_function(video_file)
        
        cap = cv2.VideoCapture(video_file)
        success, frame = cap.read()

        if success:
            # 첫 번째 프레임을 사용하여 썸네일 생성
            thumbnail = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            thumbnail = cv2.resize(thumbnail, (200, 150))
            thumbnail = QImage(thumbnail.data, thumbnail.shape[1], thumbnail.shape[0], QImage.Format.Format_RGB888)
            
            return QPixmap.fromImage(thumbnail)

        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VideoThumbnailWidget()
    widget.show()
    sys.exit(app.exec())
