from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QMainWindow()

    # 현재 스크립트 파일의 디렉토리 경로를 가져오기
    script_path = os.path.dirname(os.path.abspath(__file__))

    # UI 파일의 절대 경로 구성
    ui_file = os.path.join(script_path, 'testqt.ui')

    uic.loadUi(ui_file, MainWindow)

    MainWindow.show()
    app.exec()