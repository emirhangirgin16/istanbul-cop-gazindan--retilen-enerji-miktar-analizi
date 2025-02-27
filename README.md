İstanbul Çöp Gazından Üretilen Enerji Miktarları Görselleştirme Projesi
Bu proje, İstanbul'da çöp gazından üretilen enerji miktarlarının çeşitli grafikler yardımıyla görselleştirilmesini sağlar. Veriler, bir Excel dosyasından yüklenerek yıllık ve tesis bazında analiz edilmiştir.

İçindekiler
Kurulum

Kullanım

Fonksiyonlar

yıllara_göre_toplam_üretim

son_3_yıl

tüm_tesisler

yıllı_üretim_pasta

Özellikler

Gereksinimler


**Kurulum**
Proje dosyalarını bilgisayarınıza indirin.

Gerekli kütüphaneleri yüklemek için terminal veya komut satırında aşağıdaki komutu çalıştırın:pip install pandas matplotlib tkinter openpyxl
istanbul-cop-gazndan-uretilen-enerji-miktarlar.xlsx adlı Excel dosyasını proje dizinine yerleştirin.
Kullanım
main.py dosyasını çalıştırarak Tkinter arayüzünü başlatın:python main.py
Açılan arayüzde, görmek istediğiniz grafiği seçmek için açılır menüyü kullanın ve "Grafiği Göster" düğmesine tıklayın.

Seçtiğiniz grafik, arayüzün sağ tarafında görüntülenecektir.
**Fonksiyonlar**
yıllara_göre_toplam_üretim
Bu fonksiyon, yıllara göre toplam enerji üretim miktarlarını bar grafik olarak görselleştirir.

son_3_yıl
Bu fonksiyon, son 3 yıl içerisindeki tesis bazında enerji üretim miktarlarını bar grafik olarak görselleştirir.

tüm_tesisler
Bu fonksiyon, tüm tesislerde yıllara göre enerji üretim miktarlarını çizgi grafik olarak görselleştirir.

yıllı_üretim_pasta
Bu fonksiyon, tesis bazında enerji üretim oranlarını pasta grafik olarak görselleştirir.
**Özellikler**
Yıllık toplam enerji üretim miktarı grafiği

Son 3 yılın tesis bazında enerji üretim miktarı grafiği

Tüm tesislerde yıllara göre enerji üretim miktarı grafiği

Tesis bazında enerji üretim oranları grafiği

Kullanıcı dostu Tkinter arayüzü

**Gereksinimler**
Python 3.x

Pandas

Matplotlib

Tkinter

Openpyxl
