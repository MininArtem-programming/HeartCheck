from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QListWidget

from instr import *
from second_win import *

class FirstWin(QWidget):
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

    def connects(self):
        self.btn.clicked.connect(self.next_clicked)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.btn = QPushButton(txt_next)
        self.mainLayoutV = QVBoxLayout()
        self.mainLayoutV.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.mainLayoutV.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.mainLayoutV.addWidget(self.btn, alignment = Qt.AlignCenter)
        self.setLayout(self.mainLayoutV)

    def next_clicked(self):
        self.hide()
        self.sw = SecondWin()




app = QApplication([])
mw = FirstWin()
app.exec_()
