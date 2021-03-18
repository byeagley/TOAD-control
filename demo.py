from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QHBoxLayout, QVBoxLayout, QGridLayout)
 
from PyQt5.QtCore import Qt
import sys

 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()

 
    def UI(self):

        def switchMode():
            if combo.currentText() == 'Ackermann':
                dial.setVisible(True)
                slider_label.setText("Forward speed")
                #slider.setValue(0)
                turnButton.setVisible(False)
            if combo.currentText() == 'Turn in Place':
                dial.setVisible(False)
                slider_label.setText("Turn speed")
                #slider.setValue(50)
                turnButton.setVisible(True)
        
        def changeColor():
            if button.isChecked():
                button.setStyleSheet("background-color : green")
            else:
                button.setStyleSheet("background-color : red")

        def speedDisplay(speed):
            speed_label.setText(str(speed))
        
        # Turn in Place Button
        turnButton = QPushButton('Turn')
        turnButton.setVisible(False)

        # Power Button
        button = QPushButton('Power')
        button.setCheckable(True)
        button.clicked.connect(changeColor)
        button.setMaximumWidth(50)
        button.setStyleSheet("background-color : red") 
        
        # Driving Mode Combo Box 
        combo = QtWidgets.QComboBox(self)
        combo.addItems(["Ackermann", "Turn in Place"])
        combo.currentIndexChanged.connect(switchMode)

        # Angle Dial
        dial = QtWidgets.QDial(self)
        dial.setMinimum(-30)
        dial.setMaximum(30)
        dial.setNotchesVisible(True)
        dial.setNotchTarget(2)
        dial.move(270,300)
        
        # Speed Slider
        slider = QtWidgets.QSlider(Qt.Vertical, self)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        slider.setTickInterval(10)
        slider.valueChanged.connect(speedDisplay)

        # Slider label    
        slider_label = QtWidgets.QLabel(self)
        slider_label.setWordWrap(True)
        slider_label.setText("Forward speed")

        # Speed label
        speed_label = QtWidgets.QLabel(self)
        speed_label.setText("0")
        


        # Layout Management 
        vbox = QGridLayout()
        vbox.addWidget(combo, 0, 2)
        vbox.addWidget(dial, 1, 2)
        vbox.addWidget(slider, 1, 0)
        vbox.addWidget(slider_label, 0, 0)
        vbox.addWidget(speed_label, 2, 0)
        vbox.addWidget(button, 2, 2)
        vbox.addWidget(turnButton, 1, 1)
 
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
