import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from interviewpage import Ui_MainWindow  # Güncellenmiş UI dosyası
from mulakatlar_data import Mulakatlar  # Google Sheets bağlantısı

class MulakatUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # ✅ UI dosyasını yükle
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ✅ Google Sheets Verisini Yükle
        self.mulakatlar = Mulakatlar()
        
        # ✅ DEBUG: Tablo nesnesi var mı?
        print("DEBUG: Tablo mevcut mu?", hasattr(self.ui, "tablo"))

        # ✅ Tabloyu UI içinde tanımla
        self.tablo = self.ui.tablo  # <-- Güncellenmiş isim

        # ✅ Eğer tablo bulunamazsa hata ver
        if self.tablo is None:
            print("❌ HATA: Tablo yüklenemedi! UI içinde 'tablo' adlı QTableWidget var mı kontrol edin.")

        # ✅ Butonları Tanımla
        self.search_button = self.ui.ara
        self.exit_button = self.ui.cikis
        self.tercihler_button = self.ui.tercihler
        self.proje_gonderilmis_button = self.ui.projeGond
        self.proje_gelmis_button = self.ui.projeGel
        self.search_line_edit = self.ui.lineEdit

        # ✅ Butonlara Fonksiyon Bağla
        self.search_button.clicked.connect(self.search)
        self.exit_button.clicked.connect(self.close)
        self.tercihler_button.clicked.connect(self.go_to_preferences)
        self.proje_gonderilmis_button.clicked.connect(self.filter_sent_projects)
        self.proje_gelmis_button.clicked.connect(self.filter_received_projects)

        # ✅ Google Sheets verisini tabloya aktar
        self.load_data()

    def load_data(self):
        """Google Sheets verilerini çek ve tabloya ekle"""
        data = self.mulakatlar.sheet.get_all_records()

        if self.tablo:
            self.tablo.setRowCount(len(data))
            self.tablo.setColumnCount(len(data[0]))

            headers = list(data[0].keys())
            self.tablo.setHorizontalHeaderLabels(headers)

            for row_idx, row_data in enumerate(data):
                for col_idx, (key, value) in enumerate(row_data.items()):
                    self.tablo.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        else:
            print("❌ Tablo yüklenemedi! UI içinde 'tablo' adında bir QTableWidget olduğundan emin olun.")

    def search(self):
        """Arama butonu işlevi"""
        search_text = self.search_line_edit.text().lower()
        filtered_data = [row for row in self.mulakatlar.sheet.get_all_records() if search_text in row["Adınız Soyadınız"].lower()]
        self.update_table(filtered_data)

    def filter_sent_projects(self):
        """Projesi gönderilmiş olanları filtrele"""
        data = self.mulakatlar.sheet.get_all_records()
        filtered_data = [row for row in data if row["Proje gonderilis tarihi"]]
        self.update_table(filtered_data)

    def filter_received_projects(self):
        """Projesi gelmiş olanları filtrele"""
        data = self.mulakatlar.sheet.get_all_records()
        filtered_data = [row for row in data if row["Projenin gelis tarihi"]]
        self.update_table(filtered_data)

    def update_table(self, filtered_data):
        """TableWidget'i güncelle"""
        if self.tablo:
            self.tablo.setRowCount(len(filtered_data))
            for row_idx, row_data in enumerate(filtered_data):
                for col_idx, (key, value) in enumerate(row_data.items()):
                    self.tablo.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        else:
            print("❌ Tablo yüklenemedi! UI içinde 'tablo' adında bir QTableWidget olduğundan emin olun.")

    def go_to_preferences(self):
        """Tercihler sayfasına git"""
        print("Tercihler sayfasına yönlendirme burada olacak.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MulakatUI()
    window.show()
    sys.exit(app.exec())
