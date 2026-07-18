# Seans Yaşam-Döngüsü + Cowork↔CC Senkron + Senkron-Skill — Rapor (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit onaylı (Salih 07-18); nihai karar = Fable (m.41). Kaynak: Salih 07-18 — "end-of-day ve günaydın skill'ini hem Cowork'ten hem CC'den senkron çalışabilecek hale getirip 'seans başla' / 'seans bitir' gibi bir dile çevirebiliriz; hatta senkron çalışmamıza yardımcı bir skill oluşturabiliriz; bunları araştır çift-yönlü atlas, rapora ekle." Atlas 2 şerit: seans-yaşam-döngüsü+cross-surface senk (a9cb965d — KOŞUYOR) + insan-ajan senkron-ritüelleri (a9cb75ad — döndü).

---

## 0. BLUF
Salih'in fikri = **iki mevcut ritüeli** (`morning`/end-of-day) tek bir **seans yaşam-döngüsü** diline (`seans başla`/`seans bitir`) çevirmek + Cowork ve CC yüzeylerinde **senkron** kılmak + bir **senkron-skill** ile bağlamak. Atlas bulgusu: yeni ritüel icat etmeye gerek yok — mevcut set (`morning`/`hizalama`/vardiya-teslim) **git-as-truth üstünde `pull → iş → checkpoint → push`** omurgasına dizilir, üstüne **drift-tespiti → yeniden-hizalanma** kesme-döngüsü. Kanonlaşmış "insan-AJAN senkron ritüeli" çerçevesi **yok** (alan 2025-26 yeni); sentez bitişik olgun alanlardan (pair-programming, Scrum, deep-work, grounding-dilbilimi, HITL) türetildi ve bunlar **aynı 3 ilkeye yakınsıyor** = yüksek güven.

## 1. Salih'in fikri (çekirdek)
- **`morning` + end-of-day → seans dili:** "seans başla" (açılış) / "seans bitir" (kapanış) tek tutarlı çift.
- **Cross-surface senkron:** aynı seans-döngüsü hem Cowork (Fable ana-hat) hem CC (Opus yan-oturum) yüzeyinde çalışır; iki yüzey birbirini bozmadan devralır.
- **Senkron-skill:** Salih+JARVIS'in senkron çalışmasına yardımcı, seansları yöneten bir skill.

## 2. Cross-surface senkron mekanizması (Atlas a9cb965d döndü — TEZ tarafı)
**★ TEK EN ÖNEMLİ BULGU (mimariyi belirliyor): Claude Cowork, Claude Code'un HOOK sistemini ÇALIŞTIRMAZ.** SessionStart/SessionEnd/Stop/UserPromptSubmit yalnız Claude Code yüzeylerinde (CLI+web+IDE) ateşler; Cowork'te yok (GitHub Issue #47993, closed-dup #40495; #63360). Ayrıca Cowork'te "CLAUDE.md ilk-mesaj güvenilmez" (model açılış-ritüeli yerine ilk mesaja cevap verir). ⚠ *hareketli hedef* — hook desteği açık feature-request; bugüne göre kur, gelirse CC-bonus. → **Bu, rapor 3'ü tam onaylıyor: ortak substrat = CLAUDE.md + Skill, hook DEĞİL.** "seans başla/bitir" taşınabilir katman = **Skill**; hook = yalnız CC-tarafı deterministik hızlandırıcı/sigorta.

**Katmanlı savunma (aynı ritüel, 3 mekanizma):**
- **Katman 1 — Skill (taşınabilir, her iki yüzey):** `/seans-basla`, `/seans-bitir`. Ritüelin *beynini* (damıt/sentez/yetki-beyan) taşır. `!\`git pull\``/`!\`sed -n '1,40p' kapsül\`` **render-zamanında** (Claude görmeden) koşar → pull-önce-başla skill içinde bile deterministik.
- **Katman 2 — SessionStart/End hook (yalnız CC, deterministik):** `settings.json`; `additionalContext` ile kapsül+pano+**yetki-banner** enjekte (rapor 3-Opsiyon 2 "mimari>talimat" gerçeklemesi). **★ Kritik kısıt: SessionEnd = yan-etki-only, model-turu YOK → damıtma hook'ta YAPILAMAZ.** Damıt-adımı zorunlu olarak Skill; SessionEnd hook yalnız sigorta (commit'siz iş varsa WIP-snapshot + uyarı).
- **Katman 3 — CLAUDE.md sözleşmesi (Cowork sigortası):** "seans başla" fiili tabanda tanımlı; Cowork'te sağlam yol = kullanıcının açık "seans başla" demesi (skill claude.ai hesabında etkin — ⚠ interaktif-yerel Cowork'ün proje-`.claude/skills/` okuduğu doküman-net-değil; güvenli varsayım = hesap-senkron + CLAUDE.md sigorta).

**Cross-surface senkron mimarisi (git-as-truth tek substrat):**
- **"Kaldığın yerden devam" — İKİ resume seviyesi:** (a) CC seans-resume (`--continue/--resume`, transcript-seviyesi, aynı-yüzey) ≠ (b) **JARVIS vardiya-resume** (git-seviyesi, **çapraz-yüzey**). Taşınabilir resume-token = **durum-kapsülü "Sonraki ilk iş"** (transcript değil, kapsül). Cowork↔CC sürekliliğini bu sağlar.
- **Kadans:** her yüzey açılışta **önce `git pull`** → kapsül+pano oku → yetki-beyan; kapanışta delta-damıt → kapsül-üzerine-yaz → teslim-rapor(append) → granular-commit → push(V43).
- **Çakışma (Obsidian-Git dış-pratik yakınsak reçetesi):** yazma-uzayı **m.41 ile partisyonlanmış** (kanon=ana-sıra+Fable; yan-yüzeyler propose-only **append-only** `kuyruk/`·`cc/`·`raporlar/`) → aynı-dosya çakışması nadir. Olursa **kanon-dosyada ana-sıra kazanır** (remote/precedence-wins); yan-yüzey önerisini `kuyruk/`'a rebase. **PreToolUse `deny`** (managed) yanlış-yüzey `core/` yazımını yapısal engeller (m.1-2 klavyede-başkası'nın koda-dökülmüş hali). Kapsül=snapshot(üzerine-yaz)/log=append-only-truth (kapsül=projeksiyon).
- **Komut-dili (clig.dev verb-noun + git porcelain):** `seans başla`/`bitir` = porselen fiiller; karmaşık plumbing (pull/read/authority/distill/commit/push) tek fiil arkasında. Bookend simetrisi (pull↔push, kapsül-oku↔yaz, yetki-beyan↔teslim); Newport "shutdown complete" ↔ JARVIS **"Vardiya teslim ✓"**. Aynı komut-stringi iki yüzeyde çalışır çünkü skill-adı ortak.

**Dış çapa (end-of-day/günaydın deseni):** Newport shutdown-ritüeli (sabit-sıra + sözlü-işaret = psikolojik-sınır; ⚠ "JAP 2019" iddiası ikincil, doğrulanmadı) · Obsidian **Rollover Daily Todos** (tamamlanmamış todo'ları ertesi güne taşı) = **durum-kapsülü "Açık borçlar" + "Sonraki ilk iş" carry-forward'ının konsept-emsali.**

## 3. İnsan-ajan senkron ritüelleri (Atlas a9cb75ad döndü — 3 mercek)
Bağımsız alanlar (pair-programming, Scrum, deep-work, dilbilim, HCI, AI-coding) **aynı üç ilkeye** yakınsadı — bu yakınsama = yüksek güven:
1. **Periyodik ortak-zemin tazeleme** · 2. **Sürücünün akışını koruyan rol ayrımı** · 3. **Açık başlangıç/bitiş sınır-ritüelleri.**

**Üç mercek:**
- **Grounding (epistemolojik) — Clark & Brennan 1991:** iletişim = iletim değil; alıcının anladığına dair **kanıt (uptake)** gerekir; "amaç için yeterli" ortak-zemin, *en-az-ortak-çaba* ilkesiyle kurulur. → checkpoint = uptake üretme anı: JARVIS "yaptım" demez, **"şunu-şöyle anladım, X varsaydım, doğru mu?"** der. Ortak-zemin seans-arası **durum-kapsülünde** somutlaşır (= insan-AI "Shared Mental Model"in dosya-hali).
- **Akış/rol (ergonomik) — strong-style pairing:** navigator 2-20 şeyi izler, driver **tek** şeyden sorumlu → driver akışta kalır ("fikrin kafandan bilgisayara gitmesi için başkasının ellerinden geçmeli" = m.17 köprü birebir). Salih=navigator (karar/feedback), JARVIS=driver (commit/kod); köprü JARVIS'e **tek net adım** iletmeli. Kesinti→tam-odak dönüşü ~23 dk (Gloria Mark, doğrulandı) → checkpoint **sık ama hafif**, yoksa akış runway'i (15-20 dk) sıfırlanır.
- **Sınır-ritüeli (psikolojik) — Newport shutdown + Pomodoro:** açık başlangıç/bitiş işaretleri bilişsel kapanış/açılış sağlar; sözlü kapanış ("shutdown complete") ucuz ama işlevsel → JARVIS'te **"devir tamam".**

## 4. Senkron-skill tasarımı (a9cb75ad; a9cb965d ile cross-surface genişleyecek)
**Öz:** senkron-skill yeni ritüel icat etmez — mevcut seti **git-as-truth üstünde seans-yaşam-döngüsü omurgasına** dizer. İskelet: **pull → iş → checkpoint → push** + **drift → yeniden-hizalanma** kesmesi. Bu, HITL modelinin ("ajan bağlamı tutar, insan direksiyonu tutar") git ile somutlaştırılmış hali.

```
PULL (seans başla) → İŞ (odak-blok, strong-style, working-out-loud)
   → CHECKPOINT (nokta: micro-commit + uptake + drift-kontrol)
   → PUSH (seans bitir: kapsül güncelle + push + "devir tamam")
   ↺ drift → hizala
```

**Çalışma-ritüel seti (V24 isim-disiplini: mevcut adlar korunur, skill orkestra eder):**

| Ritüel | Faz | Ne yapar | Kanon durumu |
|---|---|---|---|
| `morning` / **seans başla** (taze) | PULL | Tam açılış-hizalanması: okuma-sırası + git log → ortak-zemin; standup 3-soru (dün-nerede/bugün-ilk-iş/bloke) | Var |
| `senk` | PULL (devam) | Hafif gün-içi yeniden-senk: kapsül+pano+son commit | **Yeni** (morning'in hafif hali) |
| `odak <süre>` | İŞ | Timebox/Pomodoro iskelesi; büyük iş parçalanır (m.21) | **Yeni** (ops) |
| `nokta` | CHECKPOINT | Micro-commit + tek-satır uptake + drift kontrolü | **Yeni** |
| `hizalama` | REPAIR | Talep/drift üzerine üç-yüzlü (m.18) yeniden-hizalanma | Var |
| vardiya-teslim / **seans bitir** (`devir`) | PUSH | Shutdown ritüeli: kapsül güncelle (makine-yüzü) + tek-satır insan-yüzü + push (m.9) + "devir tamam" | Var |
| `durum` | (her an) | Üç-yüzlü durum (m.18) | Var |

**Drift-repair tetikleyicileri (grounding-repair):** yol-sapması (yapılan iş kapsül "sonraki iş"ten uzaklaştı → m.16 hafif analoğu) · birikmiş commit'siz durum · çelişen yeni emir (→ m.16 tam devreye) · uzun sessiz seans (akış runway aşıldı). Onarım = `hizala`: üç-yüzlü özetle, sapmayı adlandır, tek-net-yön al, kapsülü tazele.

**Skill mühendisliği (Claude Code gerçeği):**
- Yan-etkili fazlar (`seans bitir`=commit+push) → **`disable-model-invocation: true`** (model kendiliğinden publish/push tetiklemesin, yalnız açık çağrı).
- **Sigorta hook'a girer, gerisi kibar öneri:** "her seans-bitir'de kapsül güncellenmeli" gibi *garanti* bir SessionEnd hook'u olmalı, skill metni değil (m.5 sigorta-istisnası birebir).
- Her skill'e "gotchas" bölümü.

**Komut-dili UX (clig.dev — ⚠ birincil 403, ikincilden):** fiil-önce Türkçe emir kipi (`senk`/`odak`/`nokta`/`hizala`/`devir`/`durum`), git zihinsel-modeline oturur (pull=seans başla, checkpoint=nokta, push=seans bitir); minimallik (6 çekirdek fiil), tutarlılık (aynı fiil her yerde aynı iş), öğrenilebilirlik (çıplak `senk` akıllı-varsayılan → `senk --pano` ileri), keşfedilebilirlik (her komut "ne yapacağım" basar; `devir` onay ister = HITL). Yeni fiil ancak "iki-kereden-fazla yapılan iş" için (m.5/skill-fikri-kutusu kuralı).

## 4b. ANTİTEZ (çift-atlas karşıt-şerit — a4c54362 döndü) — Red-Team + Sentez
> **Çerçeve:** m.37 karşıt-temel girdisi; steelman, çürütme değil. **Çekirdek ayrım:** tören-literatürünün ~%90'ı ÇOK-KİŞİLİ takım-koordinasyonundan; JARVIS TEK-kullanıcı+LLM-sürücülü → bazı parçalar çöker, hepsi değil.

**Top karşı-argümanlar:**
- **★ (en güçlü) Özel komut-DSL negatif-değerli:** LLM doğal-dili zaten anlar → senk/nokta/odak gibi bespoke fiiller saf öğrenme-maliyeti (Rasa; "doğal-olmayan gramer ölçülebilir-daha-zor", De Gruyter/hakemli). **★★ İç-tutarlılık silahı: Rapor 8'in KENDİ kuralı** (`skill olur ⟺ destek≥minsup ∧ MDL>0`) + m.37 yakınsama → fiiller henüz minimum-destek eşiğini geçmedi → **tez kendi YAGNI-kapısına takılıyor.**
- **Cargo-cult/tören-yükü:** zorunlu ritüel form>sonuç, esneklik-öldürür (Fowler dengeli görüş); ama kaynaklar katman-5 (opinion, kutuplaşmış), RCT yok — takımdan-transfer riski.
- **Cross-surface senkron kırılganlığı:** "drift-repair" mekanizması iki-yüzey senkronunun kırılganlık İTİRAFI; SSoT olgun-sonucu = "yazma-yetkili yüzey sayısını minimize et" (Unito/nojitter "doğru kaynak doğru zaman").

**Steelman (tez sağlam nerede — birey+LLM deliliyle):** ① sınır-ritüeli **bireysel-bilişsel** değeri gerçek (Zeigarnik / Leroy attention-residue, hakemli) — "seans bitir = açık-işleri-yakala + plan-bırak" tek-kişiye uygular; ② **Checklist = ağır-değil, hayat-kurtaran** (Gawande merkezi-kateter %11→0) → "seans başla/bitir" DSL değil **CHECKLIST** olarak çerçevelenirse m.5 sigorta-istisnası meşrulaştırır; ③ **LLM seanslar-arası boş-sayfa** gerçek (context-handoff, üretici-issue'lar) → durum-kapsülü + git-log tüm mimarisi bu tezin uygulaması. **Uyarı:** "context-dump fallacy" → devir SEÇİCİ olmalı (delta), tam-döküm değil (= m.34).

**SENTEZ (★ 3 parça, 3 kader — ayıraç: CHECKLIST mi / DSL-TÖREN mi):**
- **ANTİTEZ kazanır (fiil-DSL parçası):** senk/nokta/odak/hizala/devir'i **ŞİMDİ dondurma**; doğal-dil kullan, tekrar-deseni veriyle kanıtlanınca (destek≥minsup, rapor 8) skill'e döndür (= m.37 "hamleyi minimize et").
- **TEZ kazanır (ritüel+süreklilik parçası):** "seans başla/bitir"i DSL değil **CHECKLIST/state-capture** olarak koru (fiilsiz düz-talimat) — LLM boş-sayfa + Zeigarnik/Gawande değeri gerçek; m.5 sigorta.
- **KOŞULLU (senkron parçası):** iki-yüzey için ayrı-mekanik kurMA; **git-log tek-depo** üzerinden oku/yaz — zaten m.41 branch→Fable deseni; ayrı hook/çakışma-çözücü gereksiz karmaşıklık.
- **Tek cümle:** *Ritüeli tut (checklist, fiilsiz), DSL-i at (LLM doğal-dili anlar), senkronu tek-depoya indirge.*
- **m.16 tetiği:** tez "yeni fiil-kümesi + zorunlu ritüel" olarak lock istenirse m.5/m.37/m.25 ile çelişir → karar-öncesi çelişki-raporu; bu antitez o raporun kanıt-tabanı. ⚠ Kaynaklar çoğu katman-4/5, RCT yok, takımdan-transfer varsayımsal; en sağlam empirik = steelman tarafı (Gawande/Leroy/LLM-handoff).

## 5. Kanon bağı
- **m.27 (uyku/günaydın vardiya):** "seans başla/bitir" = m.27'nin skill-diline çevrilmiş hali; günaydın=PULL, iyi-geceler/devir=PUSH.
- **m.17 (köprü):** strong-style "fikrin başkasının ellerinden geçmesi" = köprünün ta kendisi; JARVIS'e tek-net-adım.
- **m.18 (üç-yüz):** `durum`/kapsül makine+insan+detay yüzleri.
- **m.16 (çelişki-kapısı):** çelişen-yeni-emir drift-repair'in en sert tetikleyicisi.
- **m.9 (proof-of-work):** `seans bitir` = push'lanmış commit.
- **m.5 (sigorta-istisnası):** garanti = hook, öneri = skill metni (birebir eşleşme).
- **m.1-2 (klavyede-başkası):** cross-surface senkron bunu koruma altına almalı (a9cb965d).
- **rapor 3 (CC okuma-sırası: yetkinlik-özdeş/yetki-ayrı):** cross-surface seans-devri bunun üstüne kurulur.
- **rapor 12 (gece):** `seans bitir`→gece-vardiyası→`seans başla` doğal zincir; gece-teslim `morning`e akar.
- **skill-fikri-kutusu (rapor 2) / skill-nasıl-oluşturulur (rapor 4):** senkron-skill bu metodolojiyle üretilir; `disable-model-invocation` + hook-sigorta orada da vurgulandı.

## 6. Açık sorular (Salih/Fable — KARAR ALINMADI)
- `seans başla/bitir` mevcut `morning`/vardiya-teslim'in **takma-adı** mı yoksa **yeni sarmalayıcı skill** mi?
- `senk`/`nokta`/`odak` üç yeni fiil kanona girsin mi, yoksa yalnız senkron-skill içi mi?
- Cross-surface: Cowork ve CC aynı anda açıkken çakışma nasıl önlenir (kilit/tek-yazar)? — a9cb965d bulgusuyla netleşecek.
- Sigorta-hook (SessionEnd kapsül-güncelle) K-009 (otomasyon bloke) kapsamında mı, yoksa lokal-hook serbest mi?
- `devir tamam` sözlü-kapanış zorunlu mu (ritüel) yoksa opsiyonel mi?
