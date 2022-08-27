from PyQt5 import uic
from PyQt5.QtWidgets import QPlainTextEdit

from setting import *


class DET_Echo():
    (form, base) = uic.loadUiType(SCREEN_URL + 'deter_echo.ui')
    TITLE = "에코"
###########################################################
    def widget_init(self, cur_screen):
        cur_screen.pte_input    : QPlainTextEdit
        cur_screen.pte_output   : QPlainTextEdit

        def preview():
            cur_screen.pte_output.setPlainText( cur_screen.pte_input.toPlainText() )

        cur_screen.pte_input.textChanged.connect(preview)

    def run(self):
        pass