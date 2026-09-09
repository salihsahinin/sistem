# 01 — Node Mimarisi ve Repo Yapısı

**Statü:** öneri dosyası (imzasız) + Katman-2 varsayım kayıtları. **Kaynak:** Salih talimatı 07-10 ("THE JARVIS PART IS THE JARVIS NODE" + "CYBER REPO STRUCTURE").

## 1. Node topolojisi

JARVIS bir merkez değil, bir **node**: Salih'in çok-vault topolojisinde sistem-çekirdeği düğümü. Diğer düğümleri yutmaz; onlarla tanımlı arayüzlerden konuşur (havuz #1 çoklu-vault fikrinin zemini).

```
                    SALİH (Patron — tüm düğümlerin üstünde) ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
                       │
   ┌───────────┬───────┴────────┬──────────────┬────────────────┐
   │           │                │              │                │
 JARVIS      Homebase         Benlik        Demirtaş       dev repoları
 node        (yaşam+proje     (kişisel      (finans uydu   (C:\Users\sasah\dev\
 (C:\JARVIS) yüzeyi, git,     bellek        bot)           portrisk → PUBLIC;
 sistem      Carvis kanonu)   vault, CC)                   ileride vault-index)
 çekirdeği,                                  + Yaşam-Arşivi (arşiv)
 planlar)
```

## 2. Arayüz kuralları (ok yönleri)

- JARVIS node diğer vault'ları **OKUR** (yalnız Salih izniyle / görev emri kapsamında); onlara **YAZMAZ**.
- Tek yazma istisnası: ajan çıktıları kendi `raporlar/` klasörüne düşer (report-only write path — sondevir kavram 6).
- Homebase kanonuna (CLAUDE.md, sözlük, havuz) yazım = Katman 1, yalnız Salih kararıyla. Bu gece hiçbir Homebase yazımı yapılmadı (karantina — tarama onayına dek).
- dev repoları (PortRisk, ileride vault-index) Salih'in kendi commit'leriyle büyür; bu node oradan yalnız plan/rapor düzeyinde bahseder. (Kayıtlı ders 06-30: "CV artefaktı ancak kendi makinende, kendi commit'lerinle doğar.")

## 3. Repo ağacı ve yazma yüzeyleri

| Yol | İşlev | Yüzey türü |
|---|---|---|
| `core/` | durum kapsülü, pano, tüzük v0, şablonlar | **KANON** — yalnız Salih kararıyla değişir (pano/kapsül durum alanları hariç: onlar operasyonel, Carvis günceller) |
| `00–03_*.md` | master plan, mimari, index planı, duvar raporu | **TASLAK/ÖNERİ** — serbest yazılır; karar blokları yalnız kaynaklı karar kaydıyla |
| `raporlar/` | ajan görev raporları | **RAPOR** — serbest; karar içeremez |
| `kuyruk/` | iş kartları (Faz D'de aktifleşir) | geçici not — durum güncellemesi serbest |
| `wiki/` | kavram wiki'leri hedef alanı | taslak |

## 4. Hijyen kuralları ("cyber" katmanı)

1. **Bu repo private/lokal kalır.** İçerik kişisel (kararlar, günlük referansları) — public'e açılmaz (red-team §2.3: gizlilik + algı riski).
2. **Public repo kontrol listesi** (PortRisk ve sonrası için): İngilizce README · LICENSE · testler · CI rozeti · **gerçek bakiye/rakam ASLA** (yalnız model ağırlıkları — kayıtlı kural: "kod public, gerçek rakam değil") · API anahtarı/secret asla (push öncesi göz taraması; `.gitignore`'da `.env`, `*.key`, `*.pem`).
3. **Tek-kopya riski kayıtlı:** bu makinede bulut yedek YOK (Salih'in bilinçli 07-10 kararı). Bu node C:\ kökünde, Homebase ayrı klasörde, dev repoları ayrı — hepsi AYNI diskte. Public GitHub repoları fiili yedek kanalı; JARVIS node için yedek kararı sistem büyürse yeniden fiyatlanır (bkz. `03_DUVAR_RAPORU.md` §4).
4. Commit dili İngilizce; her mantıksal karar/parça ayrı commit.

## 5. Varsayım kayıtları (Katman 2 — geri-açma koşullu)

- **V1 — JARVIS node ayrı repo** (Homebase'e gömülü değil). Kaynak: Salih "C:\JARVIS hedef" (07-10). Geri-açma: S12 cevabı (paket iskeleti → mevcut yapı haritalaması) ters düşerse içerik taşınır, git tarihçesi korunur.
- **V2 — Şablonlara sözlük-dışı 3 taslak alan eklendi:** zaman bütçesi (#22), hiyerarşi-telafisi notu (#23), koşucu sınıfı (#24). Sözlük v1 DONDU olduğundan bu alanlar "öneri" statüsünde; tüzüğe yalnız Salih imzasıyla girer.
- **V3 — Karantina:** bu gecenin tüm üretimi bu repoda; Homebase kaydı (CLAUDE.md proje girişi + log) tarama onayından sonraki ilk commit.
