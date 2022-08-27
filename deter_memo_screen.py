from PyQt5 import uic
from PyQt5.QtWidgets import QPlainTextEdit

from setting import *


class DET_Memo():
    (form, base) = uic.loadUiType(SCREEN_URL + 'deter_memo.ui')
    TITLE = "메모 화면"
###########################################################
    def widget_init(self, cur_screen):
        def preview():

            pass
        cur_screen.pte_first_memo : QPlainTextEdit
        cur_screen.pte_first_memo.setPlainText("this is initial page")

    def run(self):
        pass