from PyQt5 import uic
from PyQt5.QtWidgets import QPlainTextEdit, QTableWidget, QTableWidgetItem, QLabel

from common import log_pr
from setting import *


class DET_TblwWeightCalc():
    (form, base) = uic.loadUiType(SCREEN_URL + 'deter_calc_tblw_weight.ui')
    TITLE = "테이블 가중치 계산"
###########################################################
    gds_match = {}
    def calc_gds_match(self, input: str):
        # input 예시
        '''
KIT 2
KJW 3
NJH 1
NJH 3
        '''
        lines = input.split('\n')
        gds_match = {}
        for l in lines:
            if l.strip() == "":
                continue
            l_devide = l.strip().split(' ')
            if l_devide[0] not in gds_match.keys():
                gds_match[l_devide[0]]  = int(l_devide[1])
            else:
                gds_match[l_devide[0]] += int(l_devide[1])
        return gds_match

    def apply_gds_match_to_chart(self):
        tblw_c : QTableWidget = self.cur_screen.tblw_chart
        tblw_c.setRowCount(len(self.gds_match))
        idx = 0

        self.cur_screen.tblw_chart.cellChanged.disconnect()
        try:
            for g in self.gds_match:
                tblw_c.setItem(idx, 0 , QTableWidgetItem(g                      ))
                tblw_c.setItem(idx, 1 , QTableWidgetItem(str(self.gds_match[g]) ))
                tblw_c.setItem(idx, 2 , QTableWidgetItem("0"                    ))
                idx += 1
        except Exception as ex:
            log_pr("apply_gds_match_to_chart error [%s]" % (str(ex)))
        finally:
            self.cur_screen.tblw_chart.cellChanged.connect(self.when_tblw_chart_currentCellChanged)

    def apply_weight(self):
        tblw_c          : QTableWidget = self.cur_screen.tblw_chart
        lbl_pure_qty    : QLabel = self.cur_screen.lbl_pure_qty
        lbl_calc_qty    : QLabel = self.cur_screen.lbl_calc_qty
        tblw_c_cnt = tblw_c.rowCount()

        pure_qty = 0
        calc_qty = 0

        for i in range(tblw_c_cnt):
            try:
                pure_qty    += int(tblw_c.item(i, 1).text())
                calc_qty    += int(tblw_c.item(i, 1).text()) * int(tblw_c.item(i, 2).text())

                lbl_pure_qty.setText(str(pure_qty))
                lbl_calc_qty.setText(str(calc_qty))
            except Exception as ex:
                log_pr("apply_weight error [%s]" % (str(ex)))

    def widget_init(self, cur_screen):
        self.cur_screen = cur_screen

        cur_screen.pte_input    : QPlainTextEdit
        cur_screen.tblw_chart   : QTableWidget

        def preview():
            pass

        cur_screen.pte_input.   textChanged. connect(self.when_pte_input_textChanged)
        cur_screen.tblw_chart.  cellChanged. connect(self.when_tblw_chart_currentCellChanged)

    def when_pte_input_textChanged(self):
        print("when_pte_input_textChanged")
        # STEP 1. 파싱
        try:
            self.gds_match = self.calc_gds_match(self.cur_screen.pte_input.toPlainText())
        except Exception as ex:
            log_pr('widget_init - when_pte_input_textChanged 1 failed [%s]' % (str(ex)))

        # STEP 2. 파싱 내용을 테이블에 적용
        try:
            self.apply_gds_match_to_chart()
        except Exception as ex:
            log_pr('widget_init - when_pte_input_textChanged 2 failed [%s]' % (str(ex)))

    def when_tblw_chart_currentCellChanged(self):
        print("when_tblw_chart_currentCellChanged")
        # STEP 3. 테이블에 가중치를 수정할 때, 수량 항목들에 가중치를 적용
        try:
            self.apply_weight()
        except Exception as ex:
            log_pr('widget_init - when_tblw_chart_currentCellChanged failed [%s]' % (str(ex)))


    def run(self):
        pass