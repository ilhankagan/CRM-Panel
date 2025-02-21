import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from test2 import Ui_MainWindow as TercihlerUI
from PROJE import Ui_MainWindow as TercihlerAdminUI
from basvurular import BasvurularUI
from mentor import MentorInterviewUI
from mulakatlar import MulakatUI
from admin_final import AdminPanel
from giris import Ui_MainWindow as GirisUI
from google_calendar_service import get_events
import importlib

mail_sender = importlib.import_module("mail_sender")
send_mail = mail_sender.send_mail

class GirisEkrani(QMainWindow):
    def __init__(self, main_app):
        super().__init__()
        self.ui = GirisUI()
        self.ui.setupUi(self, self.switch_to_preferences)
        self.main_app = main_app
        
        # Giriş butonunu yönlendirme ekleyelim
        self.ui.pushButton.clicked.connect(self.login)
    
    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        if username == "s" and password == "d":
            self.main_app.switch_to(self.main_app.tercihler_menusu)
        elif username == "q" and password == "w":
            self.main_app.switch_to(self.main_app.tercihler_admin_menusu)
        else:
            print("❌ Hatalı giriş!")

    def switch_to_preferences(self):
        self.main_app.switch_to(self.main_app.tercihler_menusu)

class TercihlerMenusu(QMainWindow):
    def __init__(self, main_app):
        super().__init__()
        self.ui = TercihlerUI()
        self.ui.setupUi(self)
        self.main_app = main_app
        
        self.ui.pushButton.clicked.connect(lambda: self.main_app.switch_to(self.main_app.basvurular_ekrani))
        self.ui.pushButton_2.clicked.connect(lambda: self.main_app.switch_to(self.main_app.mentor_ekrani))
        self.ui.pushButton_3.clicked.connect(lambda: self.main_app.switch_to(self.main_app.mulakatlar_ekrani))
        self.ui.pushButton_5.clicked.connect(lambda: self.main_app.switch_to(self.main_app.giris_ekrani))

class TercihlerAdminMenusu(QMainWindow):
    def __init__(self, main_app):
        super().__init__()
        self.ui = TercihlerAdminUI()
        self.ui.setupUi(self)
        self.main_app = main_app
        
        self.ui.pushButton_6.clicked.connect(lambda: self.main_app.switch_to(self.main_app.admin_menusu))
        self.ui.pushButton_5.clicked.connect(lambda: self.main_app.switch_to(self.main_app.giris_ekrani))
        self.ui.pushButton_3.clicked.connect(lambda: self.main_app.switch_to(self.main_app.tercihler_admin_menusu))  # Admin Panelinden geri dönüş

        # ✅ Yeni buton işlevleri ekliyoruz!
        self.ui.pushButton.clicked.connect(lambda: self.main_app.switch_to(self.main_app.basvurular_ekrani))  # Başvurular Butonu
        self.ui.pushButton_2.clicked.connect(lambda: self.main_app.switch_to(self.main_app.mentor_ekrani))  # Mentor Görüşmesi
        self.ui.pushButton_4.clicked.connect(lambda: self.main_app.switch_to(self.main_app.mulakatlar_ekrani))  # Mülakatlar



class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.stack = QStackedWidget()
        
        self.giris_ekrani = GirisEkrani(self)
        self.tercihler_menusu = TercihlerMenusu(self)
        self.tercihler_admin_menusu = TercihlerAdminMenusu(self)
        self.basvurular_ekrani = BasvurularUI()
        self.mentor_ekrani = MentorInterviewUI()
        self.mulakatlar_ekrani = MulakatUI()
        self.admin_menusu = AdminPanel()
        
        self.stack.addWidget(self.giris_ekrani)
        self.stack.addWidget(self.tercihler_menusu)
        self.stack.addWidget(self.tercihler_admin_menusu)
        self.stack.addWidget(self.basvurular_ekrani)
        self.stack.addWidget(self.mentor_ekrani)
        self.stack.addWidget(self.mulakatlar_ekrani)
        self.stack.addWidget(self.admin_menusu)
        
        # TERCIHLER BUTONLARI EKLENDI
        self.basvurular_ekrani.ui.pushButton_9.clicked.connect(lambda: self.switch_to(self.tercihler_menusu))
        self.mentor_ekrani.preferences_button.clicked.connect(lambda: self.switch_to(self.tercihler_menusu))
        self.mulakatlar_ekrani.tercihler_button.clicked.connect(lambda: self.switch_to(self.tercihler_menusu))
        self.admin_menusu.pushButton_3.clicked.connect(lambda: self.switch_to(self.tercihler_admin_menusu))  # ✅ self.main_app kaldırıldı

        
        self.stack.setCurrentWidget(self.giris_ekrani)
        self.stack.show()
        sys.exit(self.app.exec())

    def switch_to(self, page):
        print(f"✅ Sayfa değiştiriliyor: {page}")
        self.stack.setCurrentWidget(page)

if __name__ == "__main__":
    MainApp()
