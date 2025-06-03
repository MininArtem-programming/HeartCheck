# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout

from instr import *
from final_win import *

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
        
        
    def connects(self):
        self.btn_send_results.clicked.connect(self.next_clicked)

    def initUI(self):
        self.mainLayoutH = QHBoxLayout()
        self.mainLayoutV1 = QVBoxLayout()
        self.mainLayoutV2 = QVBoxLayout()

        self.txt_line_name = QLabel(txt_name)
        self.edit_line_name = QLineEdit()
        self.edit_line_age = QLineEdit()
        self.txt_age = QLabel(txt_age)
        self.edit_age = QLineEdit()
        self.txt_first_hint = QLabel(txt_test1)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.edit_pulse1 = QLineEdit()
        self.txt_second_hint = QLabel(txt_test2)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.txt_third_hint = QLabel(txt_test3)
        self.btn_test3 = QPushButton(txt_starttest3)
        self.edit_pulse_before = QLineEdit()
        self.edit_pulse_after = QLineEdit()
        self.btn_send_results = QPushButton(txt_sendresults)

        self.timer = QLabel(txt_timer)


        self.mainLayoutV1.addWidget(self.txt_line_name, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.edit_line_name, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.edit_line_age, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.txt_age, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.edit_age, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.txt_first_hint, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.edit_pulse1, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.txt_second_hint, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.txt_third_hint, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.edit_pulse_before, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.edit_pulse_after, alignment = Qt.AlignLeft)
        self.mainLayoutV1.addWidget(self.btn_send_results, alignment = Qt.AlignCenter)
        
        self.mainLayoutV2.addWidget(self.timer, alignment = Qt.AlignCenter)



        self.edit_line_name.setPlaceholderText(txt_hintname)
        self.edit_line_age.setPlaceholderText('0')
        self.edit_age.setPlaceholderText('0')
        self.edit_pulse1.setPlaceholderText('0')
        self.edit_pulse_before.setPlaceholderText('0')
        self.edit_pulse_after.setPlaceholderText('0')

        self.mainLayoutH.addLayout(self.mainLayoutV1)
        self.mainLayoutH.addLayout(self.mainLayoutV2)

        self.setLayout(self.mainLayoutH)
        
    def next_clicked(self):
        self.hide()
        self.tw = ThirdWin()

#app = QApplication([])
#sw = SecondWin()
