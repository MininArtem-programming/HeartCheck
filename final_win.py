# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget, QVBoxLayout

from instr import *


class ThirdWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def connects(self):
        pass

    def initUI(self):
        self.mainLayoutV = QVBoxLayout()
        self.txt_result = QLabel(txt_index + '0')
        self.txt_heart_result = QLabel(txt_workheart)


        self.mainLayoutV.addWidget(self.txt_result, alignment = Qt.AlignCenter)
        self.mainLayoutV.addWidget(self.txt_heart_result, alignment = Qt.AlignCenter)

        self.setLayout(self.mainLayoutV)

    def result(self):
        
#app = QApplication([])
#tw = ThirdWin()
