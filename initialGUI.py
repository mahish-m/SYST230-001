import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#from backend.PassManager import *

"""
TODO: Create a function in here which allows for GUI based inputs and outputs. i.e. a prompt. By doing this,
all of the prompts created in the backend folder can be replaced with it.
By adding this line to the top of the code:
    from backend.PassManager import *
It runs Passmanager.py. But the prompts to Passmanager.py are command line based. This means the GUI has to wait for
the commandline/terminal to complete.
If all the prompts in passmanager.py are replaced with a function which utilizes PyQt5 from initialGUI.py, 
nothing really needs to be changed. Instead just replaced. Please work on this.
"""


class PasswordGenerator(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Print Password'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        #Inputs textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(200,40)
        
        #Inputs Button
        self.button = QPushButton('Press to print', self)
        self.button.move(10,80)
        self.button.resize(200,60)
        
        # button is related to function
        self.button.clicked.connect(self.on_click)
        self.show()
    
    
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Print Password', "User Input: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    runGui = QApplication(sys.argv)
    ex = PasswordGenerator()
    sys.exit(runGui.exec_())
