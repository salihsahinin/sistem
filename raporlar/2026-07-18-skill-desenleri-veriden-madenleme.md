# Skill Desenlerini Eldeki Veriden Madenleme — Rapor (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit onaylı (Salih 07-18); nihai karar/merge = Fable (m.41). Kaynak: Salih 07-18 — "öğrenme desenleri gibi, eldeki tekrar eden verilerle skill desenleri de oluşturabiliriz; nasıl yapacağımızı araştır." Atlas 2 şerit: (A) veriden madenleme (koşuyor) + (B) öğrenme→skill-deseni analojisi (koşuyor).

---

## 1. Fikir + öğrenme-şeridi analojisi (çekirdek)
Öğrenme şeridi (ogrenme/, Şerit 2) deneyimden desen üretir: **Atlas-araştırma → müfredat (partisyonlu) → [Yarı-1 tersine-mühendislik/anla + Yarı-2 mühendislik/3-model] → dersler/ kaydı → kapsül.**
**Skill-deseni analog** aynı makineyi kullanır ama girdisi FARKLI: dış-araştırma yerine **İÇ KORPUS** (kendi tekrar eden verimiz).

| Öğrenme şeridi | Skill-deseni analog |
|---|---|
| Atlas dış-araştırma | **korpus-madenleme (git-log, senaryo-defteri, raporlar, cc/defter)** |
| müfredat (partisyon) | skill-müfredat/aday-kütüphanesi (madenlenmiş desenler) |
| Yarı-1 tersine-mühendislik (konuyu 0'dan sök) | desen tersine-mühendislik (tekrar eden instance'ların ortak yapısını çıkar) |
| Yarı-2 mühendislik (3-model uygulama) | skill SOYUTLAMA (şablon + m.37 3-model: hangi soyutlama seviyesi) |
| dersler/ kaydı | skill-pattern kaydı → **skill-fikir-kutusu** |
| ders = BİLGİ | skill-deseni = **çalıştırılabilir/yeniden-kullanılabilir** |

## 2. Korpus — elimizde madenlenecek ne var
- **git-log:** karar-başına commit (m.10 = hafıza), İngilizce mesaj + [damıtma]/[icra] etiketi → aksiyon-dizisi/karar izleri.
- **senaryo-defteri.md:** karar blokları (bağlam + 3-model + seçim + **4-tuple gözlem** + ders) → en yapılandırılmış sinyal (ödül+desen).
- **raporlar/:** tartışma/araştırma çıktıları (bu oturumun 7 raporu dahil).
- **cc/defter.md:** ajan koşum kayıtları (görev→sonuç izleri).
- **ogrenme/dersler/:** öğrenme dersleri (bilgi-deseni).
- **skill-fikir-kutusu + POP bloğu:** zaten tespit edilmiş tekrarlayan kümeler + ertelenmiş optimizasyonlar.
- **CHAT/CEP-KAPSULU + pano/kapsül tarihçesi:** yüzey-özel izler.

## 3. Madenleme yöntemleri + boru hattı (Atlas A — DONE)
**★ Tüm literatür aynı 3-adımda buluşuyor:** (1) **tekrar-tespiti** (frekans/destek) → (2) **soyutlama** (parametreleştirme) → (3) **doğrula-ve-kütüphaneye-ekle**. Ayrışma yalnız tekrarı NEYLE ölçtükleri (sözdizimsel destek / anlamsal küme / MDL-sıkıştırma).
**Yöntemler:** **★ Agent Workflow Memory (AWM)** = en doğrudan reçete (trajektoriden tekrar rutini "workflow" indükle; çevrimdışı+çevrimiçi) — **senaryo-defteri zaten AWM'nin ihtiyaç duyduğu yapılandırılmış trajektori; çoğu çalışma bu veriyi üretmek için ayrı emek harcar, JARVIS m.10/m.37 ile üretiyor bile.** · Voyager (çalıştırılabilir kod-skill birikimi) · PolySkill (soyut-amaç/somut-uygulama ayrımı = Facet-1/Facet-2'nin teorik gerekçesi) · TroVE (kullan→büyüt→**buda**, skill-sprawl panzehiri) · ExpeL/AutoManual (başarı/başarısızlık→NL kural = senaryo-defteri "Ders" + m.37 Karşıt-temel) · Frequent-Episode-Mining / PrefixSpan (SPMF hazır araç) · Process-discovery (Inductive Miner, commit-akışı=olay-log, sapma tespiti) · RPA task-mining (deterministik→script vs değişken→LLM = skill §4) · **anti-unification/LGG** (N somut → parametreli şablon) · **library-learning (DreamCoder/Stitch/babble, MDL kriteri)** · SOAR chunking (1986 — "skill=yakınsamış politika"nın atası).

**★ Soyutlama matematiği — "ne zaman desen, ne zaman tek-seferlik":** üç sinyalin kesişimi:
> **bir küme SKILL olur ⟺ destek ≥ minsup (yatay: yeterince tekrar) ∧ MDL-net-sıkıştırma > 0 (dikey: kütüphane maliyeti dahil korpusu kısaltıyor) ∧ LGG boş-olmayan sabit-iskelet + AZ slot bırakıyor (parametreleme: aşırı-genel değil aşırı-özgül değil).**
Üçü sağlanmazsa → tek-seferlik (arşive, m.8). MDL = skill-sprawl'a **kanıtlanabilir** kapı (sezgi değil).

**7-aşamalı boru hattı (JARVIS korpusuna, turnkey):**
0. **Normalize:** git-log + senaryo-defteri + cc/defter + raporlar → yapılandırılmış kayıt + aksiyon-dizisi. *(JARVIS'te ~bedava.)*
1. **Sözdizimsel tekrar:** SPMF/PrefixSpan → minsup üstü ardışık desen (`çelişki→3-model→karşıt-temel→seçim→kaydet→commit`) → **Facet-4 otomatik dolar.**
2. **Anlamsal tekrar:** "Ders"+rapor+skill-kutusu → embed→UMAP→HDBSCAN→c-TF-IDF→LLM-adlandır (BERTopic); **insan-in-the-loop ZORUNLU** (LLM etiketi taslak, m.31 Katman-1).
3. **Soyutlama:** anti-unification/LGG → sabit-iskelet + slot'lu parametreli şablon (SEÇİM/gözlem ayrımı slot sınırını verir).
4. **MDL kapısı:** net-sıkıştırma yoksa → tek-seferlik/arşiv.
5. **İskeletle + facet + description:** 4-facet'e otur → SKILL.md (eval-önce, description NE+NE ZAMAN+negatif-tetik, yan-etki→disable-model-invocation).
6. **Doğrula + dondur:** skill-creator eval (with/without, Haiku+Sonnet+Opus) → best-arm dondurma.
7. **Çevrimiçi yakınsama:** başarılı trajektori geri-besle (AWM online) + Contextual-TS seçim + helpful/harmful (G2/ACE delta). **Delta = neyin DEĞİŞTİĞİ (Gotcha sinyali) · frekans = neyin TEKRAR ettiği.**

**Öz:** bu rapor = **keşif/soyutlama tarafı** (episode-mining + anti-unification + MDL); yakınsama-formülü raporu (5) = **seçim/yakınsama tarafı** (bandit/BOHB). Birleşince tam döngü: **keşfet→soyutla→seç→dondur→geri-besle** — aynı madalyonun iki yüzü.
**Dürüstlük:** kişisel git+markdown karar-defterinden skill-madenleme için **isimli/hazır tek boru hattı YOK** → 7-aşama SENTEZ (bileşenler olgun+kaynaklı, birleşimi deneyle sınanmamış). WebFetch 403 → sayılar abstract (AWM %24.6/%51.1 çapraz-teyitli).

## 4. Öğrenme→skill-deseni analojisi (Atlas B — DONE)
**Çerçeveler:** **ACE** (evolving-playbook: Generator→Reflector→Curator, madde-bazlı **delta** + helpful/harmful sayaç + grow-and-refine) · **Voyager** (oto-müfredat + hep-büyüyen **çalıştırılabilir** skill-kütüphanesi) · **CBR** (Retrieve→Reuse→Revise→Retain — senaryo-defteri = vaka-kütüğü) · **ExpeL** (başarı+başarısızlık yörüngesinden NL içgörü) · Reflexion (sözel pekiştirme) · Experience-Replay (senaryo-defteri = replay-buffer; ~10-vardiya birik→dene = m.35) · AAR (retrospektif→cookbook→doktrin) · Alexander/GoF (desen **madenlenir icat edilmez**; sabit-form; **"rule of three"** ~3 tekrar).

**★ Üç "grain" (kritik ayrım — skill-vs-ders sorununun cevabı):** episodik (CBR/replay = **senaryo-defteri**) · semantik (ACE/ExpeL/AAR = **wiki/fikir-kutusu/tüzük = DERS**) · **prosedürel (Voyager = çalıştırılabilir kod-skill = JARVIS'te YOK → BOŞLUK burada).** = CoALA hafıza taksonomisi (müfredat P10-P11). Öğrenme şeridi **semantik** üretir (ders=bilgi); skill şeridi **prosedürel** üretmeli (skill=çalıştırılabilir). Aynı korpus, farklı artefakt.

**1:1 eşleşme (izomorfik):** ders↔desen/skill · müfredat↔skill-kütüphanesi · dersler/↔skill-fikir-kutusu→.claude/skills/ · anlama-kapısı↔**eval-kapısı** · Yarı-1↔madenleme · Yarı-2(3-model)↔skill-tasarımı · karar-adayı→Şerit-1 ↔ skill-adayı→Fable(m.41).
**Kasıtlı FARKLAR (asıl değer):** ontoloji (bilgi↔çalıştırılabilir) · kalite-kapısı (öznel "Salih söyleyebiliyor mu"↔ölçülen A/B) · yaşam-döngüsü (öğrenilince biter↔her koşumda evrilir→Adım-5) · değer-ölçütü ([S/O/T]↔tekrar×elle-maliyet) · bakım-riski (bayatlama↔skill-sprawl+context-collapse).

## 4.5 ★ KANON RİSKİ (Atlas'ın en kritik tekil bulgusu) — m.34 context-collapse
ACE iki başarısızlık modu tanımlıyor: **brevity bias** (özet uğruna içgörü atma) + **context collapse** (iteratif YENİDEN-YAZMA detayı erozyona uğratır). **m.34'ün "katman şişince derin katmana özütle / en iç = en önemli özütler" = monolitik yeniden-yazma = ACE'nin tam kaçındığı hata.** JARVIS damıtması ölçülmezse yapısal olarak açık.
**Çözüm (transfer):** damıtmayı **madde-bazlı delta** yap — yeni-madde-ekle / sayaç-artır / deprecated-işaretle; monolitik yeniden-yaz DEĞİL. **m.8 (silme-yok, geçersiz-kıl) + m.20 (pointer-over-kopya) yarısını zaten veriyor**; eksik yarı = **helpful/harmful sayaç + grow-and-refine dedupe**. → G3 dönemsel toplu-özüt, *tam-yeniden-özet* değil ACE-tarzı *dedupe+budama* koşmalı. **(Fable'a: bu bir m.34 revizyon adayı.)**

## 5. Önerilen skill-deseni üretim döngüsü (öğrenme şeridini AYNALAYAN — ön-taslak)
1. **Madenleme (Atlas-araştırma analogu):** periyodik olarak korpusu tara (embed+küme+LLM-adlandır + frekans/delta) → tekrar eden aksiyon/karar dizileri = skill-pattern adayları.
2. **Aday-kütüphanesi (müfredat analogu):** adaylar skill-fikir-kutusuna partisyon-partisyon düşer; destek-eşiği (≥N tekrar) altındakiler bekler.
3. **Tersine-mühendislik + soyutlama (Yarı-1+2 analogu):** her aday desenin ortak iskeleti çıkarılır → parametreli SKILL.md şablonu; m.37 3-model = "hangi soyutlama seviyesi/kapsam".
4. **Kayıt + eval (dersler analogu):** skill-creator Executor/Grader ile doğrula (skill-nasıl-olusturulur raporu §6); geçen desen skill olur.
5. **Evolving-playbook (G2/ACE):** helpful/harmful sayaç + delta-güncelleme; kullanılmayan desen budanır (POP m.37-yakınsama budaması); silme yok (m.8).
- **Fark-notu:** öğrenme çıktısı = ders (pasif bilgi); skill-deseni çıktısı = çalıştırılabilir politika → doğrudan `karar-hatti`/`karar-modeli` gibi skill'lere akar.

## 6. Kanon bağı
- **G2 evolving-playbook (ACE delta + helpful/harmful):** bu döngünün motoru; JARVIS'te zaten G2 konsepti.
- **skill-fikir-kutusu:** madenlemenin ÇIKTI hedefi (tekrarlayan-küme→skill kuralı, 07-17).
- **Yakınsama-formülü (rapor 5):** madenlenmiş desen = context; skill = yakınsamış politika; 4-tuple = ödül. Madenleme, o politikanın önselini besler.
- **m.10 (git-log=hafıza) + m.34 (katmanlı ingest):** korpus zaten madenlenebilir formatta; madenleme = ingest'in otomatik hali.
- **m.35 öz-referans:** sistem kendi çıktısından desen çıkarıp kendini geliştirir.

## 7. Açık sorular (Salih cevabı bekleniyor — KARAR ALINMADI)
- Madenleme periyodik-otomatik mi (Routine) yoksa elle-tetik mi (ilk boş vardiya)?
- Destek-eşiği (bir desenin "skill adayı" sayılması için min tekrar N) kaç?
- Madenleme çıktısı skill-fikir-kutusuna mı düşer yoksa ayrı "skill-deseni kütüphanesi" mi?
- Öğrenme şeridiyle aynı oturum-protokolü mü (Yarı-1/Yarı-2) yoksa ayrı şerit mi?
