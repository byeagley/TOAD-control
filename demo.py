from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QHBoxLayout, QVBoxLayout, QGridLayout)
 
from PyQt5.QtCore import Qt
import sys
import json

parameters = {
        'power': 'off', 
        'mode': 'Ackermann',
        'forward speed': 0,
        'steering angle': 0,
        'turn speed': 50,
        'turning': False
        }

with open('output.txt', 'w') as json_file:
    json.dump(parameters, json_file, indent = len(parameters))


class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()

 
    def UI(self):

        def switchMode():
            if combo.currentText() == 'Ackermann':
                dial.setVisible(True)
                slider_label.setText("Forward speed")
                slider.setValue(0)
                dial.setValue(0)
                turnButton.setVisible(False)
                angle_label.setVisible(True)
            if combo.currentText() == 'Turn in Place':
                dial.setVisible(False)
                slider_label.setText("Turn speed")
                slider.setValue(50)
                turnButton.setVisible(True)
                angle_label.setVisible(False)
        
        def changeColor():
            if button.isChecked():
                button.setStyleSheet("background-color : green")
            else:
                button.setStyleSheet("background-color : red")

        def speedDisplay(speed):
            speed_label.setText(str(speed))
        
        def angleDisplay(angle):
            angle_label.setText(str(angle))

        def json_output():
            parameters['mode'] = combo.currentText()

            if combo.currentText() == 'Ackermann':
                parameters['forward speed'] = slider.value()
                parameters['steering angle'] = dial.value()
            elif combo.currentText() == 'Turn in Place':
                parameters['turn speed'] = slider.value()

            if turnButton.isDown():
                parameters['turning'] = True
            else:
                parameters['turning'] = False

            if button.isChecked():
                parameters['power'] = 'on'
            else:
                parameters['power'] = 'off'
            with open('output.txt', 'w') as json_file:
                json.dump(parameters, json_file, indent = len(parameters))
        
        # Turn in Place Button
        turnButton = QPushButton('Hold to Turn')
        turnButton.setVisible(False)
        turnButton.pressed.connect(json_output)
        turnButton.released.connect(json_output)

        # Power Button
        button = QPushButton('Power')
        button.setCheckable(True)
        button.clicked.connect(changeColor)
        button.clicked.connect(json_output)
        button.setMaximumWidth(50)
        button.setStyleSheet("background-color : red") 
        
        # Driving Mode Combo Box 
        combo = QtWidgets.QComboBox(self)
        combo.addItems(["Ackermann", "Turn in Place"])
        combo.currentIndexChanged.connect(switchMode)
        combo.currentIndexChanged.connect(json_output)

        # Angle Dial
        dial = QtWidgets.QDial(self)
        dial.setMinimum(-30)
        dial.setMaximum(30)
        dial.setNotchesVisible(True)
        dial.setNotchTarget(2)
        dial.move(270,300)
        dial.valueChanged.connect(angleDisplay)
        dial.valueChanged.connect(json_output)
        
        # Speed Slider
        slider = QtWidgets.QSlider(Qt.Vertical, self)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        slider.setTickInterval(10)
        slider.valueChanged.connect(speedDisplay)
        slider.valueChanged.connect(json_output)

        # Slider label    
        slider_label = QtWidgets.QLabel(self)
        slider_label.setWordWrap(True)
        slider_label.setText("Forward speed")

        # Speed label
        speed_label = QtWidgets.QLabel(self)
        speed_label.setText("0")
        speed_label.setStyleSheet('QLabel { background: #007AA5; border-radius: 3px;}')
        speed_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        speed_label.setFont(QtGui.QFont("Arial",25))

        # Angle Label
        angle_label = QtWidgets.QLabel(self)
        angle_label.setText("0")
        angle_label.setFont(QtGui.QFont("Arial",25))
        angle_label.setStyleSheet('QLabel { background: #007AA5; border-radius: 3px;}')
        angle_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)


        # Grid Layout Management 
        vbox = QGridLayout()
        vbox.addWidget(combo, 0, 2)
        vbox.addWidget(dial, 1, 2)
        vbox.addWidget(slider, 1, 0)
        vbox.addWidget(slider_label, 0, 0)
        vbox.addWidget(speed_label, 2, 0)
        vbox.addWidget(button, 2, 2)
        vbox.addWidget(turnButton, 1, 1, 1, 2)
        vbox.addWidget(angle_label, 1, 1)

 
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('PyQt5 Layout')


        self.show()

def main():
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
