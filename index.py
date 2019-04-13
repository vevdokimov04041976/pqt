import sys
import os.path, os
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        app.setWindowIcon(QIcon(os.path.join(os.getcwd() , 'icon.png')))
        btn = QPushButton('Button1', self)
        btn.clicked.connect(self.get_images)
        btn.resize(200, 50)
        btn.move(100, 100)
        btn.setStyleSheet('background-color: red;')
        self.btn = btn

        self.textbox = QLineEdit(self)
        self.textbox.setText('0000')
        self.textbox.setInputMask('0000')
        #self.textbox.setEchoMode(QLineEdit.Password)
        self.textbox.setReadOnly(False)
        self.textbox.textChanged.connect(self.on_textbox_changed)
        self.textbox.editingFinished.connect(self.on_textbox_finished)
        

        
        self.show()

    def get_images(self):
        self.btn.setText(self.btn.text()[:-1])
        print('get_images....', self.btn.text())
        value = self.textbox.text()
        print('value', value)

    def on_textbox_changed(self,text):
        print('on_textbox_changed', text)

    def on_textbox_finished(self):
        print('finish')
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
