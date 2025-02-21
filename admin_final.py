from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QLabel, QMessageBox, QWidget, QVBoxLayout
import sys
from google_calendar_service import get_events

import importlib
mail_sender = importlib.import_module("mail_sender")
send_mail = mail_sender.send_mail


class AdminPanel(QtWidgets.QMainWindow):
    def __init__(self):  # ✅ main_app parametresini ekledik
        super().__init__()
        
       
        # UI dosyasını yükle
        uic.loadUi("admin.ui", self)

        # QTabWidget bileşenini tanımla
        self.tabWidget = self.findChild(QtWidgets.QTabWidget, "ETKINLIK_2")

        if self.tabWidget is None:
            print("QTabWidget bulunamadı! Lütfen admin.ui içinde bileşenin adını kontrol edin.")
            return

        # Butonları işlevsel hale getir
        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, "pushButton_3")  # Butonu açıkça tanımla


        self.pushButton.clicked.connect(self.load_events)  # ETKİNLİK KONTROL butonu
        self.pushButton_2.clicked.connect(self.send_mails)  # MAIL GONDER butonu
        self.pushButton_4.clicked.connect(self.close)  # EXIT butonu

        if self.pushButton_3:
            self.pushButton_3.clicked.connect(lambda: self.main_app.switch_to(self.main_app.tercihler_admin_menusu))
        else:
            print("❌ pushButton_3 bulunamadı! admin.ui içinde ismini kontrol et.")




    def load_events(self):
        """Google Calendar etkinliklerini QTabWidget içinde sekmeler halinde gösterir."""
        start_date = "2025-02-18"
        end_date = "2025-02-21"
        events = get_events(start_date, end_date)

        # Mevcut sekmeleri temizle (ilk sekme hariç)
        while self.tabWidget.count() > 1:
            self.tabWidget.removeTab(1)

        if not events:
            QMessageBox.warning(self, "Uyarı", "Belirtilen tarih aralığında etkinlik bulunamadı!")
            return

        for event in events:
            # Yeni bir sekme oluştur
            new_tab = QWidget()
            layout = QVBoxLayout()

            # Etkinlik bilgilerini QLabel ile göster
            etkinlik_adi = QLabel(f"Etkinlik: {event['summary']}")
            baslangic_zamani = QLabel(f"Başlangıç Zamanı: {event['start']}")
            katilimcilar = QLabel(f"Katılımcılar: {', '.join(event['attendees']) if event['attendees'] else 'Yok'}")
            organizator = QLabel(f"Organizatör: {event['organizer']}")

            # Etkinlik bilgilerini sekmeye ekle
            layout.addWidget(etkinlik_adi)
            layout.addWidget(baslangic_zamani)
            layout.addWidget(katilimcilar)
            layout.addWidget(organizator)
            new_tab.setLayout(layout)

            # Sekmeyi QTabWidget'e ekle
            self.tabWidget.addTab(new_tab, event["summary"])

        QMessageBox.information(self, "Başarılı", "Etkinlikler başarıyla sekmelere yüklendi!")

    def send_mails(self):
        """Her sekmedeki etkinlik için mail gönderir."""
        tab_count = self.tabWidget.count()
        if tab_count <= 1:
            QMessageBox.warning(self, "Uyarı", "Mail gönderecek etkinlik bulunamadı!")
            return

        confirmation = QMessageBox.question(
            self,
            "Onay",
            "Seçili etkinliklere mail göndermek istediğinize emin misiniz?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if confirmation == QMessageBox.StandardButton.No:
            return

        for index in range(1, tab_count):  # İlk sekme hariç diğer sekmelere bak
            event_name = self.tabWidget.tabText(index)
            event_time = "Bilinmeyen Zaman"  # Google Calendar'dan gelen zamanı alabiliriz
            attendees = ["katilimci@example.com"]  # Şimdilik sabit bir liste, etkinlikten çekilebilir

            subject = f"Etkinlik Hatırlatması: {event_name}"
            body = f"Merhaba,\n\n{event_name} etkinliğine katılacaksınız.\nBaşlangıç zamanı: {event_time}\n\nİyi günler!"

            for recipient in attendees:
                if recipient.strip():
                    send_mail(recipient.strip(), subject, body)

        QMessageBox.information(self, "Başarılı", "E-postalar başarıyla gönderildi!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdminPanel()
    window.show()
    sys.exit(app.exec())
