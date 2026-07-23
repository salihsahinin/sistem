# Durum Kapsülü

*Her oturumun İLK okuduğu dosya. Üzerine yazılır; arşiv değildir. Açılış: kapsül ORIGIN KLONUNDAN okunur; mount'ta git komutu YOK (okuma dahil).*

**Güncelleme:** 2026-07-23 GÜNAYDIN VARDİYASI (Carvis, ana-sıra/Fable) — **PLATFORM KARARI ALINDI (Salih): kabuksuz-ajan rejimi → A2 KAPANDI 4/4** (senaryo-defteri 07-23; WSL2 K-011 gününe bağlandı) · A1 sicili **2/5** (07-23 senkron OK, `a27f4f8`→`e3937f9`) · bulut-vardiya raporu ingest edildi (`raporlar/2026-07-23-bulut-vardiya-dispatch-skill-raporu.md`: skill katmanları + Dispatch + ana-oturum karar-adayı) · günaydın-tetik boşluğu için hesap-skill paketi hazırlandı (kurulum tıkı Salih'te)

## Şu an
- **K-010 tetiği (m.38):** K-009 ∧ A1∧A2∧A3∧A4; A5 lider-hattı PARALEL (kuruluş = K-010∧A5). Detay pano K-010 kartı + defter 07-22.
- **A1 senkron sicili:** 2/5 ardışık OK (her günaydın log'a tek bakış: `raporlar/usage/senkron-log.jsonl`). **A2: KAPALI 4/4** (platform = kabuksuz-ajan, Salih 07-23; bu fazda ajanlara kabuk/exec YOK; core/-Bash PreToolUse teli kurulacak — tel, sınır değil; WSL2 → K-011 günü). **A3:** bekliyor (/goal 1 + /loop 1 + Routine 3 OK; araştırması DONE). **A4:** şema v1 + D4 kartı canlı (`kuyruk/ajan-defteri-sema-v1.md`); kalan denetçi bütçe-çatalı (Salih). **A5:** araştırma DONE (lider = sıkıştıran-süpervizör + read-only işçi + paralel iş); Atlas = nitelikli işçi, lider DEĞİL (Salih); ilk devir iş-sınıfı kararı açık.
- **Güvenlik istihbaratı [D] (07-22):** Windows-native'de OS sandbox YOK · settings-deny yalnız Edit/Write tutar, **core/ Bash-yazımına açık** (canary kanıtı raporda) · kabuk-taşıyan ajan zaptedilemez → şemada kabuk/exec bayrağı: VAR ise dış-bant izolasyon ZORUNLU; bu fazda ajanlara kabuk YOK.
- **K-016:** 4 skill canlı (S-A/S-B/S-C/S-G, hepsi eval'li) + atlas-kosum İLK CANLI KOŞUM: hayatta-kalma 9/9 çekirdek · 8/9 DARALTILDI (defter gözlemi). Kalan: canlı tetik testleri (doğal-dil + negatif; talimat 07-22 chat) · description-eval turu.
- **Şerit 2 (öğrenme):** P5 DONE · **P6 KOŞTU — ders html'i diskte UNTRACKED, commit+ingest dönüş ritüelinde** · P2 devir ingest bekliyor.
- **Kutu:** V59 (token-verim okuyucu — atlas verdikti: yalnız pencere-aşan iş + AUGMENT modunda) · V61 Record-a-Skill (K-016 gündemi) · V62 Cowork mobil (Mobil Köprü revizyon tetiği, m.41 boyutu Katman-1).

## Açık borçlar
- **GÜVENLİK:** PAT düz-metin + ~10 Ekim ölümü (credential-helper + yenileme tek hamle) · core/-Bash deliği (platform kararına bağlı).
- Salih kararları: MEZUN onayı (V36·V38·V40a·V43) · index.lock gerekçe-revizyonu · V59 tetik onayı · A5 ilk devir sınıfı · denetçi bütçe-çatalı · skill terfi süzgeci · günaydın-skill kurulum tıkı. **07-23 kararları: ana-oturum tanımı BEKLET (Salih şartı kuyruğa: ana oturum ↔ model=Fable; bulut-rapor beğenilmedi) · Dispatch BEKLET · CLAUDE.md sıra-önce kuralı EKLENDİ.**
- K-019 kalanı: stage-bayat/çift-koşum vakalarının toplu defter işlemesi · **senaryo-defteri 47.8KB/48KB SINIRDA (ilk boş vardiyada damıtma)**.
- Skill/wiki borçları: 20-sorgu description eval + çok-model test · wiki aday sayfaları (rol-katmanlari vb.) · Homebase pointer bayat · modern-tokenizer (O13).
- Tetikliler: K-011 · K-004 (Kasım) · PortRisk tetiği · K-018 (remote control).

## Sonraki ilk iş (yeni seans: kapsülü ORIGIN KLONUNDAN oku)
1. Senkron-log tek bakış (A1 sayacı: 2/5 → hedef 5/5; A3 koşumları A1 dolunca açılır).
2. core/-Bash PreToolUse telini kur + canlı test (PC oturumu; tel=tökezleme-teli, m.29).
3. Günaydın-skill kurulum tıkı (Salih) + skill terfi süzgeci (kuyruk notu).
4. Canlı tetik testleri (CC, 5 dk) · P6 commit+ingest · senaryo-defteri damıtma (48KB sınır AŞILDI — bu vardiyada +1 blok, ilk boş vardiyada zorunlu).
