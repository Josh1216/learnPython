from TC100cotrol import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from fake_connect import initial,servo_on,servo_off,designatedLocation
global servo
servo=0

def servoOnOff(): #伺服開關顯示
    global servo
    if servo==0:
        ui.label_2.setText("on")
        servo_on()
        servo=1
    else:
        ui.label_2.setText("off")
        servo_off()
        servo=0

def turnToZero(): #原點賦歸
    global servo
    if servo==0:
        ui.label_8.setText("賦歸完成")
        initial()
    else:
        ui.label_8.setText("請開啟servo")

def useTarget():
    userInput = ui.lineEdit.text
    designatedLocation(desloc)

        




app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.servoOnOff.clicked.connect(servoOnOff)
ui.turnToZero.clicked.connect(turnToZero)
ui.inPut.clicked.connect(useTarget)

widget.show()
app.exec_()