# Seans Teslim Raporu — 2026-08-17 seans-8 (masaüstü uygulaması Claude Code = ana-sıra; Carvis/Fable; 09:04→~00:30)

*Şablon: `core/sablonlar/seans-teslim.md` (beş soru) + hasat. Kanıt: git log 08-17 (bu seans ~40 commit) · `raporlar/hareket-gunlugu-2026-08-17.md` (her araç çağrısı) · `kuyruk/senaryo-defteri.md` 08-17 bloğu (Karar 1-28, Beyan 9). Paralel jarvis oturumu aynı gün canlıydı (Beyan 10-11; `cc/gorev-2026-08-17-1/2/4`) — bu rapor yalnız bu seansın şeridini kapsar.*

## 1. Bugün gerçekten ne değişti
- **CLAUDE.md v2 sıfırdan** (v1 14 KB → v2 6,99 KB / 40 satır; davranış sözleşmesi, durum yok; bütçe ≤80 satır/≤7 KB kalıcı kural).
- **Açık kaynak + okunabilirlik altyapısı:** `kaynak-kodu/` (harita + `.claude` bağı) · `tools/hareket-tablo.py` (bronz→silver→gold + `raporlar/hareket-gunlugu-YYYY-MM-DD.md`, 08-12→08-17 geriye dönük) · `cc/workflow/` (script kopyaları) · `tools/yuzey-parmak-izi.py` · `LICENSE` (MIT) · seans-kapanis 6b adımı.
- **Türkçeleştirme:** ATLAS ajan tanımı (İngilizce aslı arşivde), Karpathy sayfası Türkçe özet, `mdbook_test.md` arşive; dil kuralı CLAUDE.md §2 + `kaynak-kodu/README.md`.
- **Metafor cascade:** 5 anahtar emekli (şirket/CEO/patron/şirket-simülasyonu/vardiya → Jarvis/köle/tek karar verici/çalışma modeli/seans), tüzük "Jarvis Tüzüğü v0", 15 SKILL.md + evals, şablon `seans-teslim.md`; K-024 ılık cascade (kayıtlar dahil, Salih B) → denetim sıcak 0 · ılık 0.
- **Stokastik entegrasyon geri alındı;** V26 kural-tabanlı (atlas-kosum adım 5); wiki sayfası emekli-güdük.
- **Damıtma (KB-37):** defter 180,9→42,7 KB (arşiv + 42 satır index, 28 pointer eşlendi), KILAVUZ 18,7→13,3 KB.
- **Karar masası 5 parti** (açıklama-bloklu, 20 kalem hükme bağlandı) + agile atlası (`cc/rapor-2026-08-17-3.md`, 12 işçi, 799k token, 7/22/1/0) → KB-46..49.
- Kanon dokunuşları: tüzük m.14 revize, m.41 GK-2, m.2/15/25/44 yeniden yazım, ajan-metodolojisi §4 model hiyerarşisi, world-model bus matrix +1 satır, veri-katmanı §8 S3 imza, halüsinasyon-paketi F7/V26, sema-sikistirma şerhi, gorev-fonksiyonu `kosum_profili`, gorev-emri SPEC/PLAN/TASKS, KILAVUZ Tasarım ilkeleri (hazırı temel al · V1 ölçek şerhi · V12 emekli · ağır araç yükleme usulü), `wiki/paralel-oturum-protokolu.md`.

## 2. Hangi karar verildi (kaynak + gerekçe + geri-açma) — Katman-1, Salih
Defter 08-17 bloğu: Karar 1 CLAUDE.md v2 · 2 açık kaynak (m.14 revize; geri-açma: remote public'e açılış ayrı karar) · 3 metafor emekli + halef sözlük (EK-2 K-024 B) · 4 kaynak Türkçe · 5 deterministik tasarım (stokastik geri; V26) · 6 okunabilirlik (hareket kütüğü) · 7 rol = köle · 8 V26 kural-tabanlı (A) · Beyan 9 hafıza mimarisi (wiki + veri teknikleri; vektör DB ertelendi) · Masa: 10 damıtma A · 11 KB-34 koşullu (ana-sıra Claude Code; Cowork parmak-izi; model = en güçlü) · 12 MIT · 13 A1 konusuz · 14 mobil kilit kalır · 15 yazım-anı ölçüm kapısı · 16 kosum_profili + model hiyerarşisi · 17 alt-model skill pilotu · 18 açılış kapıları · 19 paylaşılan kaynak freni · 20 H4 + H6 (bulut kopyaları silinir) · 21 karar-borcu kalıcı süreç · 22 KB-11 BEKLET→konusuz · 23 ağır araç yükleme usulü · 24 şerhli-5 kapandı · 25 HAZIRI TEMEL AL + V1 ölçek şerhi (KB-14 A) · 26 agile tetiği · 27 Windows TERK · 28 KB-17 a/c (b açık). Geri-açma: her karar defter satırında; veto = revert (m.31).

## 3. Hangi fikir aday kaldı (karar DEĞİL)
- KB-46..49 (agile çıktısı: started damgası + akış metrikleri · seans hedefi · arıza/revert etiketi · girmez listesi) — masaya.
- Spec-kit aracının kurulumu, "hazırı temel al" ilkesiyle yeniden değerlendirilebilir (Salih A: desen alındı).
- İcra borçları (Katman-2): ambar tahmin↔gerçek kolonları + `v_kosum_tahmin_sapma` · `v_skill_kosum` · gorev-emri-derleme "skill koşucusu = alt model" alanı · description-eval turu (K3).
- Sunum: `tools/sunum-proof-of-work.py` HTML'i üretilmedi (08-16 "dur").

## 4. Sonraki ilk iş
Karar masası kalanı — diğer oturumda, aynı format: KB-17b → 18 → 19 → 20 → 21 → 22 → 23…32 → 36 → 46-49 → paralel oturumun KB-39..45'i (`veri/karar-borcu.jsonl`, açık 30). Salih el işleri: bulut skill kopyalarını sil · Cowork sekmesinde parmak izi · `/context` sayısı.

## 5. Yeniden açma koşulu
- Cowork sekmesi ana-sıra: `tools/yuzey-parmak-izi.py` çıktısı eşitse (m.41 GK-2).
- Vektör DB / embedding erişim: grep+SQLite'ı ölçülmüş biçimde geçmezse girmez (veri-katmanı v1).
- Stokastik yöntemler: Salih Katman-1 kararı olmadan yeniden AÇILMAZ (deterministik tasarım ilkesi).
- V25 "yalnız ilham" kuralı: emekli; hazırı temel al.

## Hasat
- **Özütler:** (1) CLAUDE.md'ye durum yazmak uzun koşumda davranışı bozar → davranış sözleşmesi + bütçe. (2) Emeklilik cascade'i script'le deterministik yapılır; Salih sözleri/imza damgaları özgül izinli kalıplarla korunur, genel tırnak kalıbı tetik cümlelerini gizler. (3) Her karar sunumu açıklama bloklu olunca 5 partide 20 kalem kapandı — masanın ertelenme nedeni format eksikliğiydi. (4) Paralel oturum canlıyken `git add -A` gerçekten çarpar (paralel oturumun 7 KB kalemiyle numara çakışması: KB-39..42 → 46..49 yeniden numaralandı) — canlı-oturum kapısı + H4 doğru. (5) Model-hiyerarşili atlas 3× bütçe aştı; koşum profili tahmin↔gerçek tablosu ilk gerçek veriyi aldı.
- **wiki-delta:** açıldı `paralel-oturum-protokolu` · emekli-güdük `stokastik-dusunce` · güncellendi `baglam-veri-ambari` (hafıza mimarisi), `kokenler-karpathy-llm-wiki` (Türkçe özet), README/olcum-banki linkleri · kuyruk: `hazırı-temel-al` ilkesi + `model-hiyerarsisi` sayfaları (aday) · `deterministik-tasarim` sayfası (aday; ilke CLAUDE.md §6'da).
- **Verilebilir miydi (V20):** bu seans tamamen sistem-içi iş; PortRisk (m.13) ilerlemedi — Salih'e söylendi (m.6).
- **token×zaman:** oturum ~15,5 saat duvar-saati (öğleden sonra boşluk), ~40 commit; agile atlası 799k işçi-token / 23 dk; hareket kütüğü 1.354+ çağrı (08-17: bu seans ~700).
- **Boyut-tetiği:** pano 21,9/12 KB · fikir-kutusu 28,2/20 KB · senaryo-defteri 57,6/48 KB → damıtma turu (sorgu-uyumu hedefi).
- **İngest sayaçları:** giren 3 gelen (paralel-oturum vakaları) → UPDATE/ADD kural (KB-08/09), İNGEST EDİLDİ damgalı; DLQ 0.
