# UDF Belge Arama

UYAP Doküman Editörü `.udf` dosyalarının içeriğinde hızlı arama yapan Linux masaüstü uygulaması.

## Flatpak

Uygulama GTK4/PyGObject kullanır. Klasör seçimi masaüstü dosya seçici portalı üzerinden yapılır; host dosya sistemine geniş erişim izni istemez.

UDF dosyaları ZIP kapsayıcısı olarak açılır ve `content.xml` içeriği UTF-8 metin olarak aranır.

### Yerel test

```bash
flatpak install flathub org.gnome.Sdk//50 org.gnome.Platform//50
flatpak-builder --user --install --force-clean build-dir io.github.adalettekno.UdfArama.yml
flatpak run io.github.adalettekno.UdfArama
```

> Not: Flathub'da GitHub barındırılan uygulama kimlikleri için güncel kuralları kontrol edin. Bu proje mevcut `com.adalettekno.UdfArama` kimliğini korur; `adalettekno.com` alan adı doğrulaması gerekiyorsa Flathub doğrulama adımını ayrıca tamamlayın.
