import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

# UI dosyasını içe aktarma
from MentorInterviewMenu import Ui_MentorInterviewPage  # UI sınıfı
from mentor_data import MentorData  # Veri çekme sınıfımız

class MentorInterviewUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # **UI dosyasını yükle**
        self.ui = Ui_MentorInterviewPage()  
        self.ui.setupUi(self)

        # **Widget'ları Tanımlama**
        self.tablo = self.ui.tablo  # Tabloyu burada tanımla
        self.search_button = self.ui.ara
        self.exit_button = self.ui.cikis
        self.preferences_button = self.ui.tercihler
        self.all_meetings_button = self.ui.tumGorusme
        self.search_line_edit = self.ui.lineEdit  # Arama kutusu
        self.comboBox = self.ui.comboBox  # ComboBox 

        # **Veri Bağlantısı**
        self.mentor_data = MentorData()

        # **Butonları Fonksiyonlara Bağlama**
        self.search_button.clicked.connect(self.search)
        self.exit_button.clicked.connect(self.close)
        self.preferences_button.clicked.connect(self.go_to_preferences)
        self.all_meetings_button.clicked.connect(self.load_data)  # Tüm görüşmeleri yükle
        self.comboBox.currentIndexChanged.connect(self.filter_by_combobox)  # ComboBox seçim değiştiğinde filtrele

    def load_data(self):
        """Tüm mentor görüşmelerini çek ve tabloya ekle"""
        data = self.mentor_data.get_all_records()

        if self.tablo:
            self.tablo.clearContents()  # Mevcut içeriği temizle
            self.tablo.setRowCount(len(data))
            self.tablo.setColumnCount(len(data[0]))

            headers = list(data[0].keys())
            self.tablo.setHorizontalHeaderLabels(headers)

            for row_idx, row_data in enumerate(data):
                for col_idx, (key, value) in enumerate(row_data.items()):
                    self.tablo.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            print("✅ Tüm görüşmeler yüklendi!")  # Test için ekledik
        else:
            print("❌ Tablo yüklenemedi!")

    def search(self):
        """Arama butonu işlevi"""
        search_text = self.search_line_edit.text().strip().lower()
        
        all_data = self.mentor_data.get_all_records()
        filtered_data = [row for row in all_data if search_text in row["Ad Soyad"].lower()]

        self.update_tablo(filtered_data)
        print(f"🔍 '{search_text}' ile eşleşen kayıtlar getirildi.")

    def filter_by_combobox(self):
        """ComboBox seçimine göre verileri filtrele"""
        selected_text = self.comboBox.currentText().strip().lower()

        print(f"🎯 ComboBox Seçildi: {selected_text}")  # Seçilen değeri test etmek için

        if not selected_text:  # Eğer seçim yapılmadıysa işlem yapma
            return

        all_data = self.mentor_data.get_all_records()
        
        # **Seçilen metni "Durum" sütununda içerenleri getir**
        filtered_data = [row for row in all_data if selected_text in row["Durum"].strip().lower()]

        self.update_tablo(filtered_data)
        print(f"🔎 '{selected_text}' içeren kayıtlar getirildi.")

    def update_tablo(self, filtered_data):
        """Tabloyu güncelle"""
        if self.tablo:
            self.tablo.clearContents()  # Önce eski içeriği temizle
            self.tablo.setRowCount(len(filtered_data))

            for row_idx, row_data in enumerate(filtered_data):
                for col_idx, (key, value) in enumerate(row_data.items()):
                    self.tablo.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            print("✅ Tablo güncellendi!")
        else:
            print("❌ TableWidget yüklenemedi!")

    def go_to_preferences(self):
        """Tercihler sayfasına git"""
        print("Tercihler sayfasına yönlendirme burada olacak.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MentorInterviewUI()
    window.show()
    sys.exit(app.exec())
