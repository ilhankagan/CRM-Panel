📌 CRM Projesi Kullanım Kılavuzu
1️⃣ Kurulum ve Çalıştırma
Bu proje, Python ile geliştirilmiş bir CRM (Customer Relationship Management - Müşteri İlişkileri Yönetimi) sistemidir. Uygulama Google Sheets ve Google Calendar entegrasyonları içerir.

🛠 Gerekli Bağımlılıkların Kurulumu
Projenin çalışması için gerekli Python paketlerini yüklemek için şu adımları takip edin:

Python'un sisteminizde yüklü olduğundan emin olun (Önerilen sürüm: 3.9+)

Terminal veya Komut İstemi'ni açarak proje klasörüne gidin.

Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:

bash
Kopyala
Düzenle
pip install -r requirements.txt
🚀 Uygulamayı Çalıştırma
Gerekli bağımlılıklar yüklendikten sonra, uygulamayı başlatmak için aşağıdaki komutu çalıştırın:

bash
Kopyala
Düzenle
python main.py
Bunu çalıştırdıktan sonra CRM uygulaması açılacaktır.

2️⃣ Kullanım Rehberi
Uygulamayı başlattığınızda sizi Giriş Ekranı karşılayacaktır. Burada kullanıcı adı ve şifre girişi yaparak ilgili menülere yönlendirme yapılır.

🔹 Giriş Ekranı
Giriş ekranında aşağıdaki giriş kombinasyonlarını kullanabilirsiniz:


Hatalı giriş yapıldığında ekranda bir uyarı mesajı çıkacaktır.

🔹 Tercihler Menüsü
Tercihler menüsüne giriş yaptığınızda aşağıdaki butonları göreceksiniz:

Başvurular → Başvurular ekranına gider.
Mülakatlar → Mülakat ekranına gider.
Mentor Görüşmesi → Mentor görüşmesi sayfasına gider.
Ana Menü → Giriş ekranına geri döner.
Kapat → Uygulamayı kapatır.
Bu menüden istediğiniz alana giderek işlemlerinizi yapabilirsiniz.

🔹 Tercihler Admin Menüsü
Bu menü, admin yetkisiyle daha fazla kontrol sağlar. Burada yukarıdaki menü öğelerine ek olarak Admin Menü butonu bulunur.

Admin Menü → Google Calendar etkinliklerinin listelendiği admin paneline gider.
🔹 Admin Paneli (Admin Menü)
Bu panelde Google Calendar ile entegre çalışan bir sistem bulunur. Aşağıdaki işlemleri yapabilirsiniz:

"ETKİNLİK KONTROL" → Google Calendar'dan etkinlikleri getirir.
"MAIL GÖNDER" → Belirlenen etkinlik katılımcılarına e-posta gönderir.
"TERCİH-ADMIN MENU" → Tercihler Admin Menüsüne geri döner.
"EXIT" → Admin panelinden çıkış yapar.
🔹 Başvurular Menüsü
Başvurular ekranına gidildiğinde kullanıcı başvuru verilerini görüntüleyebilir ve arama yapabilir.

🔸 Özel Filtreleme İşlevleri:

Mentor Görüşmesi Tanımlananlar → Başvurular arasından mentor görüşmesi atanan kişileri gösterir. (OK yazanlar)
Mentor Görüşmesi Tanımlanmayanlar → Mentor atanmayan kişileri gösterir. (ATANMADI yazanlar)
Bu butonlara tıklayarak mentor görüşmesi durumu ile ilgili listeleme yapılabilir.

🔹 Mülakatlar & Mentor Görüşmesi Ekranı
Bu ekranlarda ilgili verileri görüntüleyebilir, filtreleyebilir ve arama yapabilirsiniz.

Mülakatlar ekranı → Başvuranların mülakat süreçlerini gösterir.
Mentor Görüşmesi ekranı → Kullanıcının mentor görüşmesi sürecini takip edebilirsiniz.
Her iki ekranda da "Tercihler" butonuna tıklayarak Tercihler Menüsüne dönebilirsiniz.

3️⃣ Ekstra Bilgiler
Tüm veriler Google Sheets ile senkronize edilir.
Google Calendar API kullanılarak etkinlik yönetimi sağlanır.
E-posta gönderme işlemi için SMTP veya Mailgun entegrasyonu kullanılabilir.
4️⃣ Uygulamadan Çıkış
Uygulamadan çıkmak için:

Giriş ekranında "Kapat" butonuna tıklayabilirsiniz.
Menülerdeki "Exit" butonu ile çıkış yapabilirsiniz.
Komut satırında CTRL + C tuş kombinasyonunu kullanarak programı sonlandırabilirsiniz.

