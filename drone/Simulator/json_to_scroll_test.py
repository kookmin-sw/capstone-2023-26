import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel
import json

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON 데이터 스크롤 뷰")
        self.layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)
        
        self.load_data()
    
    def load_data(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        
        for item in data:
            label = QLabel()
            label.setText(f"ID: {item['id']} | Time: {item['time']} | Voltage: {item['voltage']}")
            self.scroll_layout.addWidget(label)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
