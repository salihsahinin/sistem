# Seans teslimi — 2026-09-10 (Friday tur-1/tur-2 dönüşü · masa-10 Karar 92 · Karar 93 ad değişimi)

*Yazan: Jarvis (ana-sıra, Fable; eski ad Carvis emekli bu seansta). Oturum 09-09 16:35 "seans başı" ile açıldı, 09-10 sabah devam etti (resume), ~13:2x "seans bitimi". Şablon `core/sablonlar/seans-teslim.md` (beş soru). Rakamlar bu seansın sayımı (m.39); deneysel m.29.*

## 1. Bugün gerçekten ne değişti
- **İB-82 KAPANDI:** Friday ilk canlı koşumu doğrulandı (09-09 16:49, auto-mod): 25 çağrı · kanon yazma 0 · push 0 · Jarvis kanon-dışı yol 0 → Karar 90 A1 = 1/1. Parti-5 çıktısı (KILAVUZ "Nerede ne var" + 9 ay-README) denetim listesiyle (8 kontrol, 5 düzeltme) Jarvis'e yerleşti.
- **Friday tur-1 A1-A10:** 10/10 düzeltildi — 2 gerçek arıza (okuma kilidi yanlış-pozitif/negatif; kütükte Bash yolu yok) hook v0.2 + 9 test ile, 8 tutarsızlık metin/şemayla.
- **Masa-10 (Lavish, 8 kalem → Karar 92, 8/8 önerilen):** İB-80 FIFO = K madde birincil (`tools/sicak-katman-fifo.py`, NFC-safe; MEMORY ilk canlı indirim) · artık dosyalar taşındı (`.lavish/` gitignore + `kaynak-kodu/lavish`, canvas karantina) · R1-R5 kademeli · desen 20 kabul · üç damıtma (kapsül 8,85→5 KB; defter Karar 87-88 arşive; Friday CLAUDE.md §6) · m.42(h) emir iç-çelişkisi kuralı · M7 = tek/alan-lider + İB-81 · push kapanışta.
- **Karar 92 EK — determinizm daraltması:** gövde `core/deterministik-tasarim.md`; CLAUDE.md'de 4 iş türüyle sınırlı tek satır; sohbet/öğretim/karar sunumunda sessiz.
- **Karar 93 — ajan adı JARVİS, Carvis emekli:** canlı bağlamda 60 dosya / 165 geçiş; tarihli kayıtlar AS-OF; sistem = "depo"/"kanon". **EK:** ad-eşitliği her bağlam kombinasyonunda — 3 katman (her-seans yükü · dizin README blokları · halef sözlük) + `tools/ad-esitligi-denetim.py` PASS.
- **M7-1 = A:** alan ajanı = Jarvis alt-ajanı, ayrı repo yok. **İB-83 DONE:** `.claude/hooks/pretool-altajan-okuma.sh` (agent_id varsa transkript · kapsül/pano/defter/kutu/MEMORY · kütükler · Friday · dış projeler RED; test 9/9; settings.json'a bağlı; canlı n=0).
- **Friday tur-2 (aynı oturum, sohbete bırakılan md — ilk A0 örneği işledi):** S1 X → hook v0.2 kalıcı · S2 K → deny satırı yok · S3 D → İB-83. B1-B5 bulguları: kütük v0.3 (`sema`, `devir_id`, agent alanları) · A3 madde-birincil · şablon kuralları (301 takibi, 1-derinlik kapsam, md tek kaynak). **İB-84 görev formatı planı** `kuyruk/gorev-format-gecis-plani-2026-09-10.md`; tur-2 B2 sonrası A1'e geçildi (md + lojik blok, json türev; `devir-md2json.py` borç).
- **M7-2 / İB-81:** Salih soruları cevaplandı; ERTELENDİ (Salih: sıkıştırılmış metinde bağlama neyin girdiğini yalnız model bilir).
- Kapsülde "## Şu an" başlığının önceki paragrafa yapışık olduğu bozukluk bulundu ve onarıldı (hook/sayaç bölümü görmüyordu).

## 2. Hangi karar verildi (kaynak + gerekçe + geri-açma)
- **Karar 92** (masa-10, 8 hüküm + EK determinizm) — defter bloğu; geri-açma: her kalem veto = revert, K değerleri 5 kapanış sonra revize.
- **Karar 92 M7-1** (tek lider; alan ajanı alt-ajan; doğum tetiği (c) zorunlu ∧ (a∨b)) — geri-açma: ≥3 devir/ay ∧ bağımsız bağlam gereksinimi.
- **Karar 93 (+EK)** ad değişimi + eşitlik garantisi — geri-açma: Salih beyanı; tarihçe arşivde aynen.
- **İB-81 ertelendi** — tetik Salih beyanı.

## 3. Hangi fikir ADAY kaldı (karar değil)
- Sisteme ayrı ad takma (Salih: "gerekirse") — şimdilik "depo"/"kanon".
- Friday pano "kanıt yolu" sütunu (Friday önerisi, öncelik düşük).
- `transcript_path` ile Friday kütüğü (belgeli ama gecikmeli; okuma izni dışı) — kullanılmadı.
- Tur-3 içeriği: aday `/docs/en/permissions` (S2 kapanışı) — hüküm sonraya (Salih).
- Wiki-delta (kuyruk): `wiki/ad-esitligi.md` (Karar 93 EK mekanizması) · `wiki/gorev-format-gecisi.md` (İB-84) · `wiki/paralel-oturum-protokolu.md`'ye Friday alt-ajan kilidi satırı.

## 4. Sonraki ilk iş
Kapsül "Sonraki ilk iş" 0-4: İB-84 A1 lojik-blok şeması + `tools/devir-md2json.py` · tur-3 (Salih içerik hükmü) · İB-83 ilk canlı koşum · sözlük başlığı emekli işareti (deny; Salih el işi) · defter damıtma (52,4→55/48 aşım: Karar 89-91 sıcak, aday `[icra] 09-09 11:30` bloğu).

## 5. Yeniden-açma koşulu
İB-83: alt-ajan kütüğünde ilk RED ∨ yanlış-pozitif beyanı · İB-80: 5 kapanış sonra bayt eşiği revizyonu · Karar 93: yeni canlı dosyada "Carvis" (denetim K3 FLAG) · İB-84: 2 devir üst üste emir-kaynaklı sapma 0 → A2 tartışması.

## Kapılar (6a-6g)
- test-kapısı: 121 test · FAIL 0 · skip 7 (iki koşum: 12:0x ve kapanış).
- kural-sayacı: 19/100 · silver-sağlık: kapanış koşumu (katman-hatti sonrası) · pointer-kayma 0/294 · anakronizm D1 0 · bayat-çekim: kuyruk 0 · skill-esik: eşleme boş, sapma 0 · ad-eşitliği PASS · FIFO 4/4 OK.
- boyut-tetiği: **senaryo-defteri 58,8/48 KB AŞIM** (Karar 92/93 blokları; damıtma adayı yazılı) · KILAVUZ 15,3/16 · CLAUDE.md 7,00/7 tam · kapsül ~6,3/8 · pano 10,1/12 · kutu 14,2/20.
- bağlam seyri: iki parça — 09-09 (2a11c9ee): 49 tur · max 122k · 128k+ 0 · çıktı 44k; **09-10 (1268ffa1): 263 tur · ilk-tur 124k · max 443k · 128k+ 258 tur · çıktı 920k** → **uzun-koşum: max bağlam 442.764 (258 tur üstte)**; statik-önek uyarısı 124k > 60k (KB-50 a; kestirim ilk mesaj dahil) → hasat kontrol listesi aşağıda zorunlu koşuldu.
- hasat kontrol listesi: (1) kural/karar adayları deftere girdi ✓ (2) açık pipeline yok; Friday tur-2 geri-dönüşü kopyalandı ✓ (3) ajan koşumu yok (Workflow yok) ✓ (4) paralel oturum: galeri şeridi 09-09 akşam kapanmış; izlenmeyen 2 gorsel HTML o şeridin, dokunulmadı ✓.
- araç-çıktısı aşımı: yok (en büyük tek çıktı Friday tur-1 dosyası ~9 KB).
- Seans hedefi (m.29, sayaç 2/5): "Friday dönüşünü almak + masa-10 kalemine hüküm" → TUTTU; sapma: hedefin dışında Karar 93 ad değişimi + İB-83 kilidi eklendi.

## Teslim yolları
- Bu rapor: `/Users/HasanSalihSahin/jarvis/raporlar/seans/seans-teslim-2026-09-10-friday-tur1-2-karar92-93.md`
- Masa-10 yüzeyi: `/Users/HasanSalihSahin/jarvis/raporlar/masa/masa-10-karar-yuzeyi-2026-09-10.html`
- Friday cevapları: `/Users/HasanSalihSahin/friday/cc/gelen/tasarim-2026-09-09-tur1-cevap.md` · `/Users/HasanSalihSahin/friday/cc/gelen/tasarim-2026-09-10-tur2-cevap.md`
- Kanıt kopyaları: `cc/devir/friday-2026-09-09-parti5/` · `cc/devir/friday-2026-09-10-tur2/`
