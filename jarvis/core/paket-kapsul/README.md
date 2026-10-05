# Konu kapsülleri (Karar 112, 2026-10-05; deneysel m.29)

*Bağlam paketi başına tek dosya: `<paket-id>.md`. Paketten çıkarken Jarvis yazar, pakete girerken okur; pencere temizlense de konu buradan sürer. Paket listesi `core/baglam-paketleri.json`, yönlendirici `tools/paket-yonlendir.py`.*

Biçim (üzerine yazılır, ≤25 satır; tarihçe git log'da):

```markdown
# <paket-id> — konu kapsülü
**Güncelleme:** YYYY-MM-DD (oturum kısa kimliği)
## Nerede kaldık
- …
## Sıradaki adım
- …
## Açık soru / Salih'te bekleyen
- …
```

Kural: karar kaydı buraya yazılmaz (defter `kuyruk/senaryo-defteri.md`); genel durum buraya yazılmaz (`core/durum-kapsulu.md`). Burası yalnız o konunun çalışma durumu.
