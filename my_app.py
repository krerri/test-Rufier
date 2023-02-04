from instr import*
from second_win import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QApplication, QWidget, QVBoxLayout, QPushButton)


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apperar()
        self.initUI()
        self.connects()
    def set_apperar(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton (txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)       
    def connects(self):
        self.button.clicked.connekt(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
my_win = MainWin()
app.exec_()
