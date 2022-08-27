import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5 import uic

from menu_initializer import MenuInit
from setting import *

form_class = uic.loadUiType(SCREEN_URL + 'main.ui')[0]

class MainScreen(QMainWindow, form_class): # main_screen
    def __init__(self):
        super().__init__()
        self.setupUi(self) # uic 로부터 상속받은 화면 초기화
        self.setWindowTitle('KIT. Tool.')
        menu = MenuInit(self)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainScreen()
    sys.exit(app.exec_())