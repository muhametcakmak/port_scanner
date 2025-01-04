# Port Tarayıcı

Bu Python programı, belirtilen bir IP adresinde port taraması yapar. Çoklu thread yapısı sayesinde hızlı ve etkili bir tarama gerçekleştirir.

## 🚀 Özellikler

- Çoklu thread desteği ile hızlı tarama
- IP adresi doğrulama
- Özelleştirilebilir port aralığı
- Kullanıcı dostu arayüz

## 📋 Gereksinimler

- Python 3.x

## 🔧 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/muhametcakmak/port_scanner.git
cd port_scanner
```

## 💻 Kullanım

1. Programı çalıştırın:
```bash
python main.py
```

2. İstenilen bilgileri girin:
   - Hedef IP adresi
   - Başlangıç portu
   - Bitiş portu

3. Program otomatik olarak taramayı başlatacak ve sonuçları gösterecektir.

## 📝 Örnek Çıktı

```
Hedef IP: 192.168.1.1
Port 80: Açık
Port 443: Açık
Port 22: Açık
Tarama tamamlandı!
```

## ⚠️ Güvenlik Notu

Bu aracı yalnızca kendi sistemlerinizde veya izin verilen sistemlerde kullanın. İzinsiz port taraması yasal sorunlara yol açabilir.

## 🤝 Katkıda Bulunma

1. Bu projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin yeni-ozellik`)
5. Pull Request oluşturun

## 👥 İletişim

Sorularınız için Issues bölümünü kullanabilirsiniz. 