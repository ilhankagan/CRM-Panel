import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from app import Ui_MainWindow  # Sizin UI dosyanız
from basvurular_data import BasvurularData  # Google Sheets veri sınıfınız


class BasvurularUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = BasvurularData()

        # Buton bağlantıları
        self.ui.pushButton.clicked.connect(self.search)  # ARA
        self.ui.pushButton_8.clicked.connect(self.load_all_data)  # TUM BASVURULAR
        self.ui.pushButton_9.clicked.connect(self.go_to_preferences)  # TERCIHLER
        self.ui.pushButton_10.clicked.connect(self.close)  # EXIT
        self.ui.pushButton_5.clicked.connect(self.find_duplicates)  # MUKERRER KAYIT
        self.ui.pushButton_7.clicked.connect(self.find_differences)  # FARKLI KAYIT
        self.ui.pushButton_2.clicked.connect(self.filter_mentors_assigned)  # Mentor Görüşmesi Tanımlananlar
        self.ui.pushButton_3.clicked.connect(self.filter_mentors_not_assigned)  # Mentor Görüşmesi Tanımlanmayanlar


        self.load_all_data()
        
    def filter_mentors_assigned(self):
        """Mentor görüşmesi tanımlananları (OK yazanları) gösterir."""
        all_data = self.data.get_all_records()
        filtered_data = [row for row in all_data if row.get("Mentor gorusmesi", "").strip().upper() == "OK"]
        self.update_table(filtered_data)

    def filter_mentors_not_assigned(self):
        """Mentor görüşmesi tanımlanmayanları (ATANMADI yazanları) gösterir."""
        all_data = self.data.get_all_records()
        filtered_data = [row for row in all_data if row.get("Mentor gorusmesi", "").strip().upper() == "ATANMADI"]
        self.update_table(filtered_data)





    def load_all_data(self):
        """Tüm başvuruları Google Sheets'ten yükler ve tabloya yansıtır."""
        records = self.data.get_all_records()
        self.update_table(records)



    def search(self):
        """Arama yapar ve tabloyu günceller."""
        search_text = self.ui.textEdit.toPlainText().strip().lower()  # ✅ `textEdit` içindeki metni al
        if not search_text:
            print("⚠️ Uyarı: Arama kutusu boş!")
            return  # Eğer arama kutusu boşsa işlem yapma

        all_data = self.data.get_all_records()
        filtered_data = [] 
        for row in all_data:
            cleaned_row = {key: (str(value).lower() if value else "") for key, value in row.items()}  # ✅ Boş hücreleri temizle
            row_text = " ".join(cleaned_row.values())  # ✅ Satırı tek string yap
            print(f"🧐 Karşılaştırılan Satır (Temizlenmiş): {row_text}")  # Temizlenen satırı yazdır

            if search_text in row_text:
                print(f"✅ Eşleşme Bulundu: {row}")
                filtered_data.append(row)
        print("📊 Sonuç Listesi:", filtered_data)  # Sonuçları yazdır
        self.update_table(filtered_data)




    def find_duplicates(self):
        """Mükerrer kayıtları bulur."""
        all_data = self.data.get_all_records()
        seen = set()
        duplicates = []
        for row in all_data:
            key = (row['Isim Soyisim'], row['Mail'], row['Telefon'])
            if key in seen:
                duplicates.append(row)
            else:
                seen.add(key)
        self.update_table(duplicates)

    def find_differences(self):
        """Farklı kayıtları bulur (örnek: bir alana göre karşılaştırma yapılabilir)."""
        all_data = self.data.get_all_records()
        unique = {tuple(row.items()) for row in all_data}
        self.update_table([dict(u) for u in unique])

    def update_table(self, data):
        """Tabloyu verilen verilerle günceller."""
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]) if data else 0)
        headers = list(data[0].keys()) if data else []
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(data):
            for col_idx, (key, value) in enumerate(row_data.items()):
                self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def go_to_preferences(self):
        print("Tercihler sayfasına yönlendiriliyor...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasvurularUI()
    window.show()
    sys.exit(app.exec())
