# Görev iletişim formatı geçiş planı — md → lojik → json → python (İB-84; Salih emri 2026-09-10)

*Salih 09-10 (Katman-1, aynen): "direk chate yüklenecek md dosyası formatında iletişim kurulmasını istiyorum md dosyasını açıp içerisindeki prompt kısmını kopyalayıp yapıştırmak istemiyorum. iletişim formatı da başlarda md olur ama günlük dil-lojik-kod bağlamında bir yerden sonra farklı dosya formatında görev verebilmek hedefimiz olsun (json format olur python olur geçiş sürecini sen tasarla)". Tasarlayan Jarvis (ana-sıra). Deneysel m.29; eşikler ilk 5 görevden sonra kalibre.*

## 0. İlke
Görev = DOSYA; sohbete bırakılır, kopyalanmaz. Dosyanın türü, alıcı ajanın onu ne kadar az yorumla icra edebildiğine göre ilerler: günlük dil (md) → lojik (m.38 bağlaç seti) → veri (json devir birimi) → kod (python görev-fonksiyonu). Her aşama bir öncekini KAPSAR; geri düşüş serbest (bir görev md'ye geri dönebilir, aşama etiketi düşer).

## 1. Aşamalar
| Aşama | Dosya | İçerik | Alıcı ne yapar | Geçiş koşulu (bir sonrakine) |
|---|---|---|---|---|
| **A0 · md (bugün)** | `cc/gelen/gorev-YYYY-MM-DD-<ad>.md` | günlük dil: oku → iş → kapanış; devir birimi json'a POINTER | okur, yorumlar, json'u açar | ≥3 görev; sapma (`[sapma]`) oranı ≤1/görev; "amaç↔done" çelişkisi 0 |
| **A1 · md + lojik blok** | aynı md; üstte `DALLAR` bloğu m.38 formunda (∧ ∨ ¬ → ↔), `done` boolean yüklem | lojik bloğu bağlayıcı sayar, düz yazı yalnız gerekçe | ≥3 görev; lojik blok ile düz yazı arasında çelişki 0; Friday soru sayısı ≤2/görev |
| **A2 · json tek başına** | `cc/gelen/devir-*.json` sohbete bırakılır; md yok | alan adları = emir; `gorev.dallar[]` lojik dizgeler; `baglam.eager[]` okuma listesi | json'u şemaya karşı doğrular (`sablon` alanı), eksik alan → DUR | ≥3 görev; şema ihlali 0; geri-dönüş `sapma` tablosu boş |
| **A3 · python görev-fonksiyonu** | `cc/gelen/gorev_*.py`: `def gorev(ctx) -> Sonuc`; `dallar` = `if` zinciri; `done` = `assert`; `butce` = dekoratör | dosyayı ÇALIŞTIRMAZ, OKUR: kod = emir (ajan-metodolojisi §1 "görev = küçük tipli fonksiyon"); test dosyası `test_gorev_*.py` done yüklemini koşar | Salih hükmü; A2'de 3 görev temiz |

## 1b. Revizyon 09-10 ~12:40 (Friday tur-2 (d) + B2 bulgusu)
- **A0 → A1 hemen:** tur-2'de md emir + json devir birimi çifti senkron çıkmadı (json (d) maddesini kaybetti). Tek kaynak = **md emir + lojik blok**; json ondan TÜRETİLİR (`tools/devir-md2json.py`, icra borcu), elle çift yazılmaz; çelişkide md kazanır.
- **Lojik blok alanları** (Friday'in 5 eksik alanı + kendi notu): DALLAR · DONE (çıktı başına ayrı yüklem) · YAZMA_İZNİ · YASAK · NİÇİN_ŞİMDİ · BAĞLI_DEVİR · KAPALI_GÖZ_ÖZETİ (envanter pointer'ı, desen 20 ön-koşulu) · ÖLÇEN (yapan ≠ ölçen).
- **Geçiş ölçüsü:** emir-kaynaklı `[sapma]` sayısı / devir (Friday sayar, Jarvis doğrular); aşama atlama = arka arkaya 2 devirde 0. Sayım: tur-1 = 2, tur-2 = 1.
- **A3 sınırı:** mekanik done `assert`, normatif done okuyan taraf; fonksiyon Jarvis'te koşar, sonucu devir birimiyle gider; `yeniden_deneme` emri yazanın bütçesinden.

## 2. Neden bu sıra
- md → lojik: aynı dosya, tek blok eklenir; ajanın "hangi cümle bağlayıcı" sorusu kalkar (Friday tur-1 A1/A2 sınıfı çelişkiler A1'de yapısal olarak görünür olur).
- lojik → json: lojik blok zaten json `dallar[]` alanının metnidir; md'nin geri kalanı (gerekçe) `baglam.karar_ozeti[]`'ne iner. Kayıp: anlatı; kazanç: şema doğrulaması makinede.
- json → python: `done_yuklemi` string'i test edilebilir `assert` olur; "bitti mi" sorusunu ajan değil test cevaplar (yapan ≠ ölçen, desen 4).

## 3. Salih'in kullanımı (her aşamada aynı)
Dosyayı Finder'dan Claude Code sohbetine sürükle/bırak (ya da `@` ile ekle). Dosyanın ilk satırı "bu dosya sohbete bırakıldığında EMİRDİR" der; ajan başka prompt beklemez. İlk örnek: `~/friday/cc/gelen/gorev-2026-09-10-tur2.md` (A0).

## 4. Ölçüm (kalibrasyon girdisi)
Geri-dönüş notundaki `sapmalar` + `acik_sorular` sayıları görev başına; `v_skill_kosum`'a `format_asamasi` alanı (A0-A3) — İB-84 icra borcu: geri-dönüş şablonuna 1 alan + gold görünüme 1 kolon.

## 5. Açık sorular (Friday tur-2 (d) cevabı bekleniyor)
Hangi aşamada hangi alan Friday'e yetmez · A3'te ajanın kodu çalıştırmaması nasıl kilitlenir (hook: `python3 cc/gelen/gorev_*.py` → RED) · A2'de md'siz json'un "neden" bilgisi nerede durur.
