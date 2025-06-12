# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget, QVBoxLayout

from instr import *
from second_win import *

class ThirdWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        
        self.exp = exp
        
        self.set_appear()
        self.initUI()
        
        self.show()
        

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


    def initUI(self):
        self.mainLayoutV = QVBoxLayout()
        
        self.txt_heart_result = QLabel(txt_workheart + self.result())
        self.txt_result = QLabel(txt_index + str(self.index))
        
        self.mainLayoutV.addWidget(self.txt_result, alignment = Qt.AlignCenter)
        self.mainLayoutV.addWidget(self.txt_heart_result, alignment = Qt.AlignCenter)

        self.setLayout(self.mainLayoutV)

    def result(self):
        self.index = ruffie_test(self.exp.test1, self.exp.test2, self.exp.test3)
        
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res[0]
            elif self.index >= 11:
                return txt_res[1]
            elif self.index >= 6:
                return txt_res[2]
            elif self.index >= 0.5:
                return txt_res[3]
            else:
                return txt_res[4]
        
        if self.exp.age >= 13:
            if self.index >= 16.5:
                return txt_res[0]
            elif self.index >= 12.5:
                return txt_res[1]
            elif self.index >= 7.5:
                return txt_res[2]
            elif self.index >= 2:
                return txt_res[3]
            else:
                return txt_res[4]
        
        if self.exp.age >= 11:
            if self.index >= 18:
                return txt_res[0]
            elif self.index >= 14:
                return txt_res[1]
            elif self.index >= 9:
                return txt_res[2]
            elif self.index >= 3.5:
                return txt_res[3]
            else:
                return txt_res[4]
        
        if self.exp.age >= 9:
            if self.index >= 19.5:
                return txt_res[0]
            elif self.index >= 15.5:
                return txt_res[1]
            elif self.index >= 10.5:
                return txt_res[2]
            elif self.index >= 5:
                return txt_res[3]
            else:
                return txt_res[4]
        
        if self.exp.age == 7:
            if self.index >= 21:
                return txt_res[0]
            elif self.index >= 17:
                return txt_res[1]
            elif self.index >= 12:
                return txt_res[2]
            elif self.index >= 6.5:
                return txt_res[3]
            else:
                return txt_res[4]
        