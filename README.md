# ⚖️ UDF Belge Arama (com.adalettekno.UdfArama)

[![Flatpak](https://shields.io)](https://flathub.org)
[![License](https://shields.io)](LICENSE)

**UDF Belge Arama**, Linux (Ubuntu, Debian, Mint, PikaOS vb.) işletim sistemleri üzerinde çalışan, UYAP Döküman Editörü (.udf) formatındaki dilekçe, karar ve tensip tutanağı vb. belgelerin içerisinde içerik arayan hafif, hızlı ve kullanıcı dostu bir yazılımdır.

Hukukçuların ve adliye personelinin binlerce arşivlenmiş UDF dosyası arasından aradıkları emsal kararları veya evrakları saniyeler içinde bulması için tasarlanmıştır.

---

## ✨ Öne Çıkan Özellikler

* 📂 **Kalıcı Üst Klasör Hafızası:** Programı her açtığınızda her seferinde sıfırdan klasör seçmek zorunda kalmazsınız. Son seçtiğiniz üst klasör hafızada tutulur ve siz değiştirmedikçe orada aramaya devam eder.
* 🔍 **Alt Klasörler Dahil Derin Arama:** Seçtiğiniz üst klasörün altındaki tüm alt kırılımları ve klasörleri otomatik olarak tarar.
* 🚀 **Kesintisiz Kontrol ve Entegrasyon:** Arama sonuçları listesi kaybolmadan, sırayla farklı belgeleri açarak aradığınız belgenin hangisi olduğunu saptayabilirsiniz.
* 🛡️ **Bağımsız ve Güvenli Tasarım:** Dış masaüstü bağımlılıklarından yalıtılmış (gömülü modal pencereler), terminal ekranıyla uğraştırmayan temiz bir grafik arayüze sahiptir.

---

## 🛠️ Kurulum Yöntemi

### Programı bilgisayarınızın sistem menüsüne (Başlat menüsü) logosuyla birlikte kalıcı olarak entegre etmek için terminali açıp şu tek satırlık komutu çalıştırmanız yeterlidir:

```bash
curl -sL https://raw.githubusercontent.com/adalettekno/com.adalettekno.UdfArama/main/bin/udfarama | sudo tee /usr/local/bin/udfarama > /dev/null && sudo chmod +x /usr/local/bin/udfarama
```

---

## 🚀 Kullanım Kılavuzu

1. Programı sistem menünüzden **"UDF Belge Arama"** şeklinde aratarak veya terminale `udfarama` yazarak başlatınız.
2. İlk açılışta arama yapmak istediğiniz ana üst klasörü seçiniz (Bu klasör kalıcı olarak hafızaya alınacaktır).
3. Sonraki açılışlarda karşınıza gelen onay kutusundan doğrudan **"Bu Klasörde Ara"** diyebilir veya **"Klasörü Değiştir"** diyerek yeni bir alan seçebilirsiniz.
4. Aramak istediğiniz ibareyi çift tırnak kullanmadan girip Enter'a basınız.
5. Arama ile küçük büyük harf duyarlılığı olmaksızın tüm sonuçlara ulaşabileceksiniz.
6. Listelenen sonuçlardan istediğiniz belgeyi açıp inceleyin. İşiniz bittiğinde programdan güvenle çıkış yapabilirsiniz.

---

## 🛡️ Lisans ve Katkıda Bulunma
Bu proje **MIT** lisansı altında açık kaynak olarak korunmaktadır. Hukuk teknolojilerine (LegalTech) katkı sunmak, hata bildirmek veya kodu geliştirmek için "Pull Request" açabilir ya da bir "Issue" bırakabilirsiniz.

Developed by **Adalettekno** ⚖️⚡
