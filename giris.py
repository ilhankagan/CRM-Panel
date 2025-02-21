from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, switch_to_preferences):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(19, 29, 759, 529))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(19, 19, 721, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(70, 0, 561, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fotograflar/Screenshot_20250212_234051_Chrome.jpg"))
        self.label.setObjectName("label")

        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setGeometry(QtCore.QRect(110, 169, 241, 221))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 161, 41))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 161, 41))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")

        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setGeometry(QtCore.QRect(410, 170, 241, 221))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(0, 50, 241, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 150, 241, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.frame_5 = QtWidgets.QFrame(parent=self.frame)
        self.frame_5.setGeometry(QtCore.QRect(489, 399, 171, 111))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton.setGeometry(QtCore.QRect(12, 10, 141, 41))
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 141, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.switch_to_preferences = switch_to_preferences

        self.pushButton.clicked.connect(self.myFunction)
        self.pushButton_2.clicked.connect(MainWindow.close)  # Kapat butonuna tıklandığında pencereyi kapat

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "KULLANICI ADI:"))
        self.label_3.setText(_translate("MainWindow", "PAROLA:"))
        self.pushButton.setText(_translate("MainWindow", "GIRIS"))
        self.pushButton_2.setText(_translate("MainWindow", "KAPAT"))

    def myFunction(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == "mehmet" and password == "itforever":
            self.switch_to_preferences()
        elif username == "s" and password == "d":
            self.switch_to_preferences()
        elif username == "selim" and password == "cyber_warrior":
            self.switch_to_preferences()
        else:
            QtWidgets.QMessageBox.warning(None, "Hata", "Kullanıcı adı veya parola hatalı!")


class Ui_PreferencesPage(object):
    def setupUi(self, PreferencesPage, switch_to_main):
        PreferencesPage.setObjectName("PreferencesPage")
        PreferencesPage.resize(1081, 812)
        
        self.centralwidget = QtWidgets.QWidget(parent=PreferencesPage)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setText("ANA MENU")
        self.pushButton_5.setGeometry(QtCore.QRect(50, 50, 200, 40))
        self.pushButton_5.clicked.connect(switch_to_main)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setText("KAPAT")
        self.pushButton_4.setGeometry(QtCore.QRect(50, 100, 200, 40))
        self.pushButton_4.clicked.connect(QtWidgets.QApplication.instance().quit)

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setText("BASVURULAR")
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 200, 40))

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setText("MULAKATLAR")
        self.pushButton_2.setGeometry(QtCore.QRect(50, 250, 200, 40))

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setText("MENTOR GORUSMESI")
        self.pushButton_3.setGeometry(QtCore.QRect(50, 300, 200, 40))

        PreferencesPage.setCentralWidget(self.centralwidget)

    def retranslateUi(self, PreferencesPage):
        _translate = QtCore.QCoreApplication.translate
        PreferencesPage.setWindowTitle(_translate("PreferencesPage", "User Panel"))


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window_ui = Ui_MainWindow()
        self.preferences_page_ui = Ui_PreferencesPage()

        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 1012, 701)

        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Giriş sayfasını ekliyoruz
        self.main_window = QtWidgets.QMainWindow(self)
        self.main_window_ui.setupUi(self.main_window, self.show_preferences_page)
        self.stacked_widget.addWidget(self.main_window)

        # Kullanici sayfasını ekliyoruz
        self.preferences_page = QtWidgets.QMainWindow(self)
        self.preferences_page_ui.setupUi(self.preferences_page, self.show_main_page)
        self.stacked_widget.addWidget(self.preferences_page)

    def show_preferences_page(self):
        # Giriş sayfasından kullanici sayfasina gec
        self.stacked_widget.setCurrentWidget(self.preferences_page)

    def show_main_page(self):
        # Kullanici sayfasından giriş sayfasına geçiş yap
        self.stacked_widget.setCurrentWidget(self.main_window)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
