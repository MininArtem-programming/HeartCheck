# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget

from instr import *

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.mainLayoutH = QHBoxLayout()
        
    def connects(self):
        pass

    def initUI(self):
        self.txt_line_name = QLabel(txt_name)
        self.edit_line_name = QLineEdit(txt_hintname)