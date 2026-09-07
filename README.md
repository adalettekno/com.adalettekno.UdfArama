# ⚖️ UDF Belge Arama (com.adalettekno.UdfArama)

[![License: MIT](https://shields.io)](LICENSE)
[![Bash](https://shields.io)](https://gnu.org)

**UDF Belge Arama**, Linux (Ubuntu, Debian, Mint, Pardus vb.) işletim sistemleri üzerinde çalışan, UYAP Doküman Editörü (.udf) formatındaki dilekçe, karar ve tensip tutanağı gibi belgelerin içerisinde içerik araması yapan hafif, hızlı ve kullanıcı dostu bir masaüstü yazılımıdır.

Hukukçuların ve adliye personelinin binlerce arşivlenmiş UDF dosyası arasından aradıkları emsal kararları veya evrakları saniyeler içinde bulması için tasarlanmıştır.

---

## ✨ Öne Çıkan Özellikler

* 📂 **Kalıcı Üst Klasör Hafızası:** Programı her açtığınızda sıfırdan klasör seçmek zorunda kalmazsınız. Son seçtiğiniz üst klasör hafızada tutulur ve siz değiştirmedikçe orada aramaya devam eder.
* 🔍 **Alt Klasörler Dahil Derin Arama:** Seçtiğiniz üst klasörün altındaki tüm alt kırılımları ve klasörleri otomatik olarak tarar.
* 🚀 **Kesintisiz Kontrol ve Entegrasyon:** Arama sonuçları listesi kaybolmadan, sırayla farklı belgeleri açarak aradığınız belgenin hangisi olduğunu saptayabilirsiniz.
* 🛡️ **Masaüstü Ortam Uyumluluğu:** KDE, GNOME ve XFCE gibi farklı masaüstü ortamlarında Zenity arayüzünün bağımsız, kararlı ve gömülü pencerelerle çalışmasını sağlar.

---

## 🛠️ Kurulum Yöntemi

Programı bilgisayarınızın **Sistem Menüsüne (Başlat Menüsü) logosu ve kısayoluyla birlikte tam entegre** bir şekilde kurmak için terminali açıp aşağıdaki tek satırlık komutu çalıştırmanız yeterlidir:

```bash
curl -sL https://raw.githubusercontent.com/adalettekno/com.adalettekno.UdfArama/main/bin/udfarama | sudo tee /usr/local/bin/udfarama > /dev/null && sudo chmod +x /usr/local/bin/udfarama && sudo wget -qO /usr/share/applications/com.adalettekno.UdfArama.desktop https://githubusercontent.com && sudo mkdir -p /usr/share/icons/hicolor/256x256/apps/ && sudo wget -qO /usr/share/icons/hicolor/256x256/apps/udfarama.png https://githubusercontent.com
```

---

## 🚀 Kullanım Kılavuzu

1. Programı sistem menünüzden **"UDF Belge Arama"** şeklinde aratarak grafik arayüzle veya terminale `udfarama` yazarak başlatınız.
2. İlk açılışta arama yapmak istediğiniz ana üst klasörü seçiniz (Bu klasör kalıcı olarak hafızaya alınacaktır).
3. Sonraki açılışlarda karşınıza gelen onay kutusundan doğrudan **"Bu Klasörde Ara"** diyebilir veya **"Klasörü Değiştir"** diyerek yeni bir alan seçebilirsiniz.
4. Aramak istediğiniz ibareyi çift tırnak kullanmadan girip Enter'a basınız.
5. Listelenen sonuçlardan istediğiniz belgeyi çift tıklayarak sisteminizde kurulu olan varsayılan UYAP Editörü ile açıp inceleyebilirsiniz. İşiniz bittiğinde programdan güvenle çıkış yapabilirsiniz.

---

## 🛡️ Lisans ve Katkıda Bulunma
Bu proje **MIT** lisansı altında açık kaynak olarak korunmaktadır. Hukuk teknolojilerine (LegalTech) katkı sunmak, hata bildirmek veya kodu geliştirmek için "Pull Request" açabilir ya da bir "Issue" bırakabilirsiniz.

Developed by **AdaletTekno** ⚖️⚡
