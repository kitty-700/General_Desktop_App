import threading

# ScreenBase 클래스는 명칭 DET_* 로 정의되는 determinant 클래스들로부터 상속을 받아 메뉴 (MenuInit 클래스)에서 화면 호출을 위해 사용됨

class ScreenBase():
    def __init__(self, determinant):
        self.determinant = determinant
        form = determinant.form
        base = determinant.base
        class BaseWindow(base, form):
            class excute(threading.Thread):
                def __init__(selfself, determinant):
                    self.determinant = determinant
                def run(self):
                    determinant.run()

            def __init__(self, determinant):
                self.determinant = determinant
                super(self.determinant.base, self).__init__()
                self.setupUi(self)
                self.setWindowTitle(self.determinant.TITLE)

                self.determinant.widget_init(self)

        self.base_window = BaseWindow(self.determinant)