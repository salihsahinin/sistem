# Seans teslim raporu — 2026-09-11 10:07 → 2026-09-15 ~12:00 (Fable ana-sıra; resume 09-14, 09-15) · masa-11/12 · Karar 94-96 · skill hazinesi yönetimi

*Şablon `core/sablonlar/seans-teslim.md` (beş soru). Rakamlar bu seansın sayımı (m.39); kestirim `[?]`. Uzun seans: 4 takvim günü, 2 resume; hasat kontrol listesi §6.*

## 1. Bugün gerçekten ne değişti
- **Masa-11 (09-11) → Karar 94:** İB-81 erteleme aynen ("M7'ye başla" tetik değildi; ders deftere) · öğrenme serisi = evals (`ogrenme/evals/`, 7 hafta) · R4+R5 dar işçisi İB-81 tetiğine bağlı. İB-81 kuru-koşum aracı `tools/tuzuk-iz-tarama.py` + raporu havuzda (47 madde, 9 izli, 17 iz).
- **Karar 94 EK-1..4 (09-14/15):** ürün turu (seri sonu → aday → 3 model → metrik önce → hüküm → ana-sırada icra) · güncel-pratik şartı (dar canlı tarama) · güvenlik şeridi `ogrenme/guvenlik/` (6 hafta, sektör başlığı sütunu; evals'a geriye dönük eklendi) · öğretim biçimi standardı = ogren v0.1 iskeleti · skill-oluşturma alt-adımı (g) + kavram-dersi icra-türü eşlemesi.
- **Büyük-harf vurgu sızıntısı (Salih yan-görevi 09-15):** kök neden ölçüldü (yüklenen kanon 20-73‰, Sonnet çıktı 1,4-3,2‰) → Stop hook `stop-buyuk-harf.sh` (test 5/5; canlı tetiklendi) + ders yolu dosyalarında 47 sözcük küçültüldü; kalan kaynaklar Salih (a): olduğu gibi, 5 seans sonra ölç (sayaç 0/5).
- **Karar 95:** yan oturum = kendi branch + push + PR; merge yalnız ana-sıra Fable (`wiki/paralel-oturum-protokolu.md` §5).
- **Masa-12 (09-15) → Karar 96 (7 kalem):** üç yuva md hiyerarşisi — `~/.claude/CLAUDE.md` kullanıcı düzeyi YAZILDI (repo dışı, 10 madde) + `.claude/rules/{ogrenme,cc,tools}.md` (`paths:`) · 14 skill adayı (A1-A6 bağlam-uzayından, Ö1-Ö8 öğrenmeden) · şema v1.1 `core/skill-uretim-semasi.md` §4b · **hazine tavanı KALKTI (Salih beyanı)** → F6 seçim-isabeti + katalog `.claude/skills/README.md` · InstructionsLoaded hook + `veri/bronz/talimat-yukleme-olay.jsonl` · üretim partisyonlu P1-P3 (hız ilkesi) · staj bilgisi genelleştirilmiş formatta tek hazine.
- **İB-88 P1 tamam:** `karar-masasi` skill iskeleti (deterministik `scripts/masa-uret.py`, şablon, 3 eval + 5/5 description eval, kapı denetimi 0 hata). Kapı denetimi F1e ölçüm-only ve F1b harf-duyarsız yapıldı.
- **md→skill atlas koşumu:** 3 aile × tez + antitez + V26 sondaj (4 birincil belge aynen) + maskeli hakem (Opus). Hayatta-kalma A1 9/1/2 · A2 8/6/1 · A3 9/3/0. Düşenler: "resmî kural yok", "en son okunan en etkili", Kun Chen Program Bench atfı. Raporlar `cc/rapor/2026-09/rapor-2026-09-15-md-skill-*.md`. `tools/baglam-skill-aday.py` (183 bölüm skorlandı).
- Yan oturumlar (Sonnet): evals H1-H3 DONE (κ=1,0), H4 açık; guvenlik G1 kavramsal DONE. Dosyaları yan oturumun branch/PR'ına ait, bu seans dokunmadı.

## 2. Hangi karar verildi (kaynak · gerekçe · geri-açma)
Karar 94 + EK-1..4, Karar 95, Karar 96 + M2 EK (tavan kalktı) — hepsi `kuyruk/senaryo-defteri.md`'de Salih beyanı aynen. Geri-açma: Karar 96 F6 için 10 skill-kapisi koşumu sonrası ölçüm; hazine tavanı yeniden ancak tetiklenme isabeti düşerse ve Salih isterse.

## 3. Hangi fikir ADAY kaldı (karar değil)
- Atlas ana ajanı çocuk açınca kendiliğinden devam etmiyor → sentez ana-sırada ya da SendMessage ile uyandırma (atlas-kosum gotcha adayı).
- InstructionsLoaded ham alan şeması ilk 3 seanstan çıkarılacak (İB-87 silver tablo).
- Kapsül 8134/8192 B, defter 63 KB / 48 (aşım) → damıtma adayı Karar 89-93 blokları.

## 4. Sonraki ilk iş
Kapsülde: İB-88 P2 (masa-12 spec'e dök, elle yazılanla karşılaştır) → İB-89 ogren evrimi → İB-91 acilis-kapilari.py → … ; İB-86 CLAUDE.md damıtma (globale taşınan satırlar); İB-87. Öğrenme: evals H4, guvenlik G1 pratik.

## 5. Yeniden-açma koşulu
İB-81 yalnız Salih "İB-81'i başlat" beyanıyla. Hazine tavanı yalnız isabet düşüşü + Salih. Büyük-harf kaynakları 5 seans sonra ölçüm.

## 6. Kapılar + hasat kontrol listesi
- test-kapısı: 121 test · FAIL 0 · skip 7 · silver-sağlık exit 0 (yetim 39/351, T-B-KAPANDI aday 105, T-A ön-eleme 500/7482) · kural sayacı 19/100 · skill-eşik yeni-pencere sapması 0 · bayat-çekim: kuyruk 0 · hareket-tablo PASS.
- boyut-tetiği: defter 63/48 KB · kapsül 8,1/8 KB (sınır) · CLAUDE.md 7168/7168.
- uzun-koşum: max bağlam 228k (66 tur 128K üstü, 96 tur, çıktı 146k token). Hasat: (1) kalıcı kural adayları ingest'e girdi (defter/README/şema) · (2) açık pipeline yok; atlas koşumu tamamlandı · (3) alt-ajan tahmin↔gerçek: 7 ajan ≈680k [?] (`v_skill_kosum` atlas satırları) · (4) paralel oturum canlıydı (evals/guvenlik yan oturumları), commit'ler yol bazlı, çakışma 0.
- araç-çıktısı aşımı: yok (uzun çıktılar dosyaya yazıldı).
- Seans hedefi (m.29, sayaç 5/5): açılış hedefi "M7 karar-modeli + hüküm" TUTTU; üstüne 3 masa-kalemi paketi + skill hattı (hedef genişledi, sapma değil). **5 seans doldu → mini-değerlendirme sonraki masaya.**
