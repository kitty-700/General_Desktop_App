import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from deter_calc import DET_TblwWeightCalc
from screen_base import ScreenBase

from common import *
from deter_echo import DET_Echo
from deter_memo_screen import DET_Memo

class MenuInit():
    def __init__(self, main_scr): # main_scr 는 MainScreen 클래스
        self.main_scr = main_scr
        status_bar = main_scr.statusBar()
        main_scr.setStatusBar(status_bar)
        menu_bar = main_scr.menuBar()  # QMainWindow 클래스에서 QMenuBar 를 자동 상속

        ## 일반
        try:
            gen = menu_bar.addMenu('일반')
            for i in self.menu_gen():
                gen.addAction(i)
        except Exception as ex:
            log_pr('MenuInit init failed 1 [%s]' % (str(ex)))
        ### 일반 [END]

        ## 계산
        try:
            calc = menu_bar.addMenu('계산')
            for i in self.menu_calc():
                calc.addAction(i)
        except Exception as ex:
            log_pr('MenuInit init failed 2 [%s]' % (str(ex)))
        ### 계산 [END]

    def menu_gen(self):
        sub_menus = []
        # 메모
        self.scr_memo_windows = []
        def show_memo():
            self.scr_memo_windows.append(ScreenBase(DET_Memo()).base_window)
            self.scr_memo_windows[-1].show()
        sub_menus.append(action_init(self, '메모'
                                     , show_memo
                                     , ''))
        # 메모 [END]
        # EXIT
        sub_menus.append(action_init(self, 'Exit'
                                     , exit_program
                                     , 'Ctrl+X'))
        # EXIT [END]
        return sub_menus

    def menu_calc(self):
        sub_menus = []
        # 계산
        self.scr_calc_windows = []
        def show_calc():
            self.scr_calc_windows.append(ScreenBase(DET_TblwWeightCalc()).base_window)
            self.scr_calc_windows[-1].show()
        sub_menus.append(action_init(self, '테이블 가중치 계산'
                                     , show_calc
                                     , ''))
        # 계산 [END]
        # 에코
        self.scr_echo_windows = []
        def show_echo():
            self.scr_echo_windows.append(ScreenBase(DET_Echo()).base_window)
            self.scr_echo_windows[-1].show()
        sub_menus.append(action_init(self, '에코'
                                     , show_echo
                                     , ''))
        # 에코 [END]
        return sub_menus

##########################################################################
def exit_program():
    sys.exit()

def action_init(menu_init:MenuInit, id:str, func, shortcut:str = ''):
    # id        = "&Exit"       # id 앞에 & 가 붙으면 Alt 를 눌렀을 때 가장 앞 글자를 shortcut 으로 사용한다는 뜻 (한글은 해당 사항 없음)
    # shortcut  = "Ctrl+X"
    tmp_action = QAction(id, menu_init.main_scr)
    tmp_action.setShortcut(shortcut)
    # tmp_action.setStatusTip("끝내기")
    tmp_action.triggered.connect(func)
    return tmp_action